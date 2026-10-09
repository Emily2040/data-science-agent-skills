#!/usr/bin/env python3
"""End-to-end verification suite for the 25-skill catalog, deterministic scripts, and multi-stage workflows."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS = REPO_ROOT / "data-science-agent-skills"


def run_py(script: Path, *args: str) -> tuple[int, dict | str]:
    proc = subprocess.run([sys.executable, str(script), *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = (proc.stdout or "").strip()
    try:
        parsed = json.loads(out) if out else {}
    except Exception:
        parsed = out
    return proc.returncode, parsed


class TestCatalogEndToEnd(unittest.TestCase):
    def test_01_all_25_skills_validate_strict(self) -> None:
        code, data = run_py(REPO_ROOT / "scripts" / "catalog_cli.py", "validate", "--strict")
        self.assertEqual(code, 0, f"Catalog validation failed: {data}")
        self.assertEqual(data["passed"], 25)
        self.assertEqual(data["failed"], 0)

    def test_02_profile_table_mixed_numeric_and_safe_names(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = Path(tmpdir) / "mixed.csv"
            rows = ["model_name,feature_name,customer_name,score"] + [
                f"xgb_{i},feat_{i},Alice Smith,{i}.5" for i in range(19)
            ] + ["xgb_19,feat_19,Bob Jones,N/A"]
            csv_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
            code, data = run_py(SKILLS / "ai-data-readiness-triage/scripts/profile_table.py", str(csv_path))
            self.assertEqual(code, 0)
            cols = data["columns"]
            self.assertEqual(cols["score"]["inferred_type"], "numeric")
            self.assertEqual(cols["score"]["non_numeric_coerced_or_skipped"], 1)
            self.assertFalse(cols["model_name"]["pii_name_hint"])
            self.assertFalse(cols["feature_name"]["pii_name_hint"])
            self.assertTrue(cols["customer_name"]["pii_name_hint"])

    def test_03_split_leakage_probe_target_postal_and_missing_key(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            train_csv = tmp / "train.csv"
            eval_csv = tmp / "eval.csv"
            train_csv.write_text("user_id,postal_code,target\n1,94101,0\n2,94102,1\n", encoding="utf-8")
            eval_csv.write_text("user_id,postal_code,target\n3,94103,0\n4,94104,1\n", encoding="utf-8")

            # Clean split with target='target' and postal_code column -> exit 0
            code, data = run_py(
                SKILLS / "leakage-adversary/scripts/split_leakage_probe.py",
                str(train_csv), str(eval_csv), "--key", "user_id", "--target", "target"
            )
            self.assertEqual(code, 0)
            self.assertEqual(data["status"], "no_obvious_leakage")
            self.assertEqual(data["suspicious_columns"], [])

            # Missing key column -> blocked (exit 2)
            code_missing, data_missing = run_py(
                SKILLS / "leakage-adversary/scripts/split_leakage_probe.py",
                str(train_csv), str(eval_csv), "--key", "nonexistent_id", "--target", "target"
            )
            self.assertEqual(code_missing, 2)
            self.assertEqual(data_missing["status"], "blocked")

    def test_04_lineage_ignores_python_imports_and_extracts_sql(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            py_file = tmp / "pipeline.py"
            py_file.write_text("from pathlib import Path\nimport pandas as pd\ndf = pd.read_csv('events.csv')\n", encoding="utf-8")
            sql_file = tmp / "query.sql"
            sql_file.write_text("CREATE TABLE mart.daily_users AS SELECT * FROM raw.user_events JOIN dim.accounts ON id = user_id;\n", encoding="utf-8")
            code, data = run_py(SKILLS / "semantic-lineage-mapper/scripts/extract_lineage_tokens.py", str(py_file), str(sql_file))
            self.assertEqual(code, 0)
            self.assertNotIn("pathlib", data["tokens"]["sql_from_join"])
            self.assertIn("raw.user_events", data["tokens"]["sql_from_join"])
            self.assertIn("dim.accounts", data["tokens"]["sql_from_join"])
            self.assertIn("events.csv", data["tokens"]["file_path"])

    def test_05_drift_probe_catches_constant_shift_variance_and_nan(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            b_csv = tmp / "base.csv"
            c_csv = tmp / "cur.csv"
            b_csv.write_text("const_c,var_c,nan_c\n1,1,10\n1,-1,12\n1,1,11\n1,-1,9\n", encoding="utf-8")
            c_csv.write_text("const_c,var_c,nan_c\n1.5,100,NaN\n1.5,-100,10\n1.5,100,11\n1.5,-100,12\n", encoding="utf-8")
            code, data = run_py(SKILLS / "drift-monitor-designer/scripts/drift_probe.py", str(b_csv), str(c_csv))
            self.assertEqual(code, 0)
            self.assertEqual(data["columns"]["const_c"]["status"], "investigate")
            self.assertEqual(data["columns"]["var_c"]["status"], "investigate")
            self.assertEqual(data["columns"]["nan_c"]["status"], "investigate")

    def test_06_multi_skill_lifecycle_pipeline(self) -> None:
        """Chain 5 skills across the lifecycle on a clean vs leaky/unready project."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            # Stage 1: Question Framing
            canvas = tmp / "canvas.json"
            canvas.write_text(json.dumps({
                "decision_owner": "VP Retention",
                "decision_action": "Trigger proactive renewal offer",
                "analysis_unit": "account_id",
                "target_definition": "churn_within_30d",
                "time_horizon": "30 days",
                "primary_metric": "net_retention_lift",
                "action_threshold": "+2.0% lift over rule baseline",
                "guardrail_metrics": ["offer_margin_cost"],
                "target_available_at_decision_time": True,
            }), encoding="utf-8")
            c1, d1 = run_py(SKILLS / "data-question-framing/scripts/decision_canvas_validator.py", str(canvas))
            self.assertEqual(c1, 0)
            self.assertEqual(d1["status"], "go")

            # Stage 2: Baseline Ablation Lab
            ablation = tmp / "ablation.json"
            ablation.write_text(json.dumps({
                "baseline_score": 0.74,
                "candidate_score": 0.79,
                "min_lift": 0.02,
                "latency_ratio": 1.4,
                "max_latency_ratio": 2.5,
                "seeds_evaluated": 5,
            }), encoding="utf-8")
            c2, d2 = run_py(SKILLS / "baseline-ablation-lab/scripts/ablation_delta_audit.py", str(ablation))
            self.assertEqual(c2, 0)
            self.assertEqual(d2["status"], "go")

            # Stage 4: Evaluation Reality Check
            preds = tmp / "preds.csv"
            preds.write_text(
                "y_true,y_pred,y_prob,slice\n1,1,0.9,enterprise\n0,0,0.1,enterprise\n1,1,0.85,smb\n0,0,0.15,smb\n",
                encoding="utf-8",
            )
            c3, d3 = run_py(SKILLS / "evaluation-reality-check/scripts/slice_error_auditor.py", str(preds))
            self.assertEqual(c3, 0)
            self.assertEqual(d3["status"], "pass")

            # Stage 5: Production ML Handoff
            handoff = tmp / "handoff.json"
            handoff.write_text(json.dumps({
                "model_artifact_sha256": "a" * 64,
                "input_schema": {"account_id": "string", "usage_30d": "float"},
                "output_schema": {"churn_prob": "float"},
                "latency_p99_ms_budget": 45,
                "fallback_baseline": "rule_tenure_threshold_v1",
                "oncall_owner": "ml-platform-oncall",
                "rollback_trigger": "psi > 0.25 or error_rate > 0.01",
            }), encoding="utf-8")
            c4, d4 = run_py(SKILLS / "production-ml-handoff/scripts/handoff_readiness_audit.py", str(handoff))
            self.assertEqual(c4, 0)
            self.assertEqual(d4["status"], "ready_for_handoff")

    def test_07_flat_install_for_single_level_skill_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            target = Path(tmpdir) / "installed_skills"
            code, data = run_py(
                REPO_ROOT / "scripts" / "catalog_cli.py",
                "install", "--target", str(target), "--skill", "leakage-adversary"
            )
            self.assertEqual(code, 0)
            self.assertTrue((target / "leakage-adversary" / "SKILL.md").exists())



    def test_08_multilingual_native_support_en_zh_ja_ko(self) -> None:
        for readme_name in ["README.md", "README.zh-CN.md", "README.ja.md", "README.ko.md"]:
            self.assertTrue((REPO_ROOT / readme_name).exists(), f"Missing {readme_name}")
            self.assertTrue((SKILLS / readme_name).exists(), f"Missing inner {readme_name}")

        catalog = json.loads((REPO_ROOT / "catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(catalog.get("supported_languages"), ["en", "zh-CN", "ja", "ko"])
        self.assertEqual(len(catalog.get("skills", [])), 25)
        for skill_entry in catalog["skills"]:
            self.assertEqual(set(skill_entry["i18n"].keys()), {"en", "zh-CN", "ja", "ko"})

        for lang in ["en", "zh-CN", "ja", "ko"]:
            code, out = run_py(REPO_ROOT / "scripts" / "catalog_cli.py", "list", "--lang", lang)
            self.assertEqual(code, 0, f"Failed for {lang}: {out}")
            self.assertEqual(out["count"], 25)
            self.assertEqual(out["language"], lang)



if __name__ == "__main__":
    unittest.main(verbosity=2)

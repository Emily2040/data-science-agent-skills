#!/usr/bin/env python3
"""Strict portable-skill contract and behavioral smoke tests with no third-party dependencies."""
from __future__ import annotations

import argparse
import json
import re
import struct
import subprocess
import sys
import tempfile
from pathlib import Path


REQUIRED = [
    "SKILL.md",
    "README.md",
    "MANIFEST.json",
    "AGENTS.md",
    "agents/openai.yaml",
    "references/multilingual-guide.md",
    "references/playbook.md",
    "references/acceptance-tests.md",
    "references/provider-interop.md",
    "references/agent-portability.md",
    "references/quality-rubric.md",
    "references/benchmark-plan.md",
    "references/research-grounding.md",
    "references/evidence-map.md",
    "references/infographic-spec.md",
    "tests/test_skill_contract.py",
    "tests/fixtures/clean.md",
    "tests/fixtures/messy.md",
    "tests/fixtures/adversarial.md",
    "assets/hero-shot.png",
    "assets/reddit-infographic.png",
]

README_SECTIONS = [
    "Executive Summary",
    "Research-Informed Design Standard",
    "Problem It Solves",
    "What This Skill Should Do",
    "Required Inputs",
    "Operating Workflow",
    "Expected Outputs",
    "Concrete Use Cases",
    "Red Flags",
    "Agent And Provider Portability",
    "Validation",
]

AGENT_NAMES = ["Codex", "Claude", "Gemini", "Copilot", "Cursor", "Windsurf", "Gravity", "LangGraph", "CrewAI", "AutoGen"]


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path} is not a valid PNG")
    return struct.unpack(">II", data[16:24])


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md missing frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter not closed")
    raw = text[4:end].strip().splitlines()
    values = {}
    for line in raw:
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values


def check_links(root: Path, md_path: Path, markdown: str, file_name: str, errors: list[str]) -> None:
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", markdown):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0].strip()
        if not clean:
            continue
        rel_to_doc = (md_path.parent / clean).resolve()
        rel_to_root = (root / clean).resolve()
        if not rel_to_doc.exists() and not rel_to_root.exists():
            errors.append(f"{file_name} broken link: {target}")


def run_script_smoke_tests(root: Path, errors: list[str]) -> None:
    scripts_dir = root / "scripts"
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        pass_json = tmp / "pass.json"
        pass_json.write_text(json.dumps({"items": [{"id": "c1", "weight": 1.0, "status": "pass"}]}), encoding="utf-8")
        proc = subprocess.run([sys.executable, str(scripts_dir / "checklist_score.py"), str(pass_json), "--strict"], capture_output=True, text=True)
        if proc.returncode != 0:
            errors.append(f"checklist_score.py failed on passing payload: {proc.stderr or proc.stdout}")

        fail_json = tmp / "fail.json"
        fail_json.write_text(json.dumps({"items": [{"id": "c1", "weight": 1.0, "status": "fail"}]}), encoding="utf-8")
        proc_fail = subprocess.run([sys.executable, str(scripts_dir / "checklist_score.py"), str(fail_json)], capture_output=True, text=True)
        if proc_fail.returncode == 0:
            errors.append("checklist_score.py returned 0 on all-failing checklist")

        if (scripts_dir / "profile_table.py").exists():
            csv_path = tmp / "sample.csv"
            csv_path.write_text("model_name,score\nalpha,1.0\nbeta,2.0\ngamma,N/A\n", encoding="utf-8")
            p = subprocess.run([sys.executable, str(scripts_dir / "profile_table.py"), str(csv_path)], capture_output=True, text=True)
            if p.returncode != 0:
                errors.append(f"profile_table.py crashed: {p.stderr}")
            else:
                out = json.loads(p.stdout)
                if out["columns"]["model_name"]["pii_name_hint"] is not False:
                    errors.append("profile_table.py falsely flagged model_name as PII")

        if (scripts_dir / "split_leakage_probe.py").exists():
            t_csv, e_csv = tmp / "train.csv", tmp / "eval.csv"
            t_csv.write_text("id,postal_code,target\n1,94101,0\n2,94102,1\n", encoding="utf-8")
            e_csv.write_text("id,postal_code,target\n3,94103,0\n4,94104,1\n", encoding="utf-8")
            p = subprocess.run([sys.executable, str(scripts_dir / "split_leakage_probe.py"), str(t_csv), str(e_csv), "--key", "id", "--target", "target"], capture_output=True, text=True)
            if p.returncode != 0:
                errors.append(f"split_leakage_probe.py false positive on clean split: {p.stdout}")

        if (scripts_dir / "extract_lineage_tokens.py").exists():
            py_file = tmp / "etl.py"
            py_file.write_text("from pathlib import Path\ndf = pd.read_csv('raw_events.csv')\n", encoding="utf-8")
            p = subprocess.run([sys.executable, str(scripts_dir / "extract_lineage_tokens.py"), str(py_file)], capture_output=True, text=True)
            out = json.loads(p.stdout)
            if "pathlib" in out["tokens"]["sql_from_join"]:
                errors.append("extract_lineage_tokens.py misclassified Python import as SQL table")

        if (scripts_dir / "drift_probe.py").exists():
            b_csv, c_csv = tmp / "base.csv", tmp / "cur.csv"
            b_csv.write_text("x\n-1.0\n1.0\n-1.0\n1.0\n", encoding="utf-8")
            c_csv.write_text("x\n-50.0\n50.0\n-50.0\n50.0\n", encoding="utf-8")
            p = subprocess.run([sys.executable, str(scripts_dir / "drift_probe.py"), str(b_csv), str(c_csv)], capture_output=True, text=True)
            out = json.loads(p.stdout)
            if out["columns"]["x"]["status"] != "investigate":
                errors.append("drift_probe.py missed 50x variance explosion")

        if (scripts_dir / "notebook_repro_audit.py").exists():
            nb_path = tmp / "test.ipynb"
            nb_path.write_text(json.dumps({
                "cells": [
                    {"cell_type": "code", "execution_count": 1, "source": ["import random\n", "random.seed(42)\n"]},
                    {"cell_type": "code", "execution_count": 2, "source": ["x = random.random()\n"]},
                ]
            }), encoding="utf-8")
            p = subprocess.run([sys.executable, str(scripts_dir / "notebook_repro_audit.py"), str(nb_path)], capture_output=True, text=True)
            out = json.loads(p.stdout)
            if out["cell_findings"]:
                errors.append(f"notebook_repro_audit.py false positive on seeded notebook: {out}")

        if (scripts_dir / "compute_budget_estimator.py").exists():
            p = subprocess.run([sys.executable, str(scripts_dir / "compute_budget_estimator.py"), "--hours", "2", "--hourly-rate", "2.5", "--runs", "4", "--failure-rate", "0.2", "--budget", "50"], capture_output=True, text=True)
            if p.returncode != 0:
                errors.append(f"compute_budget_estimator.py failed: {p.stdout}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir", nargs="?", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()
    root = Path(args.skill_dir).resolve()
    errors: list[str] = []

    for rel in REQUIRED:
        if not (root / rel).exists():
            errors.append(f"missing {rel}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")
    manifest = json.loads((root / "MANIFEST.json").read_text(encoding="utf-8"))

    try:
        fm = frontmatter(skill_text)
        if fm.get("name") != root.name:
            errors.append("frontmatter name does not match folder")
        if not re.fullmatch(r"[a-z0-9-]{1,63}", fm.get("name", "")):
            errors.append("frontmatter name is not portable hyphen-case")
        desc = fm.get("description", "")
        if len(desc) < 120 or len(desc) > 360:
            errors.append(f"frontmatter description length ({len(desc)}) must be between 120 and 360 chars")
        if "Trigger for Codex, Claude" in desc or "workflow for score" in desc.lower() or "workflow for force" in desc.lower():
            errors.append("frontmatter description contains ungrammatical or bloated template boilerplate")
        if set(fm) != {"name", "description"}:
            errors.append("frontmatter should contain only name and description")
    except Exception as exc:
        errors.append(str(exc))

    first_lines = "\n".join(readme.splitlines()[:8])
    if "hero-shot.png" not in first_lines or "reddit-infographic.png" not in first_lines:
        errors.append("README must show hero and infographic at the top")
    for section in README_SECTIONS:
        if f"## {section}" not in readme:
            errors.append(f"README missing section: {section}")
    for section in ["Mission", "Operating Rules", "What This Skill Must Do", "Workflow", "Output Contract", "Final Checks"]:
        if f"## {section}" not in skill_text:
            errors.append(f"SKILL.md missing section: {section}")

    if len(skill_text.splitlines()) > 500:
        errors.append("SKILL.md exceeds 500 lines; progressive disclosure failed")

    try:
        hero_size = png_size(root / "assets/hero-shot.png")
        if hero_size != (1600, 900):
            errors.append(f"hero-shot.png wrong size: {hero_size}")
    except ValueError as exc:
        errors.append(str(exc))

    try:
        info_size = png_size(root / "assets/reddit-infographic.png")
        if info_size != (1080, 1350):
            errors.append(f"reddit-infographic.png wrong size: {info_size}")
    except ValueError as exc:
        errors.append(str(exc))

    ml_guide = (root / "references/multilingual-guide.md").read_text(encoding="utf-8")
    for lang_token in ["English", "简体中文", "日本語", "한국어"]:
        if lang_token not in ml_guide or lang_token not in skill_text or lang_token not in readme:
            errors.append(f"missing native multilingual token {lang_token}")
    if set(manifest.get("supported_languages", [])) != {"en", "zh-CN", "ja", "ko"}:
        errors.append("manifest missing supported_languages [en, zh-CN, ja, ko]")
    if manifest.get("name") != root.name:
        errors.append("MANIFEST name does not match folder")
    for agent in AGENT_NAMES:
        joined = "\n".join([
            (root / "references/agent-portability.md").read_text(encoding="utf-8"),
            (root / "README.md").read_text(encoding="utf-8"),
            json.dumps(manifest),
        ])
        if agent not in joined:
            errors.append(f"missing portability mention for {agent}")

    for fixture in ["clean", "messy", "adversarial"]:
        text = (root / "tests" / "fixtures" / f"{fixture}.md").read_text(encoding="utf-8")
        if fixture not in text.lower():
            errors.append(f"{fixture} fixture does not identify itself")
        if "even though unknown" in text.lower() or "even though no " in text.lower():
            errors.append(f"{fixture} fixture contains ungrammatical template phrase")

    for md in root.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        check_links(root, md, text, md.relative_to(root).as_posix(), errors)
        if re.search(r"\b(TODO|REPLACE_ME|FIXME)\b", text):
            errors.append(f"placeholder token in {md.relative_to(root).as_posix()}")
        if re.search(r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*['\"][A-Za-z0-9_\-]{12,}", text):
            errors.append(f"secret-like string in {md.relative_to(root).as_posix()}")

    for py in root.rglob("*.py"):
        source = py.read_text(encoding="utf-8")
        compile(source, str(py), "exec")

    for rel in manifest.get("required_files", []):
        if not (root / rel).exists():
            errors.append(f"manifest required file missing: {rel}")

    run_script_smoke_tests(root, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("world-class-skill-contract-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

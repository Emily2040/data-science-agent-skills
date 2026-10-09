#!/usr/bin/env python3
"""Root CLI to list (in EN/ZH-CN/JA/KO), validate, and flat-install the 25 data science agent skills."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "data-science-agent-skills"
CATALOG_JSON = REPO_ROOT / "catalog.json"


def discover_skills() -> list[Path]:
    return sorted(
        p for p in SKILLS_DIR.iterdir()
        if p.is_dir() and (p / "SKILL.md").exists() and (p / "MANIFEST.json").exists()
    )


def cmd_list(lang: str) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    catalog = json.loads(CATALOG_JSON.read_text(encoding="utf-8"))
    norm_lang = {
        "zh": "zh-CN",
        "cn": "zh-CN",
        "zh-cn": "zh-CN",
        "ja": "ja",
        "jp": "ja",
        "ko": "ko",
        "kr": "ko",
        "en": "en",
    }.get(lang.lower(), "en")
    rows = []
    for item in catalog.get("skills", []):
        loc = item.get("i18n", {}).get(norm_lang, item.get("i18n", {}).get("en", {}))
        rows.append(
            {
                "name": item["name"],
                "language": norm_lang,
                "title": loc.get("title", item["display_name"]),
                "summary": loc.get("short", item["short_description"]),
                "trigger": loc.get("trigger", ""),
                "scripts": [Path(s).name for s in item.get("scripts", [])],
            }
        )
    print(json.dumps({"language": norm_lang, "count": len(rows), "skills": rows}, indent=2, ensure_ascii=False))
    return 0


def _validate_one(skill: Path) -> dict | None:
    validator = skill / "scripts" / "quick_validate_skill.py"
    proc = subprocess.run([sys.executable, str(validator), str(skill), "--strict"], capture_output=True, text=True)
    if proc.returncode != 0:
        return {"skill": skill.name, "output": proc.stdout.strip() or proc.stderr.strip()}
    return None


def cmd_validate() -> int:
    skills = discover_skills()
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(_validate_one, skills))
    failures = [r for r in results if r is not None]
    print(
        json.dumps(
            {
                "total": len(skills),
                "passed": len(skills) - len(failures),
                "failed": len(failures),
                "failures": failures,
            },
            indent=2,
        )
    )
    return 1 if failures else 0


def cmd_install(target: Path, selected: list[str] | None) -> int:
    target.mkdir(parents=True, exist_ok=True)
    skills = discover_skills()
    installed = []
    for skill in skills:
        if selected and skill.name not in selected:
            continue
        dest = target / skill.name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(skill, dest)
        installed.append(skill.name)
    print(json.dumps({"target": str(target.resolve()), "installed_count": len(installed), "installed": installed}, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p_list = sub.add_parser("list", help="List all 25 skills in English, Simplified Chinese, Japanese, or Korean")
    p_list.add_argument("--lang", default="en", help="Language code: en, zh-CN, ja, ko")
    p_val = sub.add_parser("validate", help="Run strict contract and script validation across all 25 skills")
    p_val.add_argument("--strict", action="store_true", help="Strict validation mode (default)")
    p_install = sub.add_parser("install", help="Install flat skill folders into a target skills directory")
    p_install.add_argument("--target", required=True, help="Target directory (e.g. ~/.codex/skills or ~/.claude/skills)")
    p_install.add_argument("--skill", action="append", default=None, help="Specific skill slug(s) to install")
    args = parser.parse_args()

    if args.command == "list":
        return cmd_list(args.lang)
    if args.command == "validate":
        return cmd_validate()
    if args.command == "install":
        return cmd_install(Path(args.target).expanduser(), args.skill)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

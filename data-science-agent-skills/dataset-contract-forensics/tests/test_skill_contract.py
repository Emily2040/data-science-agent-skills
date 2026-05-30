#!/usr/bin/env python3
"""Strict portable-skill contract tests with no third-party dependencies."""
from __future__ import annotations

import argparse
import json
import re
import struct
import sys
from pathlib import Path


REQUIRED = [
    "SKILL.md",
    "README.md",
    "MANIFEST.json",
    "AGENTS.md",
    "agents/openai.yaml",
    "references/playbook.md",
    "references/acceptance-tests.md",
    "references/provider-interop.md",
    "references/agent-portability.md",
    "references/quality-rubric.md",
    "references/benchmark-plan.md",
    "references/research-grounding.md",
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
        raise ValueError(f"{path} is not a PNG")
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


def check_links(root: Path, markdown: str, file_name: str, errors: list[str]) -> None:
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", markdown):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0]
        if clean and not (root / clean).exists():
            errors.append(f"{file_name} broken link: {target}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir", nargs="?", default=".")
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
        if len(fm.get("description", "")) < 140:
            errors.append("frontmatter description too weak for cross-agent triggering")
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

    hero_size = png_size(root / "assets/hero-shot.png")
    info_size = png_size(root / "assets/reddit-infographic.png")
    if hero_size != (1600, 900):
        errors.append(f"hero-shot.png wrong size: {hero_size}")
    if info_size != (1080, 1350):
        errors.append(f"reddit-infographic.png wrong size: {info_size}")

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

    for md in root.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        check_links(root, text, md.relative_to(root).as_posix(), errors)
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

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("world-class-skill-contract-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

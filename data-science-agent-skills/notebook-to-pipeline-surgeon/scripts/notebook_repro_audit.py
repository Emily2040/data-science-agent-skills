#!/usr/bin/env python3
"""Audit a Jupyter notebook (.ipynb) for reproducibility and pipeline-refactoring hazards."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ABS_PATH_RE = re.compile(r"(?:[A-Za-z]:[\\/]|/Users/|/home/|/content/|/mnt/)")
SECRET_RE = re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password)\s*=\s*['\"][^'\"]{8,}['\"]")
RNG_CALL_RE = re.compile(
    r"\b(?:random\.(?:random|randint|choice|choices|shuffle|sample|uniform|gauss)|np\.random\.(?:rand|randn|randint|choice|normal|uniform|permutation)|torch\.rand|tf\.random)\b"
)
SEED_CALL_RE = re.compile(
    r"\b(?:random\.seed|np\.random\.seed|default_rng|torch\.manual_seed|tf\.random\.set_seed|random_state\s*=|seed\s*=)\b"
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebook_path")
    args = parser.parse_args()

    nb = json.loads(Path(args.notebook_path).read_text(encoding="utf-8"))
    execution_counts: list[int] = []
    findings: list[dict[str, object]] = []
    seed_seen_in_notebook = False

    for index, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        if SEED_CALL_RE.search(source):
            seed_seen_in_notebook = True

    for index, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        count = cell.get("execution_count")
        if isinstance(count, int):
            execution_counts.append(count)
        flags = {
            "shell_install": bool(re.search(r"(^|\n)\s*[!%]+\s*(?:pip|conda|uv|poetry)\s+install", source)),
            "absolute_path": bool(ABS_PATH_RE.search(source)),
            "random_without_seed_hint": bool(RNG_CALL_RE.search(source)) and not seed_seen_in_notebook,
            "secret_hint": bool(SECRET_RE.search(source)),
        }
        if any(flags.values()):
            findings.append({"cell": index, "execution_count": count, "flags": [k for k, v in flags.items() if v]})

    out_of_order = execution_counts != sorted(execution_counts) or len(execution_counts) != len(set(execution_counts))
    status = "needs_repro_cleanup" if (out_of_order or findings) else "clean_enough_for_smoke_run"
    print(
        json.dumps(
            {
                "notebook": args.notebook_path,
                "code_cells_executed": len(execution_counts),
                "seed_detected": seed_seen_in_notebook,
                "out_of_order_execution": out_of_order,
                "cell_findings": findings,
                "status": status,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Inventory common data science dependency and artifact surfaces."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DEP_FILES = {"requirements.txt", "pyproject.toml", "environment.yml", "environment.yaml", "renv.lock", "DESCRIPTION"}
MODEL_SUFFIXES = {".pkl", ".joblib", ".onnx", ".pt", ".pth", ".safetensors", ".h5"}
DATA_SUFFIXES = {".csv", ".parquet", ".jsonl", ".xlsx", ".feather"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Inventory DS supply-chain surfaces.")
    parser.add_argument("path")
    args = parser.parse_args()
    root = Path(args.path)
    result = {"dependency_files": [], "notebooks": [], "model_artifacts": [], "data_files": []}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = str(path.relative_to(root))
        if path.name in DEP_FILES:
            result["dependency_files"].append(rel)
        if path.suffix == ".ipynb":
            result["notebooks"].append(rel)
        if path.suffix.lower() in MODEL_SUFFIXES:
            result["model_artifacts"].append(rel)
        if path.suffix.lower() in DATA_SUFFIXES:
            result["data_files"].append(rel)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

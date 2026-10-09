#!/usr/bin/env python3
"""Create a lightweight experiment provenance manifest from local files and git state."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def git_value(args: list[str]) -> tuple[bool, str | None]:
    try:
        proc = subprocess.run(["git", *args], capture_output=True, text=True, check=True)
        return True, proc.stdout.strip()
    except Exception:
        return False, None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifacts", nargs="*", help="Data, config, or model files to hash")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    files = {}
    for raw in args.artifacts:
        path = Path(raw)
        if path.is_file():
            files[str(path)] = {"sha256": sha256_file(path), "bytes": path.stat().st_size}

    git_ok, commit = git_value(["rev-parse", "HEAD"])
    _, branch = git_value(["rev-parse", "--abbrev-ref", "HEAD"])
    status_ok, porcelain = git_value(["status", "--porcelain"])

    record = {
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_available": git_ok and status_ok,
        "git_commit": commit,
        "git_branch": branch,
        "git_dirty": bool(porcelain) if status_ok else None,
        "python": platform.python_version(),
        "platform": platform.platform(),
        "seed": args.seed,
        "notes": args.notes,
        "artifacts": files,
    }
    print(json.dumps(record, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

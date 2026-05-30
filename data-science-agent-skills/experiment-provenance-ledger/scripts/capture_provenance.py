#!/usr/bin/env python3
"""Create a compact provenance ledger entry for an experiment."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_value(args):
    try:
        return subprocess.check_output(["git", *args], stderr=subprocess.DEVNULL, text=True).strip()
    except Exception:
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture a provenance ledger JSON.")
    parser.add_argument("--artifact", action="append", default=[])
    parser.add_argument("--data", action="append", default=[])
    parser.add_argument("--command", default="")
    parser.add_argument("--notes", default="")
    args = parser.parse_args()
    files = []
    for group, paths in [("artifact", args.artifact), ("data", args.data)]:
        for item in paths:
            path = Path(item)
            files.append({"kind": group, "path": str(path), "sha256": sha256(path) if path.is_file() else None})
    ledger = {
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "cwd": os.getcwd(),
        "git_commit": git_value(["rev-parse", "HEAD"]),
        "git_dirty": bool(git_value(["status", "--porcelain"])),
        "command": args.command,
        "files": files,
        "notes": args.notes,
    }
    print(json.dumps(ledger, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

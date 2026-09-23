#!/usr/bin/env python3
"""Fail if docs pages and product-codes.json disagree (no invented or missing codes)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CODES_PATH = ROOT / "product-codes.json"
DOCS = ROOT / "docs"


def names(kind: str) -> set[str]:
    directory = DOCS / kind
    return {path.stem for path in directory.glob("*.md") if path.stem != "index"}


def main() -> int:
    listed = json.loads(CODES_PATH.read_text(encoding="utf-8"))
    failed = False
    for kind in ("findings", "metrics", "gates"):
        expected = set(listed[kind])
        actual = names(kind)
        if expected != actual:
            failed = True
            missing = sorted(expected - actual)
            extra = sorted(actual - expected)
            print(f"{kind}: missing={missing} extra={extra}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# Original implementation: ebikin.
"""Add a YYYY-MM taxonomy tag to canonical FANBOX-migrated Zola posts.

Only files carrying the canonical kinneko.fanbox.cc source footer are eligible.
The script changes the front-matter tags array only and is idempotent.
"""
from __future__ import annotations

import argparse
import ast
import re
from pathlib import Path

DATE_RE = re.compile(r'^date\s*=\s*"(\d{4}-\d{2})-\d{2}(?:[ T][^"]*)?"\s*$', re.MULTILINE)
TAGS_RE = re.compile(r'^(tags\s*=\s*)(\[[^\n]*\])\s*$', re.MULTILINE)
SOURCE_MARKER = "kinneko.fanbox.cc/posts/"


def transformed(text: str, path: Path) -> str | None:
    if SOURCE_MARKER not in text:
        return None
    front, sep, body = text.partition("+++")
    if front:
        raise ValueError(f"{path}: expected opening TOML delimiter")
    if not sep:
        raise ValueError(f"{path}: missing opening TOML delimiter")
    front, sep, body = body.partition("+++")
    if not sep:
        raise ValueError(f"{path}: missing closing TOML delimiter")

    date = DATE_RE.search(front)
    if not date:
        raise ValueError(f"{path}: missing parseable date")
    month = date.group(1)
    tags = TAGS_RE.search(front)
    if not tags:
        raise ValueError(f"{path}: missing one-line tags array")

    try:
        values = ast.literal_eval(tags.group(2))
    except (SyntaxError, ValueError) as exc:
        raise ValueError(f"{path}: invalid tags array") from exc
    if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
        raise ValueError(f"{path}: tags must be a string array")
    if month in values:
        return None

    values.append(month)
    rendered = ", ".join(f'"{value}"' for value in values)
    updated_front = front[:tags.start(2)] + f"[{rendered}]" + front[tags.end(2):]
    return "+++" + updated_front + "+++" + body


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write changes (default is a dry run)")
    parser.add_argument("root", nargs="?", default="content/posts", type=Path)
    args = parser.parse_args()

    changed: list[Path] = []
    for path in sorted(args.root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        updated = transformed(text, path)
        if updated is None:
            continue
        changed.append(path)
        if args.write:
            path.write_text(updated, encoding="utf-8")

    mode = "updated" if args.write else "would_update"
    print(f"{mode}={len(changed)}")
    for path in changed:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

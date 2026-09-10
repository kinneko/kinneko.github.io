#!/usr/bin/env python3
"""Audit FANBOX public inventory against canonical-source footers in Zola posts.

Original implementation by ebikin. Reports only public FANBOX posts whose
canonical URL is absent from content/posts, grouped by publication month.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

CANONICAL_RE = re.compile(r"https://kinneko\.fanbox\.cc/posts/(\d+)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", default="data/fanbox-post-inventory.json")
    parser.add_argument("--content", default="content/posts")
    parser.add_argument("--json-output")
    parser.add_argument("--next-month", action="store_true")
    args = parser.parse_args()

    inventory = json.loads(Path(args.inventory).read_text())["posts"]
    canonical_ids: set[str] = set()
    for path in Path(args.content).rglob("*.md"):
        canonical_ids.update(CANONICAL_RE.findall(path.read_text(errors="replace")))

    missing = [
        post for post in inventory
        if post["visibility"] == "全体公開" and post["id"] not in canonical_ids
    ]
    missing.sort(key=lambda post: (post["publishedDatetime"], int(post["id"])))
    by_month = Counter(post["publishedDatetime"][:7] for post in missing)
    report = {
        "inventory_public": sum(post["visibility"] == "全体公開" for post in inventory),
        "canonical_migrated": len(canonical_ids),
        "missing_public": len(missing),
        "missing_by_month": dict(sorted(by_month.items())),
        "missing": missing,
    }
    if args.json_output:
        path = Path(args.json_output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    if args.next_month:
        month = min(by_month) if by_month else ""
        print(month)
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

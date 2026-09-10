#!/usr/bin/env python3
"""Refresh FANBOX post inventory from the canonical creator pagination API.

Original implementation by ebikin. The JSON inventory is the auditable source
for FANBOX URL, title, publication timestamp, and access attribute checks.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen

API_ROOT = "https://api.fanbox.cc"
CREATOR_ID = "kinneko"
HEADERS = {
    "Origin": f"https://{CREATOR_ID}.fanbox.cc",
    "Referer": f"https://{CREATOR_ID}.fanbox.cc/",
    "User-Agent": "Mozilla/5.0",
}


def get_json(url: str) -> dict:
    request = Request(url, headers=HEADERS)
    with urlopen(request, timeout=90) as response:
        return json.load(response)


def normalized_post(post: dict) -> dict:
    fee = int(post.get("feeRequired") or 0)
    restricted = bool(post.get("isRestricted"))
    return {
        "id": str(post["id"]),
        "url": f"https://{CREATOR_ID}.fanbox.cc/posts/{post['id']}",
        "title": post["title"],
        "publishedDatetime": post["publishedDatetime"],
        "feeRequired": fee,
        "isRestricted": restricted,
        "visibility": "全体公開" if not restricted and fee == 0 else f"¥{fee}",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/fanbox-post-inventory.json")
    args = parser.parse_args()

    first = get_json(f"{API_ROOT}/post.paginateCreator?creatorId={CREATOR_ID}&sort=newest")
    page_urls = first["body"]["pageUrls"]
    posts: list[dict] = []
    for url in page_urls:
        posts.extend(normalized_post(post) for post in get_json(url)["body"]["posts"])
    posts.sort(key=lambda post: (post["publishedDatetime"], int(post["id"])))
    ids = [post["id"] for post in posts]
    if len(ids) != len(set(ids)):
        raise RuntimeError("FANBOX pagination returned duplicate post IDs")

    output = {
        "schema_version": 1,
        "generated_by": "ebikin original FANBOX inventory collector",
        "source": f"{API_ROOT}/post.paginateCreator?creatorId={CREATOR_ID}&sort=newest",
        "latest_publishedDatetime": posts[-1]["publishedDatetime"] if posts else None,
        "posts": posts,
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    public = sum(post["visibility"] == "全体公開" for post in posts)
    print(f"inventory: total={len(posts)} public={public} restricted={len(posts)-public} output={path}")


if __name__ == "__main__":
    main()

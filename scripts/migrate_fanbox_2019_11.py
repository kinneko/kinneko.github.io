#!/usr/bin/env python3
"""Add the verified public FANBOX post 670427 without touching origin-owned paths.

The local macOS WebKit reader is the public-access and article-block authority.
This one-post migration intentionally gives the retained body asset a post-ID
name: an identical legacy filename already exists on origin/main and is left
untouched under the published-content preservation rule.
"""
from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
READER = "/Users/kinneko/work/knowledge-wiki/fanbox_public_reader"
POST_ID = "670427"
URL = f"https://kinneko.fanbox.cc/posts/{POST_ID}"
DATE = "2019-11-25"
ASSET_DIR = ROOT / "static" / DATE
ARTICLE = ROOT / "content" / "posts" / "2019" / "11" / f"{DATE}.md"


def download(source: str, destination: Path) -> None:
    if destination.exists():
        raise RuntimeError(f"refusing to replace an existing asset: {destination}")
    part = Path(str(destination) + ".part")
    try:
        request = Request(source, headers={"User-Agent": "Mozilla/5.0", "Referer": URL})
        with urlopen(request, timeout=90) as response, part.open("wb") as out:
            if response.status != 200:
                raise RuntimeError(f"{source}: HTTP {response.status}")
            while chunk := response.read(1024 * 1024):
                out.write(chunk)
        os.replace(part, destination)
    except Exception:
        part.unlink(missing_ok=True)
        raise


def main() -> None:
    if ARTICLE.exists():
        raise RuntimeError(f"refusing to replace an existing article: {ARTICLE}")
    raw = subprocess.check_output([READER, URL], text=True, timeout=120)
    post = json.loads(raw)
    if "全体公開" not in post.get("text", ""):
        raise RuntimeError("reader did not verify 全体公開")
    blocks = post.get("article_blocks")
    if not blocks:
        raise RuntimeError("reader returned no article_blocks")
    title = post["title"].removesuffix("｜kinneko｜pixivFANBOX")
    if title != "やっぱりアレは長くないといけない":
        raise RuntimeError(f"unexpected title: {title}")
    head = next((item for item in post.get("head_images", []) if item.get("name") in {"og:image", "twitter:image"}), None)
    if not head:
        raise RuntimeError("no verified og:image or twitter:image")

    # The source begins with an explicit sponsorship callout. It is excluded;
    # the remaining ordered text and the single product photo are retained.
    retained = []
    for block in blocks:
        if block["kind"] == "text" and "スポンサードで公開されています" in block.get("text", ""):
            continue
        retained.append(block)

    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    cover = f"{POST_ID}-cover{Path(urlparse(head['url']).path).suffix.lower() or '.jpeg'}"
    inline = f"{POST_ID}-inline-01.png"
    download(head["url"], ASSET_DIR / cover)
    image_blocks = [block for block in retained if block["kind"] == "image"]
    if len(image_blocks) != 1:
        raise RuntimeError(f"expected one retained body image, got {len(image_blocks)}")
    download(image_blocks[0]["url"], ASSET_DIR / inline)

    body: list[str] = []
    for block in retained:
        if block["kind"] == "image":
            body += [f"![](/{DATE}/{inline})", ""]
            continue
        text = block.get("text", "").strip()
        if text:
            body += ["　" + text.lstrip("　"), ""]
    while body and not body[-1]:
        body.pop()
    content = "\n".join([
        "+++",
        'date = "2019-11-25 08:29:00"',
        "draft = false",
        f'title = "{title}"',
        'description = "長いSIMピンを用意して、深いSIMカードスロットを開けられるか試す。"',
        "",
        "[taxonomies]",
        'tags = ["SIM", "スマートフォン", "2019-11"]',
        "",
        "[extra]",
        f'image = "{DATE}/{cover}"',
        "+++",
        "",
        *body,
        "",
        "---",
        "> オリジナル投稿：<br>",
        f"> {title}｜kinneko｜pixivFANBOX<br>",
        f"> <{URL}>",
        "",
    ])
    ARTICLE.write_text(content, encoding="utf-8")
    print(json.dumps({"article": str(ARTICLE.relative_to(ROOT)), "assets": [str((ASSET_DIR / cover).relative_to(ROOT)), str((ASSET_DIR / inline).relative_to(ROOT))]}, ensure_ascii=False))


if __name__ == "__main__":
    main()

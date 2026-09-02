# fanbox-zola

公開URLは https://kinneko.github.io/ です。

## FANBOX migration provenance

### 2026-08 public-post backfill

- **Canonical sources / copyright:** [kinneko on pixivFANBOX](https://kinneko.fanbox.cc/), authored and copyright-held by kinneko. This repository is an authorized static mirror of the author's own public posts; canonical-source links remain in every migrated article.
- **Source scope:** public-only posts. Restricted/supporter-only posts were not copied.
- **Reader / source data:** `fanbox_public_reader` captured public rendered article blocks into `/Users/kinneko/work/fanbox-zola-local-test/aug-2026-migration-source/`. The reader's `article_blocks` sequence is the body-order source; `head_images` provides the title image.
- **Asset source:** title and body media are downloaded only from FANBOX's public image endpoints (`pixiv.pximg.net` and `downloads.fanbox.cc`) associated with each canonical post. Donation/support-callout-adjacent images are intentionally excluded.
- **Changed repository paths:**
  - `content/posts/2026/08/2026-08-18.md`
  - `content/posts/2026/08/2026-08-19.md`
  - `content/posts/2026/08/2026-08-25.md` through `2026-08-28.md`
  - `content/posts/2026/08/2026-08-31.md`
  - matching title/body assets under `static/2026-08-*/`
- **Transformation:** original text, body-media order, published timestamp, canonical-source footer, subject tags, and required `2026-08` tag were retained. The migration generator is ebikin original: `/Users/kinneko/work/fanbox-zola-local-test/migrate_august_2026.py`.

| Published (JST) | Canonical FANBOX post |
| --- | --- |
| 2026-08-18 | https://kinneko.fanbox.cc/posts/12423033 |
| 2026-08-19 | https://kinneko.fanbox.cc/posts/12423907 |
| 2026-08-25 | https://kinneko.fanbox.cc/posts/12476142 |
| 2026-08-26 | https://kinneko.fanbox.cc/posts/12477071 |
| 2026-08-27 | https://kinneko.fanbox.cc/posts/12478614 |
| 2026-08-28 | https://kinneko.fanbox.cc/posts/12486092 |
| 2026-08-31 | https://kinneko.fanbox.cc/posts/12488300 |

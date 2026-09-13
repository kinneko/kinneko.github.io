# fanbox-zola

公開URLは https://kinneko.github.io/ です。

## FANBOX migration provenance

### 2018-04 public-post backfill

- **Canonical sources / copyright:** [kinneko on pixivFANBOX](https://kinneko.fanbox.cc/), authored and copyright-held by kinneko. This repository is an authorized static mirror of the author's own public posts; canonical-source links remain in every migrated article.
- **Source scope:** the canonical inventory identifies two `全体公開` posts in April 2018; neither supporter-only nor private content was copied.
- **Reader / source data:** `fanbox_public_reader` captured verified public rendered source data in `/Users/kinneko/work/fanbox-zola-local-test/apr-2018-migration-source/`. Its `article_blocks` lists no retained body-media blocks for either post. Post `11756` has only the creator-cover `og:image`, so no substitute title image was used; post `13939` retains its verified post-specific `og:image` under `static/2018-04-27-13939/`.
- **Transformation:** original displayed text and publication timestamps were retained; donation/support-callout text was excluded. The canonical footer, specific subject tags, and exactly one `2018-04` tag accompany each article.

| Published (JST) | Canonical FANBOX post |
| --- | --- |
| 2018-04-27 | https://kinneko.fanbox.cc/posts/11756 |
| 2018-04-27 | https://kinneko.fanbox.cc/posts/13939 |

### 2019-11 public-post backfill

- **Canonical sources / copyright:** [kinneko on pixivFANBOX](https://kinneko.fanbox.cc/), authored and copyright-held by kinneko. This repository is an authorized static mirror of the author's public posts; the migrated article preserves its canonical-source link.
- **Source scope:** the auditable canonical inventory identifies two `全体公開` posts not represented by canonical footers in November 2019. Post `644361` collides with the human-owned origin/main article `content/posts/2019/11/2019-11-13.md`; it was not modified. The one otherwise-absent public post, `670427`, was copied. No restricted or supporter-only content was copied.
- **Reader / source data:** the local macOS WebKit `fanbox_public_reader` verified `全体公開` on the canonical URL and supplied ordered `article_blocks`; verified `og:image` supplied the title image. The leading sponsorship callout was excluded. The retained lone body image is 1372×772 (not the 1200×250 supporter-roster banner) and is reproduced in its source-block position.
- **Asset provenance / reuse:** `static/2019-11-25/XfeePpV8QmcOM7scAo7isGzq.png` already existed on origin/main and is byte-identical to the public source body image. It was left untouched; the migration adds a separately named downloaded copy, `670427-inline-01.png`, plus the verified title image. Downloads use `.part` files and atomic rename in `scripts/migrate_fanbox_2019_11.py`.
- **Transformation:** the original displayed body text and timestamp, local title image, specific subject tags, exactly one `2019-11` tag, and canonical FANBOX footer were retained.

| Published (JST) | Canonical FANBOX post |
| --- | --- |
| 2019-11-25 | https://kinneko.fanbox.cc/posts/670427 |

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

### 2025-01 public-post backfill

- **Canonical sources / copyright:** [kinneko on pixivFANBOX](https://kinneko.fanbox.cc/), authored and copyright-held by kinneko. This repository is an authorized static mirror of the author's own public posts; each migrated article retains its canonical-source URL.
- **Source scope:** canonical FANBOX listing pagination found 19 January 2025 posts: 13 explicitly `全体公開` posts were copied; 6 `¥100` supporter-only posts were not copied.
- **Reader / source data:** `fanbox_public_reader` captured the verified public rendered article blocks in `/Users/kinneko/work/fanbox-zola-local-test/jan-2025-migration-source/`. `article_blocks` is the body-order source and `head_images` supplies each title image.
- **Asset source / reuse:** title and body media come only from FANBOX public image endpoints associated with each canonical post. Donation/support-callout text and adjacent media are excluded.
- **Changed repository paths:** `content/posts/2025/01/_index.md`, the 13 dated article files in `content/posts/2025/01/`, and their corresponding cover/body assets under `static/2025-01-*/`.
- **Transformation:** original text, displayed body-media order, timestamp, source footer, subject tags, and exactly one required `2025-01` tag were retained. The migration generator is ebikin original/adapted: `/Users/kinneko/work/fanbox-zola-local-test/migrate_january_2025.py`.

| Published (JST) | Canonical FANBOX post |
| --- | --- |
| 2025-01-06 | https://kinneko.fanbox.cc/posts/9126929 |
| 2025-01-07 | https://kinneko.fanbox.cc/posts/9156661 |
| 2025-01-08 | https://kinneko.fanbox.cc/posts/9156766 |
| 2025-01-09 | https://kinneko.fanbox.cc/posts/9156974 |
| 2025-01-10 | https://kinneko.fanbox.cc/posts/9163056 |
| 2025-01-14 | https://kinneko.fanbox.cc/posts/9195382 |
| 2025-01-15 | https://kinneko.fanbox.cc/posts/9209714 |
| 2025-01-16 | https://kinneko.fanbox.cc/posts/9173767 |
| 2025-01-21 | https://kinneko.fanbox.cc/posts/9194255 |
| 2025-01-23 | https://kinneko.fanbox.cc/posts/9245309 |
| 2025-01-27 | https://kinneko.fanbox.cc/posts/9203854 |
| 2025-01-29 | https://kinneko.fanbox.cc/posts/9253238 |
| 2025-01-30 | https://kinneko.fanbox.cc/posts/9256984 |

| Published (JST) | Canonical FANBOX post |
| --- | --- |
| 2026-08-18 | https://kinneko.fanbox.cc/posts/12423033 |
| 2026-08-19 | https://kinneko.fanbox.cc/posts/12423907 |
| 2026-08-25 | https://kinneko.fanbox.cc/posts/12476142 |
| 2026-08-26 | https://kinneko.fanbox.cc/posts/12477071 |
| 2026-08-27 | https://kinneko.fanbox.cc/posts/12478614 |
| 2026-08-28 | https://kinneko.fanbox.cc/posts/12486092 |
| 2026-08-31 | https://kinneko.fanbox.cc/posts/12488300 |

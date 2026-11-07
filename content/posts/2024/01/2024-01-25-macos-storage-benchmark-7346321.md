+++
date = "2024-01-25T08:00:00"
draft = false
title = "macOSのストレージベンチ"
description = "ディスクのパフォーマンスをmacOSで測定するという習慣はないので、そういうツールは入れていなかった。"

[taxonomies]
tags = ["macOS", "ストレージ", "2024-01"]

[extra]
image = "/2024-01-25/7346321-title.jpeg"
+++

　ディスクのパフォーマンスをmacOSで測定するという習慣はないので、そういうツールは入れていなかった。

　CrystalDiskMarkと同じUIのAmorphousDiskMarkというのがあるとのことで入れてみる。

　sharewareというのは久しぶりに見る。でも、ドネーションについては、このページには特に書かれていない。

> AmorphousDiskMark for macOS - measures storage read/write performance<br>
> <https://www.katsurashareware.com/amorphousdiskmark/>

![](/2024-01-25/7346321-01.png)

　あぁ、AppStoreでしか配布してないわ...

　このMBPはApp Store Freeで生活することにしているので、これは入れられないわ。面倒な...

　しょうがないので、仕事用のIntel MBPを出してくる。App Storeを開いてインストールする。

![](/2024-01-25/7346321-02.png)

　起動するとこんな画面。テスト回数、サイズ、ストレージと速度単位を選んで、Allボタンを押すと実行される。

![](/2024-01-25/7346321-03.png)

　テスト項目は、SEQ1M QD8, SEC1M QD1, RND4K QD64, RND4K QD1の４つ。

　SEQはシーケンシャルアクセス、RNDはランダムアクセス、その後のはサイズ、DQは同時実行数。

　MBP内蔵SSDだとこんな結果になった。

![](/2024-01-25/7346321-04.png)

　これで、RHDのテストをやってみる予定。

---
> オリジナル投稿：<br>
> macOSのストレージベンチ｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/7346321>

+++
date = "2024-03-01 08:00:00"
draft = false
title = "７年落ちPCのRAMを安く増設したのだけど..."
description = "さっそく取り付けてメモリテストしてみる。lenovoなので、システム組み込みの診断プログラムが内蔵されている。テストはだいじね。"

[taxonomies]
tags = ["PC", "メモリ", "2024-03"]

[extra]
image = "2024-03-01/7529546-cover.jpeg"
+++


　さっそく取り付けてメモリテストしてみる。lenovoなので、システム組み込みの診断プログラムが内蔵されている。テストはだいじね。

　F10押しながら電源を入れてDiagnosticsを起動して、メモリのメニューを選ぶ。せっかくなので、メモリ拡張テストを実行する。

![](/2024-03-01/7529546-01.png)

　テスト内容は以下。Bit fade testだけはデフォルトでチェックが入ってなかった。たぶん、時間かかるからかな。全部チェックして実行する。テストは13種類。

```text
    Advanced integrity test
    Address test
    Bit high test
    Bit low test
    Walking ones right test
    Walking ones left test
    Modulo-20 test
    Moving inversions-8bit test
    Moving inversions-32bit test
    Random pattern test
    Random number sequence test
    Block move test
    Bit fade test (~180 min)
```

![](/2024-03-01/7529546-02.png)

　開始された。

![](/2024-03-01/7529546-03.png)

　あ...

![](/2024-03-01/7529546-04.png)

　通ってるテストもあるのだなぁ。

```text
    Advanced integrity test: FAILED
    Address test: FAILED
    Bit high test: FAILED
    Bit low test: FAILED
    Walking ones right test: PASSED
    Walking ones left test: PASSED
    Modulo-20 test: FAILED
    Moving inversions-8bit test: FAILED
    Moving inversions-32bit test: PASSED
    Random pattern test: FAILED
    Random number sequence test: PASSED
    Block move test
    Bit fade test (~180 min)
```

![](/2024-03-01/7529546-05.png)

　Advanced integrity testやAddress testなどの基本的なテストに失敗しているので、メモリが不安定であるか、故障している可能性が高い。

　Bit fade testは長そうなので処理を中断して、一本づつやるか...

![](/2024-03-01/7529546-06.png)

　中断した。

![](/2024-03-01/7529546-07.png)

　メモリのパラメータが書き込まれているSPD(Serial Presence Detect)の読み取りは、メーカー名とかは拾えていないけど、一応問題ない感じ。

![](/2024-03-01/7529546-08.png)

　起動すると普通に認識はしているけど、これは、このまま運用すると超ヤバいやつやね...

```text
kinneko@aosp:~$ free
               total        used        free      shared  buff/cache   available
Mem:        32796832      343044    32065248        1512      388540    32059240
Swap:        4194300           0     4194300
```

　一本目。Bit fade testはパスしてテスト。

![](/2024-03-01/7529546-09.png)

　ダメですね...

![](/2024-03-01/7529546-10.png)

　念の為、スロットを移動してもう一度。

![](/2024-03-01/7529546-11.png)

　結果は同じですね。

![](/2024-03-01/7529546-12.png)

　二本目は通るね。

![](/2024-03-01/7529546-13.png)

　一応、Bit fade test以外はテストしておく。問題なさそうね。

![](/2024-03-01/7529546-14.png)

![](/2024-03-01/7529546-15.png)

　ダメな一本は10日保証があるのと、同じメモリがあと二本あるのを確認して買ってきているので、交換してくるしかないかな... ただ、普段いかないハードオフでお店が遠いのよねぇ...

　交換したやつがまたダメだったらつらいから、PC持ち込みでチェックしてから交換してくるかな...

　というわけで、ハードオフの店頭で場所と電源を貸してもらって、テストをした上で交換してきた。

![](/2024-03-01/7529546-16.png)

　なんか、ほんとにいろいろ遠回りになってるよ...

---
> オリジナル投稿：<br>
> ７年落ちPCのRAMを安く増設したのだけど...｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/7529546>

+++
date = "2022-05-18T08:00:00"
draft = false
title = "Digisparkに書けない -1-"
description = "Digisparkへの書き込み時に起きるMicronucleusのエラーを調べ、ブートローダーを確認する。"

[taxonomies]
tags = ["Digispark", "Arduino", "Micronucleus", "2022-05"]

[extra]
image = "/2022-05-18/3736434-title.jpeg"
+++


　スリープレスドングルをまだほしい人がいるということで、マイコンのリハビリを兼ねて作ってみることにする。

　前にやったときには、M1で書き込むとブートローダーが死ぬ症状に見舞われて20個以上のDigisparkを無駄にしたのがショックで、もうDigisparkはさわるまいと思ったのだった。

> M1環境でArduino IDEを入れてみる -3- (Digispark 1)<br>
> <https://kinneko.fanbox.cc/posts/2079538>

> M1環境でArduino IDEを入れてみる -4- (Digispark 2)<br>
> <https://kinneko.fanbox.cc/posts/2080481>

　ひさしぶりにDigisparkを買おうと思ったら、Aliexpressではえらい高値がついていた。昔の三倍くらいかな。おまけに、まとめて買ったら無料だった送料もしっかり徴収されるようになっている。

　これって、いままでのコストじゃ到底作れないじゃん。というわけで、２個セットをやめて１個にすることにした。

　どんなものが来るのかわからないリスクなんかを考えると、shigezoneAkibaで買うのと変わらないということで、今回はそちらで手配した。

　そういうわけで、前のIntel Macを取り出してきて書き込み作業をしている。書き込むのはスリープレスドングル用の小さいスケッチ。Arduino IDEは1.8.5のままキープしている環境。

　だが、書けない。どういうこと？

![](/2022-05-18/3736434-01.png)

```text
次のフォルダのライブラリDigisparkMouseを使用中：/Users/kinneko 1/Library/Arduino15/packages/digistump/hardware/avr/1.6.7/libraries/DigisparkMouse (legacy)
最大6012バイトのフラッシュメモリのうち、スケッチが3098バイト（51%）を使っています。
グローバル変数は93バイトのRAMを使用しています。
/Users/kinneko 1/Library/Arduino15/packages/digistump/tools/micronucleus/2.0a4/launcher -cdigispark --timeout 60 -Uflash:w:/var/folders/5g/qbmy93zn3cx5r15pkc6tyxsc0000gr/T/arduino_build_670430/digispark_sleepless.ino.hex:i
Running Digispark Uploader...
Plug in device now... (will timeout in 60 seconds)
> Please plug in the device ...
> Press CTRL+C to terminate the program.
> Device is found!
connecting: 16% complete
connecting: 22% complete
connecting: 28% complete
connecting: 33% complete
> Device has firmware version 1.6
> Available space for user applications: 6012 bytes
> Suggested sleep time between sending pages: 8ms
> Whole page count: 94  page size: 64
> Erase function sleep duration: 752ms
parsing: 50% complete
> Erasing the memory ...
erasing: 55% complete
erasing: 60% complete
erasing: 65% complete
> Starting to upload ...
writing: 70% complete
writing: 75% complete
writing: 80% complete
> Starting the user app ...
>> Run error -1 has occured ...
>> Please unplug the device and restart the program.
```

　手元にある正常なやつはちゃんと書ける。

![](/2022-05-18/3736434-02.png)

```text
Running Digispark Uploader...
Plug in device now... (will timeout in 60 seconds)
> Please plug in the device ...
> Press CTRL+C to terminate the program.
> Device is found!
connecting: 16% complete
connecting: 22% complete
connecting: 28% complete
connecting: 33% complete
> Device has firmware version 2.5
> Device signature: 0x1e930b
> Available space for user applications: 6650 bytes
> Suggested sleep time between sending pages: 7ms
> Whole page count: 104  page size: 64
> Erase function sleep duration: 728ms
parsing: 50% complete
> Erasing the memory ...
erasing: 55% complete
erasing: 60% complete
erasing: 65% complete
> Starting to upload ...
writing: 70% complete
writing: 75% complete
writing: 80% complete
> Starting the user app ...
running: 100% complete
>> Micronucleus done. Thank you!
```

　違いは、Digisparkに書き込まれたMicronucleusのバージョンだけかな？

　どうすべ。

　とりあえず、前に何をしたのか復習する。すっかり忘れてるしw

> Digisparkのプリインブートローダーをアップデートする -1-<br>
> <https://kinneko.fanbox.cc/posts/1121221>

> Digisparkのプリインブートローダーをアップデートする -2-<br>
> <https://kinneko.fanbox.cc/posts/1121444>

　ファームは、このあたりにビルドしたものがある。

> <https://github.com/ArminJo/micronucleus-firmware/tree/master/firmware/releases>

　本家はこっちかな。

> micronucleus/micronucleus: ATTiny usb bootloader with a strong emphasis on bootloader compactness.<br>
> <https://github.com/micronucleus/micronucleus>

　hexファームウエアは同じっぽい。

> micronucleus/firmware/releases at master · micronucleus/micronucleus<br>
> <https://github.com/micronucleus/micronucleus/tree/master/firmware/releases>

```text
$ wget https://raw.githubusercontent.com/ArminJo/micronucleus-firmware/master/firmware/releases/t85_agressive.hex
$ curl -O https://raw.githubusercontent.com/ArminJo/micronucleus-firmware/master/firmware/releases/t85_agressive.hex
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
Dload  Upload   Total   Spent    Left  Speed
100  3788  100  3788    0     0  10519      0 --:--:-- --:--:-- --:--:-- 10493
$ ls -la
total 8
drwxr-xr-x   2 kinneko1  staff    102  4 25 14:11 .
drwx------+ 95 kinneko1  staff  58786  4 25 14:10 ..
-rw-r--r--   1 kinneko1  staff   3788  4 25 14:11 t85_agressive.hex
$ file t85_agressive.hex
t85_agressive.hex: ASCII text
```

　本家には、ツールのバイナリは置いていない。

　書き込みツールは"micronucleus-2.0a4-osx.tar.gz"で、前から変わっていないようだ。あいかわらず、M1対応はしていないのね。する見込みもないか。

> <https://github.com/digistump/DigistumpArduino/tree/master/tools>

　Arduino IDEでは、ツールは、このへんにダウンロードされているはず。

`/Users/[ユーザー名]/Library/Arduino15/packages/digistump`

　落とし直したブートローダーを描いてみる。

```text
$ ./micronucleus --run upgrade-t85_aggressive.hex
$ ./micronucleus -run t85_agressive.hex
> Please plug in the device ...
> Press CTRL+C to terminate the program.
> Device is found!
connecting: 40% complete
> Device has firmware version 1.6
> Available space for user applications: 6012 bytes
> Suggested sleep time between sending pages: 8ms
> Whole page count: 94  page size: 64
> Erase function sleep duration: 752ms
parsing: 60% complete
> Program file is 2134 bytes too big for the bootloader!
```

　あ、書けない。死んだかも...

```text
$ ./micronucleus -run
> Please plug in the device ...
> Press CTRL+C to terminate the program.
> Device is found!
connecting: 40% complete
> Device has firmware version 1.6
> Available space for user applications: 6012 bytes
> Suggested sleep time between sending pages: 8ms
> Whole page count: 94  page size: 64
> Erase function sleep duration: 752ms
parsing: 40% complete
> Error opening -run: No such file or directory
> Error loading or parsing hex file.
```

　死んでなかったわ。よかった。

　しかし、一歩も進んでいない。

---
> オリジナル投稿：<br>
> Digisparkに書けない -1-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/3736434>

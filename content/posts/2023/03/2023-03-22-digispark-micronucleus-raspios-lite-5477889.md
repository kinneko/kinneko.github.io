+++
date = "2023-03-22 08:00:00"
draft = false
title = "Digispark開発環境再び - RaspiOS Liteでmicronucleus書き込み"
description = "NT富山に持っていったスリープレスドングルの在庫がどうにも見当たらない。"

[taxonomies]
tags = ["Digispark", "Raspberry Pi", "Arduino", "2023-03"]

[extra]
image = "2023-03-22/5477889-title.jpeg"
+++

　NT富山に持っていったスリープレスドングルの在庫がどうにも見当たらない。

　このまえ、竹田さんから注文もらったときには、手渡しだったので、さくっと１つ作って渡したのだけど、BOOTHで新しい注文が来てしまったので、なかなかそういうわけにもいかなくなった。(3/12)

> Digispark開発環境再び - RaspiOS LiteでArduino CLI｜kinneko｜pixivFANBOX<br>
> <https://www.fanbox.cc/@kinneko/posts/5232973>

　今回から、動作確認の待ち時間が面倒になったので、起動時にはLEDを3回点滅させることにした。

　いま手元にあるロットは、部品が高騰していた頃に、Aliexpressで頼むのとたいしてかわらないということで、国内のShigezoneから購入したもの。LEDは緑赤で、どちらも輝度が低いもの。基板厚が1.9mmなので少し薄いため、USBコネクタに差し込んだときの嵌合が甘く、PETテープで2.2mmまで厚くしてある。

　また、出荷時に書き込まれたブートローダーであるmicronucleusが1.6であるので、起動に６秒弱かかるのがよくない。BOOTHで頒布しているバージョンは、micronucleus 2.6(ArminJo版) を使用して、起動を2秒弱に短縮している。

　というわけで、micronucleusを書き込む環境を作る必要が出てきた。

　micronucleusの書き込みは、大量のDigisparkをゴミにしてしまったことがあるので、トラウマでやる気がしない。しかし、やっておかないといけないよなぁ...

　前に手順は確立してあるのだけど、その環境を削除してしまっているので、再構築する。

　前にやった記録は長すぎて、自分でも再履修するのがめんどくさい。新しい環境での動作確認を兼ねて再履修。再履修記事なので、内容はほとんどないです。

> Digisparkの起動時間を短縮する -1-｜kinneko｜pixivFANBOX<br>
> <https://www.fanbox.cc/@kinneko/posts/3947194>

> Digisparkの起動時間を短縮する -2-｜kinneko｜pixivFANBOX<br>
> <https://www.fanbox.cc/@kinneko/posts/3947823>

> Digisparkの起動時間を短縮する -3-｜kinneko｜pixivFANBOX<br>
> <https://www.fanbox.cc/@kinneko/posts/3951023>

> Digisparkの起動時間を短縮する -4-｜kinneko｜pixivFANBOX<br>
> <https://www.fanbox.cc/@kinneko/posts/3951115>

> Digisparkの起動時間を短縮する -5-｜kinneko｜pixivFANBOX<br>
> <https://www.fanbox.cc/@kinneko/posts/3959961>

> Digisparkの起動時間を短縮する -6-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/3964117>

> Digisparkの起動時間を短縮する -7-｜kinneko｜pixivFANBOX<br>
> <https://www.fanbox.cc/@kinneko/posts/3980193>

> Digisparkの起動時間を短縮する -8-｜kinneko｜pixivFANBOX<br>
> <https://www.fanbox.cc/@kinneko/posts/3980281>

　ブートローダー書き込み用のmicronucleusコマンドは、ArduinoIDEにDigisparkのライブラリ追加したときにインストールされている。

　RaspiOS上では、"/home/[ユーザー名]/.arduino15/packages/digistump"になっている。micronucleusコマンドの実体は、"/home/pi/.arduino15/packages/digistump/tools/micronucleus/2.6/micronucleus"になる。

　まずは、micronucleusコマンドのバージョンを調べる。path情報からは2.6だというのはわかるのだけど、前にやったときの経験からは実行するまでわからない。

```text
pi@pi:~ $ ./.arduino15/packages/digistump/tools/micronucleus/2.6/micronucleus
micronucleus-cli version: 2.5 from Nov  4 2021
Neither filename nor --erase-only nor --info given!
usage: micronucleus [--help] [--run] [--dump-progress] [--fast-mode] [--type intel-hex|raw] [--timeout integer] [--no-ansi] (--erase-only | --info | filename)
```

　相変わらず、パス名には26とあるのに、micronucleusコマンドの実体はv2.5になっている。

　書き込むmicronucleusのビルド済みのhexには２種類あって、ISPで普通に書き込むようなものと、書かれているものを削除してから書き込みするセルフアップグレードルーチンのついたものがある。セルフアップグレードルーチンのついたものは、配布元のupgradesディレクトリに入っている。

　ただ、これを使って失敗すると、ブートローダーをセルフ削除してから書き込むため、前の時のように途中で失敗したりすると完全にレンガになってしまってハイボルテージプログラマでブートローダーを上書きしないと直せなくなってしまう。

　ArminJo版のセルフアップグレードルーチンのついたブートローダー、"upgrade-t85_entry_on_powerOn_activePullup_fastExit.hex"をダウンロードする。

```text
pi@pi:~ $ curl -OL https://raw.githubusercontent.com/ArminJo/micronucleus-firmware/master/firmware/upgrades/upgrade-t85_entry_on_powerOn_activePullup_fastExit.hex
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
Dload  Upload   Total   Spent    Left  Speed
100  6276  100  6276    0     0  16962      0 --:--:-- --:--:-- --:--:-- 17008
```

　書き込んでみる。成功した。

```text
pi@pi:~ $ ./.arduino15/packages/digistump/tools/micronucleus/2.6/micronucleus --run upgrade-t85_entry_on_powerOn_activePullup_fastExit.hex
> Please plug in the device ...
> Device is found!
connecting: 33% complete
> Device has firmware version 1.6
> Available space for user applications: 6012 bytes
> Suggested sleep time between sending pages: 8ms
> Whole page count: 94  page size: 64
> Erase function sleep duration: 752ms
parsing: 50% complete
> Erasing the memory ...
erasing: 66% complete
> Starting to upload ...
writing: 83% complete
> Starting the user app ...
running: 100% complete
>> Micronucleus done. Thank you!
```

　書き込み後は、LEDが素早く２回チカチカするのを繰り返している。この時には、メモリマッピングが変わっているので、前に書き込まれていたAruduinoのスケッチは消えてしまっている。

　書き込みされたバージョンを確認する。micronucleusを不正なオプションを渡して起動すると、バージョンの確認ができる。"Device has firmware version 2.6"とあるので、書き込みには成功している。問題なさそう。

```text
pi@pi:~ $ ./.arduino15/packages/digistump/tools/micronucleus/2.6/micronucleus ?
> Please plug in the device ...
> Device is found!
connecting: 40% complete
> Device has firmware version 2.6
> Device signature: 0x1e930b
> Bootloader entry condition: The bootloader is activated if the D- pin is high, i.e. a pullup resistor is attached and powered and a power on condition was detected.
> Bootloader exit condition: The bootloader exits fast (< 1 second) if no USB detected.
> Available space for user applications: 6586 bytes
> Suggested sleep time between sending pages: 7ms
> Whole page count: 103  page size: 64
> Erase function sleep duration: 721ms
parsing: 40% complete
> Error opening ?: No such file or directory
> Error loading or parsing hex file.
```

　スケッチは消えてしまっているので、再度書き込み。

```text
pi@pi:~ $ arduino-cli upload -p /dev/ttyAMA0 -b digistump:avr:digispark-tiny:clock=clock165 digispark_sleepless
> Please plug in the device (will time out in 60 seconds) ...
> Device is found!
connecting: 16% complete
connecting: 22% complete
connecting: 28% complete
connecting: 33% complete
> Device has firmware version 2.6
> Device signature: 0x1e930b
> Bootloader entry condition: The bootloader is activated if the D- pin is high, i.e. a pullup resistor is attached and powered and a power on condition was detected.
> Bootloader exit condition: The bootloader exits fast (< 1 second) if no USB detected.
> Available space for user applications: 6586 bytes
> Suggested sleep time between sending pages: 7ms
> Whole page count: 103  page size: 64
> Erase function sleep duration: 721ms
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

　動作確認を行って、問題ないのを確認した。

![](/2023-03-22/5477889-01.png)

![](/2023-03-22/5477889-02.png)

![](/2023-03-22/5477889-03.png)

![](/2023-03-22/5477889-04.png)

---
> オリジナル投稿：<br>
> Digispark開発環境再び - RaspiOS Liteでmicronucleus書き込み｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/5477889>

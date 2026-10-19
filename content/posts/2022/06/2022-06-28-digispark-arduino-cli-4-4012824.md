+++
date = "2022-06-28T08:00:00"
draft = false
title = "DigisparkでArduino CLIを試す -4-"
description = "Arduino CLIでDigisparkのビルド済みバイナリを出力する方法を試します。"

[taxonomies]
tags = ["Digispark", "Arduino CLI", "2022-06"]
+++
　なんかArduino CLIの機能の宝探しをしている気分なのだけど、ドキュメント読めってことなんだろうなぁ... 今回は読まないけどw

　バイナリを吐き出すオプションというのがあって、"--export-binaries"を付けると必ずバイナリを吐き出すようなので試す。

```text
pi@pi:~ $ arduino-cli compile -b digistump:avr:digispark-tiny:clock=clock165 digispark_sleepless --export-binaries
In file included from /home/pi/digispark_sleepless/digispark_sleepless.ino:1:0:
/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/DigiMouse.h: In function 'unsigned char usbFunctionDescriptor(usbRequest*)':
/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/DigiMouse.h:323:18: warning: invalid conversion from 'const unsigned char*' to 'unsigned char*' [-fpermissive]
      usbMsgPtr = rt_usbDeviceDescriptor;
                  ^~~~~~~~~~~~~~~~~~~~~~
/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/DigiMouse.h:328:18: warning: invalid conversion from 'const unsigned char*' to 'unsigned char*' [-fpermissive]
      usbMsgPtr = rt_usbHidReportDescriptor;
                  ^~~~~~~~~~~~~~~~~~~~~~~~~
Sketch uses 2840 bytes (42%) of program storage space. Maximum is 6650 bytes.
Global variables use 92 bytes (17%) of dynamic memory, leaving 420 bytes for local variables. Maximum is 512 bytes.
```

```text
Used library   Version Path
DigisparkMouse         /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse
```

```text
Used platform Version Path
digistump:avr 1.7.5   /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5
```

　tmpではない配下のディレクトリにバイナリがコピーされている。

```text
pi@pi:~ $ find ./ | grep sleepless
./Arduino/digispark_sleepless
./Arduino/digispark_sleepless/digispark_sleepless.ino
./digispark_sleepless
./digispark_sleepless/digispark_sleepless.ino
./digispark_sleepless/build
./digispark_sleepless/build/digistump.avr.digispark-tiny
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.eep
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.with_bootloader.bin
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.with_bootloader.hex
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.lst
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.map
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.hex
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.elf
```

　環境変数で"ARDUINO_SKETCH_ALWAYS_EXPORT_BINARIES"を指定することで同じ効果があるというのを見つけたのでテストする。これも有効のようだ。

```text
pi@pi:~ $ rm -rf ./digispark_sleepless/build/*
pi@pi:~ $ export ARDUINO_SKETCH_ALWAYS_EXPORT_BINARIES=true
pi@pi:~ $ echo $ARDUINO_SKETCH_ALWAYS_EXPORT_BINARIES
true
pi@pi:~ $ arduino-cli compile -b digistump:avr:digispark-tiny:clock=clock165 digispark_sleepless
(snip)
```

```text
pi@pi:~ $ find ./ | grep sleepless
./Arduino/digispark_sleepless
./Arduino/digispark_sleepless/digispark_sleepless.ino
./digispark_sleepless
./digispark_sleepless/digispark_sleepless.ino
./digispark_sleepless/build
./digispark_sleepless/build/digistump.avr.digispark-tiny
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.eep
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.with_bootloader.bin
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.with_bootloader.hex
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.lst
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.map
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.hex
./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.elf
```

　毎回何らかの指定をするのは面倒なので、ビルド時には必ずバイナリを残すようにしたい。こういう場合は、".arduino15/arduino-cli.yaml"に設定をしておく。

```text
pi@pi:~ $ vi ./.arduino15/arduino-cli.yaml
```

　デフォルトでは以下になっている。

```text
sketch:
  always_export_binaries: false
```

　trueに変更しておく。

```text
sketch:
  always_export_binaries: true
```

　ビルドしてみると、ファイルができているのが確認できた。

```text
pi@pi:~ $ rm -rf ./digispark_sleepless/build/*
pi@pi:~ $ export ARDUINO_SKETCH_ALWAYS_EXPORT_BINARIES
pi@pi:~ $ echo $ARDUINO_SKETCH_ALWAYS_EXPORT_BINARIES
```

```text
pi@pi:~ $
pi@pi:~ $ arduino-cli compile -b digistump:avr:digispark-tiny:clock=clock165 digispark_sleepless
(snip)
```

```text
pi@pi:~ $ ls -l ./digispark_sleepless/build/digistump.avr.digispark-tiny/
total 244
-rw-r--r-- 1 pi pi     13 Jun 20 16:58 digispark_sleepless.ino.eep
-rwxr-xr-x 1 pi pi  35908 Jun 20 16:58 digispark_sleepless.ino.elf
-rw-r--r-- 1 pi pi   8020 Jun 20 16:58 digispark_sleepless.ino.hex
-rw-r--r-- 1 pi pi 170203 Jun 20 16:58 digispark_sleepless.ino.lst
-rw-r--r-- 1 pi pi  15141 Jun 20 16:58 digispark_sleepless.ino.map
-rw-r--r-- 1 pi pi   2316 Jun 20 16:58 digispark_sleepless.ino.with_bootloader.bin
-rw-r--r-- 1 pi pi   6092 Jun 20 16:58 digispark_sleepless.ino.with_bootloader.hex
```

　現在のarduino-cli.yamlの設定は以下の状態になっている。他にも使えそうなオプションがデフォルトで書かれている。

```text
pi@pi:~ $ cat .arduino15/arduino-cli.yaml
board_manager:
  additional_urls:
  - https://raw.githubusercontent.com/ArminJo/DigistumpArduino/master/package_digistump_index.json
daemon:
  port: "50051"
directories:
  data: /home/pi/.arduino15
  downloads: /home/pi/.arduino15/staging
  user: /home/pi/Arduino
library:
  enable_unsafe_install: false
logging:
  file: ""
  format: text
  level: info
metrics:
  addr: :9090
  enabled: true
output:
  no_color: false
sketch:
  always_export_binaries: true
updater:
  enable_notification: true
```

---
> オリジナル投稿：<br>
> DigisparkでArduino CLIを試す -4-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/4012824>

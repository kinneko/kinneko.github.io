+++
date = "2022-06-27T08:00:00"
draft = false
title = "DigisparkでArduino CLIを試す -3-"
description = "Arduino CLIでDigispark用スケッチをコンパイルし、FQBNとビルド手順を確認する。"

[taxonomies]
tags = ["Digispark", "Arduino CLI", "Raspberry Pi", "2022-06"]
+++

　スリープレス・ドングル用のスケッチ"digispark_sleepless"をコンパイルしてみる。

```text
pi@pi:~ $ find ./ | grep sleepless
./Arduino/digispark_sleepless
./Arduino/digispark_sleepless/digispark_sleepless.ino
```

　設定でスケッチのPATHは見ていないのね。

```text
pi@pi:~ $ arduino-cli compile -b digistump:avr digispark_sleepless
Error opening sketch: no valid sketch found in /home/pi: missing /home/pi/pi.ino
pi@pi:~ $ arduino-cli compile -b digistump:avr digispark_sleepless.ino
Error opening sketch: no valid sketch found in /home/pi: missing /home/pi/pi.ino
```

　フルパスで渡してみる。指定されたFQBNはないというエラーになる。

```text
pi@pi:~ $ arduino-cli compile -b digistump:avr ./Arduino/digispark_sleepless/digispark_sleepless.ino

Used platform Version Path

Error during build: Invalid FQBN: not an FQBN: digistump:avr
```

　ボードを指定する情報が足りないようだ。digistump:avrの下に、さらに何か書かないといけなさそう。でも、それって、どうやって調べるんだ？

　どうやら"board listall"でインストール済みのボード一覧が表示されるようだ。

```text
pi@pi:~ $ arduino-cli board listall
Board Name                       FQBN
Adafruit Circuit Playground      arduino:avr:circuitplay32u4cat
Arduino BT                       arduino:avr:bt
Arduino Duemilanove or Diecimila arduino:avr:diecimila
Arduino Esplora                  arduino:avr:esplora
Arduino Ethernet                 arduino:avr:ethernet
Arduino Fio                      arduino:avr:fio
Arduino Gemma                    arduino:avr:gemma
Arduino Industrial 101           arduino:avr:chiwawa
Arduino Leonardo                 arduino:avr:leonardo
Arduino Leonardo ETH             arduino:avr:leonardoeth
Arduino Mega ADK                 arduino:avr:megaADK
Arduino Mega or Mega 2560        arduino:avr:mega
Arduino Micro                    arduino:avr:micro
Arduino Mini                     arduino:avr:mini
Arduino NG or older              arduino:avr:atmegang
Arduino Nano                     arduino:avr:nano
Arduino Pro or Pro Mini          arduino:avr:pro
Arduino Robot Control            arduino:avr:robotControl
Arduino Robot Motor              arduino:avr:robotMotor
Arduino Uno                      arduino:avr:uno
Arduino Uno Mini                 arduino:avr:unomini
Arduino Uno WiFi                 arduino:avr:unowifi
Arduino Yún                      arduino:avr:yun
Arduino Yún Mini                 arduino:avr:yunmini
Digispark                        digistump:avr:digispark-tiny
Digispark Pro (16 MHz)           digistump:avr:digispark-pro
LilyPad Arduino                  arduino:avr:lilypad
LilyPad Arduino USB              arduino:avr:LilyPadUSB
Linino One                       arduino:avr:one
```

　というわけで、"digistump:avr:digispark-tiny"がFBQNだとわかったので、ボード設定情報を確認してみる。

```text
pi@pi:~ $ arduino-cli board details -b digistump:avr:digispark-tiny
Board name:            Digispark
FQBN:                  digistump:avr:digispark-tiny
Board version:         1.7.5
Package name:          digistump
Package maintainer:    Digistump,ArminJo
Package URL:           https://raw.githubusercontent.com/ArminJo/DigistumpArduino/master/package_digistump_index.json
Package website:       https://github.com/ArminJo/DigistumpArduino
Package online help:   https://github.com/ArminJo/DigistumpArduino
Platform name:         Digistump AVR Boards
Platform category:     Digistump
Platform architecture: avr
Platform URL:          https://github.com/ArminJo/DigistumpArduino/raw/master/digistump-avr-1.7.5.zip
Platform file name:    digistump-avr-1.7.5.zip
Platform size (bytes): 2261198
Platform checksum:     SHA-256:cf37933e721eecc010d1e890cff4174ad8439662e4e610a6cd950f0ce8c124f0
Required tool:         arduino:avr-gcc                                                               7.3.0-atmel3.6.1-arduino7
Required tool:         digistump:micronucleus                                                        2.6
Option:                Clock                                                                                                                                 clock
16 MHz - No USB                                                               ✔                                                       clock=clock16
16.5 MHz - For V-USB                                                                                                                  clock=clock165
8 MHz - No USB                                                                                                                        clock=clock8
1 MHz - No USB                                                                                                                        clock=clock1
Option:                Micronucleus variant                                                                                                                  micronucleus
Default (6650 bytes avail.)                                                   ✔                                                       micronucleus=default
Recommended (6586 bytes avail.)                                                                                                       micronucleus=recommended
Entry on reset (6586 bytes avail.)                                                                                                    micronucleus=entryReset
Agressive (6778)                                                                                                                      micronucleus=agressive
Option:                Burn Bootloader Method                                                                                                                burnmode
Upgrade (via USB)                                                             ✔                                                       burnmode=upgrade
Fresh Install (via ISP)                                                                                                               burnmode=install
Bootloader informations (via USB), no programming                                                                                     burnmode=info
Programmers:           Id                                                                            Name
arduinoasisp32u4                                                              Arduino Leo/Micro as ISP (ATmega32U4)
avrisp                                                                        AVR ISP
usbtinyisp2                                                                   USBtinyISP (ATTinyCore) FAST, for parts running >=2 MHz
diamexusbisp                                                                  Diamex USB ISP
dragon                                                                        AVR Dragon ISP mode (ATTinyCore)
arduinoasisp                                                                  Arduino as ISP
micronucleusprog                                                              micronucleus.2.5
ponyser                                                                       Ponyser Programmer
usbasp                                                                        USBasp (ATTinyCore)
parallel                                                                      Parallel Programmer
avrispmkii                                                                    AVRISP mkII
atmel_ice                                                                     Atmel-ICE
stk500                                                                        Atmel STK500
usbtinyisp                                                                    USBtinyISP (ATTinyCore) SLOW, for new or 1 MHz parts
```

　基本的にはArduino IDEでメニューに出てくる内容とまったく同じだ。選ばれているオプションは緑色で表示されて、チェックマークが付いているのがわかる。

　でも、このままでは使えない。クロックは「16 MHz - No USB」になっていて、USBが使えなくなっている。これを「16.5 MHz - For V-USB」に変更してやる必要がある。どうやって選択したらいいのだろう？

　設定のオプションは、FQBNの後にコロンでつないで付けるようだ。複数ある場合は、カンマでつなげて増やす。

```text
pi@pi:~ $ arduino-cli board details -b digistump:avr:digispark-tiny:clock=clock165
(snip)
Option:                Clock                                                                                                                                 clock
16 MHz - No USB                                                                                                                       clock=clock16
16.5 MHz - For V-USB                                                          ✔                                                       clock=clock165
8 MHz - No USB                                                                                                                        clock=clock8
1 MHz - No USB                                                                                                                        clock=clock1
(snip)
```

　ここまでで、ようやくビルドできる感じがわかってきた。ビルドしてみる。

```text
pi@pi:~ $ arduino-cli compile -b digistump:avr:digispark-tiny:clock=clock165 ./Arduino/digispark_sleepless/digispark_sleepless.ino
In file included from /home/pi/Arduino/digispark_sleepless/digispark_sleepless.ino:1:0:
/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/DigiMouse.h: In function 'unsigned char usbFunctionDescriptor(usbRequest*)':
/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/DigiMouse.h:323:18: warning: invalid conversion from 'const unsigned char*' to 'unsigned char*' [-fpermissive]
usbMsgPtr = rt_usbDeviceDescriptor;
^~~~~~~~~~~~~~~~~~~~~~
/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/DigiMouse.h:328:18: warning: invalid conversion from 'const unsigned char*' to 'unsigned char*' [-fpermissive]
usbMsgPtr = rt_usbHidReportDescriptor;
^~~~~~~~~~~~~~~~~~~~~~~~~
Sketch uses 2840 bytes (42%) of program storage space. Maximum is 6650 bytes.
Global variables use 92 bytes (17%) of dynamic memory, leaving 420 bytes for local variables. Maximum is 512 bytes.
Used library   Version Path
DigisparkMouse         /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse
Used platform Version Path
digistump:avr 1.7.5   /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5
```

　２つ警告が出ているが、ビルドは通ったようだ。Arduino IDEを使うより、はるかに早い感じ。これは使えそう。

　しかし、hexファイルはどこに出ているのだろう？探してみても見つからない。削除されているのかな？

　通常は、スケッチを作成するのもCLIから行うようだ。オプションは"sketch new"。

```text
pi@pi:~ $ arduino-cli sketch new digispark_sleepless
Sketch created in: /home/pi/digispark_sleepless
pi@pi:~ $ ls -al digispark_sleepless/
total 12
drwxr-xr-x  2 pi pi 4096 Jun 20 16:17 .
drwxr-xr-x 19 pi pi 4096 Jun 20 16:17 ..
-rw-r--r--  1 pi pi   35 Jun 20 16:17 digispark_sleepless.ino
pi@pi:~ $ cat digispark_sleepless/digispark_sleepless.ino
void setup() {
}
void loop() {
}
```

　Arduino IDEで新規にスケッチを開いた時と同じで、ディレクトリが掘られて、スケルトンが書かれている。viで編集して、スリープレス・ドングルのスケッチを書く。

```text
pi@pi:~ $ vi digispark_sleepless/digispark_sleepless.ino
```

　ビルドする。こんどはフルパスを渡さなくてもスケッチ名だけで良い感じ。

```text
pi@pi:~ $ arduino-cli compile -b digistump:avr:digispark-tiny:clock=clock165 digispark_sleepless
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
Used library   Version Path
DigisparkMouse         /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse
Used platform Version Path
digistump:avr 1.7.5   /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5
```

　hexを探してみるけど、やっぱり見つからない。

```text
pi@pi:~ $ find ./ | grep sleepless
./Arduino/digispark_sleepless
./Arduino/digispark_sleepless/digispark_sleepless.ino
./digispark_sleepless
./digispark_sleepless/digispark_sleepless.ino
```

　そういえば、/tmpも使っていたなと思い出したので、探してみるとあった。

```text
pi@pi:~ $ ls -l /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C
total 276
-rw-r--r-- 1 pi pi    462 Jun 20 16:21 build.options.json
-rw-r--r-- 1 pi pi   7133 Jun 20 16:21 compile_commands.json
drwxr-xr-x 2 pi pi   4096 Jun 20 16:21 core
-rw-r--r-- 1 pi pi     13 Jun 20 16:21 digispark_sleepless.ino.eep
-rwxr-xr-x 1 pi pi  35908 Jun 20 16:21 digispark_sleepless.ino.elf
-rw-r--r-- 1 pi pi   8020 Jun 20 16:21 digispark_sleepless.ino.hex
-rw-r--r-- 1 pi pi 170203 Jun 20 16:21 digispark_sleepless.ino.lst
-rw-r--r-- 1 pi pi  15141 Jun 20 16:21 digispark_sleepless.ino.map
-rw-r--r-- 1 pi pi   2316 Jun 20 16:21 digispark_sleepless.ino.with_bootloader.bin
-rw-r--r-- 1 pi pi   6092 Jun 20 16:21 digispark_sleepless.ino.with_bootloader.hex
-rw-r--r-- 1 pi pi   1371 Jun 20 16:21 includes.cache
drwxr-xr-x 3 pi pi   4096 Jun 20 16:21 libraries
drwxr-xr-x 2 pi pi   4096 Jun 20 16:21 preproc
drwxr-xr-x 2 pi pi   4096 Jun 20 16:21 sketch
pi@pi:~ $ cat /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/digispark_sleepless.ino.hex
:1000000082C0A6C083C3A4C00EC3A2C0A1C0A0C0AA
:100010009FC09EC09DC09CC09BC09AC099C0120149
:10002000010100000008C016DA27000101020001EA
:1000300005010902A1010901A1000509190129030E
:100040001500250195037501810295017505810152
:100050000501093009311581257F75089502810652
:10006000093895018106C0C000370038010101013F
:1000700001010102040810202803640069006700E0
:1000800069007300740075006D0070002E0063003D
:100090006F006D003A004D006F0075007300650041
(snip)
```

　"-v"オプションで詳細ログを出しても、inoやelfの場所が確認できる。

```text
pi@pi:~ $ arduino-cli compile -b digistump:avr:digispark-tiny:clock=clock165 digispark_sleepless -v
Using board 'digispark-tiny' from platform in folder: /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5
Using core 'tiny' from platform in folder: /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5
Detecting libraries used...
/home/pi/.arduino15/packages/arduino/tools/avr-gcc/7.3.0-atmel3.6.1-arduino7/bin/avr-g++ -c -g -Os -Wall -Wextra -std=gnu++11 -fpermissive -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -flto -w -x c++ -E -CC -mmcu=attiny85 -DF_CPU=16500000L -DSERIAL_BUFFER_SIZE= -DARDUINO=10607 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR -DARDUINO=10607 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR "-DDIGISTUMPCORE=\"1.7.5\"" -DDIGISTUMPCORE_MAJOR=1UL -DDIGISTUMPCORE_MINOR=7UL -DDIGISTUMPCORE_PATCH=5UL -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/cores/tiny -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/variants/digispark /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/sketch/digispark_sleepless.ino.cpp -o /dev/null
Alternatives for DigiMouse.h: [DigisparkMouse]
ResolveLibrary(DigiMouse.h)
-> candidates: [DigisparkMouse]
/home/pi/.arduino15/packages/arduino/tools/avr-gcc/7.3.0-atmel3.6.1-arduino7/bin/avr-g++ -c -g -Os -Wall -Wextra -std=gnu++11 -fpermissive -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -flto -w -x c++ -E -CC -mmcu=attiny85 -DF_CPU=16500000L -DSERIAL_BUFFER_SIZE= -DARDUINO=10607 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR -DARDUINO=10607 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR "-DDIGISTUMPCORE=\"1.7.5\"" -DDIGISTUMPCORE_MAJOR=1UL -DDIGISTUMPCORE_MINOR=7UL -DDIGISTUMPCORE_PATCH=5UL -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/cores/tiny -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/variants/digispark -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/sketch/digispark_sleepless.ino.cpp -o /dev/null
Using cached library dependencies for file: /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/oddebug.c
Using cached library dependencies for file: /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/osccal.c
Using cached library dependencies for file: /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/usbdrv.c
/home/pi/.arduino15/packages/arduino/tools/avr-gcc/7.3.0-atmel3.6.1-arduino7/bin/avr-g++ -c -g -Os -Wall -Wextra -std=gnu++11 -fpermissive -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -flto -w -x c++ -E -CC -mmcu=attiny85 -DF_CPU=16500000L -DSERIAL_BUFFER_SIZE= -DARDUINO=10607 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR -DARDUINO=10607 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR "-DDIGISTUMPCORE=\"1.7.5\"" -DDIGISTUMPCORE_MAJOR=1UL -DDIGISTUMPCORE_MINOR=7UL -DDIGISTUMPCORE_PATCH=5UL -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/cores/tiny -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/variants/digispark -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/usbdrvasm.S -o /dev/null
Error while detecting libraries included by /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/usbdrvasm.S
Generating function prototypes...
/home/pi/.arduino15/packages/arduino/tools/avr-gcc/7.3.0-atmel3.6.1-arduino7/bin/avr-g++ -c -g -Os -Wall -Wextra -std=gnu++11 -fpermissive -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -flto -w -x c++ -E -CC -mmcu=attiny85 -DF_CPU=16500000L -DSERIAL_BUFFER_SIZE= -DARDUINO=10607 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR -DARDUINO=10607 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR "-DDIGISTUMPCORE=\"1.7.5\"" -DDIGISTUMPCORE_MAJOR=1UL -DDIGISTUMPCORE_MINOR=7UL -DDIGISTUMPCORE_PATCH=5UL -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/cores/tiny -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/variants/digispark -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/sketch/digispark_sleepless.ino.cpp -o /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/preproc/ctags_target_for_gcc_minus_e.cpp
/home/pi/.arduino15/packages/builtin/tools/ctags/5.8-arduino11/ctags -u --language-force=c++ -f - --c++-kinds=svpf --fields=KSTtzns --line-directives /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/preproc/ctags_target_for_gcc_minus_e.cpp
Compiling sketch...
/home/pi/.arduino15/packages/arduino/tools/avr-gcc/7.3.0-atmel3.6.1-arduino7/bin/avr-g++ -c -g -Os -Wall -Wextra -std=gnu++11 -fpermissive -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -flto -MMD -mmcu=attiny85 -DF_CPU=16500000L -DSERIAL_BUFFER_SIZE= -DARDUINO=10607 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR -DARDUINO=10607 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR "-DDIGISTUMPCORE=\"1.7.5\"" -DDIGISTUMPCORE_MAJOR=1UL -DDIGISTUMPCORE_MINOR=7UL -DDIGISTUMPCORE_PATCH=5UL -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/cores/tiny -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/variants/digispark -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/sketch/digispark_sleepless.ino.cpp -o /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/sketch/digispark_sleepless.ino.cpp.o
In file included from /home/pi/digispark_sleepless/digispark_sleepless.ino:1:0:
/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/DigiMouse.h: In function 'unsigned char usbFunctionDescriptor(usbRequest*)':
/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/DigiMouse.h:323:18: warning: invalid conversion from 'const unsigned char*' to 'unsigned char*' [-fpermissive]
usbMsgPtr = rt_usbDeviceDescriptor;
^~~~~~~~~~~~~~~~~~~~~~
/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/DigiMouse.h:328:18: warning: invalid conversion from 'const unsigned char*' to 'unsigned char*' [-fpermissive]
usbMsgPtr = rt_usbHidReportDescriptor;
^~~~~~~~~~~~~~~~~~~~~~~~~
Compiling libraries...
Compiling library "DigisparkMouse"
/home/pi/.arduino15/packages/arduino/tools/avr-gcc/7.3.0-atmel3.6.1-arduino7/bin/avr-gcc -c -g -x assembler-with-cpp -flto -mmcu=attiny85 -DF_CPU=16500000L -DSERIAL_BUFFER_SIZE= -DARDUINO=10607 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR -DARDUINO=10607 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR "-DDIGISTUMPCORE=\"1.7.5\"" -DDIGISTUMPCORE_MAJOR=1UL -DDIGISTUMPCORE_MINOR=7UL -DDIGISTUMPCORE_PATCH=5UL -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/cores/tiny -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/variants/digispark -I/home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse/usbdrvasm.S -o /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/libraries/DigisparkMouse/usbdrvasm.S.o
Using previously compiled file: /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/libraries/DigisparkMouse/osccal.c.o
Using previously compiled file: /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/libraries/DigisparkMouse/oddebug.c.o
Using previously compiled file: /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/libraries/DigisparkMouse/usbdrv.c.o
Compiling core...
Using previously compiled file: /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/core/pins_arduino.c.o
Using precompiled core: /tmp/arduino-core-cache/core_digistump_avr_digispark-tiny_clock_clock165_362f33b417d6d7a395420a223c2238ec.a
Linking everything together...
/home/pi/.arduino15/packages/arduino/tools/avr-gcc/7.3.0-atmel3.6.1-arduino7/bin/avr-gcc -Os -g -Wl,--gc-sections -mrelax -fmerge-all-constants -mmcu=attiny85 -o /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/digispark_sleepless.ino.elf /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/sketch/digispark_sleepless.ino.cpp.o /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/libraries/DigisparkMouse/oddebug.c.o /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/libraries/DigisparkMouse/osccal.c.o /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/libraries/DigisparkMouse/usbdrv.c.o /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/libraries/DigisparkMouse/usbdrvasm.S.o /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/core/pins_arduino.c.o /tmp/arduino-core-cache/core_digistump_avr_digispark-tiny_clock_clock165_362f33b417d6d7a395420a223c2238ec.a -L/tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C -lm
/home/pi/.arduino15/packages/arduino/tools/avr-gcc/7.3.0-atmel3.6.1-arduino7/bin/avr-objcopy -O ihex -j .eeprom --set-section-flags=.eeprom=alloc,load --no-change-warnings --change-section-lma .eeprom=0 /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/digispark_sleepless.ino.elf /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/digispark_sleepless.ino.eep
/home/pi/.arduino15/packages/arduino/tools/avr-gcc/7.3.0-atmel3.6.1-arduino7/bin/avr-objcopy -O ihex -R .eeprom /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/digispark_sleepless.ino.elf /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/digispark_sleepless.ino.hex
bash -c "/home/pi/.arduino15/packages/arduino/tools/avr-gcc/7.3.0-atmel3.6.1-arduino7/bin/avr-objdump --disassemble --source --line-numbers --demangle --section=.text /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/digispark_sleepless.ino.elf > /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/digispark_sleepless.ino.lst"
bash -c "/home/pi/.arduino15/packages/arduino/tools/avr-gcc/7.3.0-atmel3.6.1-arduino7/bin/avr-nm --numeric-sort --line-numbers --print-size  /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/digispark_sleepless.ino.elf > /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/digispark_sleepless.ino.map"
Using library DigisparkMouse in folder: /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse (legacy)
/home/pi/.arduino15/packages/arduino/tools/avr-gcc/7.3.0-atmel3.6.1-arduino7/bin/avr-size -A /tmp/arduino-sketch-AE54463E157DE1275E94BEA6E672C89C/digispark_sleepless.ino.elf
Sketch uses 2840 bytes (42%) of program storage space. Maximum is 6650 bytes.
Global variables use 92 bytes (17%) of dynamic memory, leaving 420 bytes for local variables. Maximum is 512 bytes.
Used library   Version Path
DigisparkMouse         /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5/libraries/DigisparkMouse
Used platform Version Path
digistump:avr 1.7.5   /home/pi/.arduino15/packages/digistump/hardware/avr/1.7.5
```

---
> オリジナル投稿：<br>
> DigisparkでArduino CLIを試す -3-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/4012607>

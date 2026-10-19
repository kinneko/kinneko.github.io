+++
date = "2022-06-23T08:00:00"
draft = false
title = "DigisparkでArduino CLIを試す -1-"
description = "Raspberry Pi 3にArduino CLIを導入し、Digisparkの書き込み作業をコマンドライン化する。"

[taxonomies]
tags = ["Digispark", "Arduino CLI", "Raspberry Pi", "2022-06"]

[extra]
image = "/2022-06-23/3921422-title.jpeg"
+++

　Raspi3でUSB起動するDigisparkのスケッチ書き込み環境を作ったのだけど、ArduinoIDEを起動するのにモニタを点けないといけないのはどうにも面倒だ。

　できれば、sshで接続したらそのまま書き込み作業をやりたい。

　またArduinoIDEを使うと、書き込み時に都度ビルドが行われるので時間がかかる。同じパターンの生産を行うのであれば、ビルド済みのバイナリを書き込みするだけのほうが快適な作業ができる。

　Raspi3側でも、GUIが動作しないほうが、Raspiの動作メモリにもやさしい環境になる。HDMIやUSBマウスや、USBキーボードを接続しない分、電力的にも安定する。

　そういえば、Arduino CLIというのがあったなということで調べてみる。最新版は、0.23であるようだ。

> GitHub - arduino/arduino-cli: Arduino command line tool<br>
> <https://github.com/arduino/arduino-cli>

![](/2022-06-23/3921422-01.png)

> Arduino CLI<br>
> <https://arduino.github.io/arduino-cli/0.22/>

![](/2022-06-23/3921422-02.png)

> Installation - Arduino CLI<br>
> <https://arduino.github.io/arduino-cli/0.23/installation/>

![](/2022-06-23/3921422-03.png)

　インストールドキュメントには、まずはberwを使うように書かれている。あとは、シェエルスクリプトでインストールする方法と、ビルド済みのバイナリを導入する方法がある。

　macOS環境ではないので、Homeberwを入れるのは問題ないのだけれど、なんか気持ち悪いので、シェルスクリプトでインストールする。

　シェルスクリプトをダウンロードしてインストールする場合には、環境変数BINDIRを指定することで、インストール場所を設定できるようだ。

　最近のローカルバイナリのインストールパスは、"~/.local/bin"を使うのが一般的で標準でPATHも通っているようだ。RaspiOSではどうか確認してみたが、残念ながらパスは通っていなかった。

```text
pi@pi:~ $ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games
```

　また、インストール時にバージョンの指定もできる。

```text
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=/usr/local/bin sh -s 0.23.x
```

　master/install.shが何をやっているか簡単に見てみる。

> <https://raw.githubusercontent.com/arduino/arduino-cli/0.23.x/install.sh>

　基本的にはcurl/wgetでダウンロードしてきて、/tmpの下に作業ディレクトリを掘って、アーカイブを展開し、それを指定ディレクトリにコピーしているだけのようだ。中でビルド作業などはやっていない。

　特にシェルスクリプトを使って導入するような理由はなさそうだ。

　バイナリをダウンロードするのは、Linux ARM 32 bitとあるのはARMv7のバイナリのようだ(今の環境はRaspi3でRaspiOS 32bitをインストールしてある)。その他に64bitのものも用意されている。このリンクはlatestでバージョンは指定できないのね。

> <https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Linux_ARMv7.tar.gz>

> <https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Linux_ARM64.tar.gz>

```text
pi@pi:~ $ curl -OL https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Linux_ARMv7.tar.gz
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
Dload  Upload   Total   Spent    Left  Speed
0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0
100 11.4M  100 11.4M    0     0  22812      0  0:08:46  0:08:46 --:--:-- 52119
pi@pi:~ $ ls -alh arduino-cli_latest_Linux_ARMv7.tar.gz
-rw-r--r-- 1 pi pi 12M Jun 20 14:35 arduino-cli_latest_Linux_ARMv7.tar.gz
```

　ファイル2個しか入ってないw

```text
pi@pi:~ $ tar xvf arduino-cli_latest_Linux_ARMv7.tar.gz
arduino-cli
LICENSE.txt
```

　バージョンの確認をしてみる。

```text
pi@pi:~ $ ./arduino-cli --help
Arduino Command Line Interface (arduino-cli).
Usage:
arduino-cli [command]
Examples:
./arduino-cli <command> [flags...]
Available Commands:
board           Arduino board commands.
burn-bootloader Upload the bootloader.
cache           Arduino cache commands.
compile         Compiles Arduino sketches.
completion      Generates completion scripts
config          Arduino configuration commands.
core            Arduino core operations.
daemon          Run as a daemon on port: 50051
debug           Debug Arduino sketches.
help            Help about any command
lib             Arduino commands about libraries.
monitor         Open a communication port with a board.
outdated        Lists cores and libraries that can be upgraded
sketch          Arduino CLI sketch commands.
update          Updates the index of cores and libraries
upgrade         Upgrades installed cores and libraries.
upload          Upload Arduino sketches.
version         Shows version number of Arduino CLI.
Flags:
--additional-urls strings   Comma-separated list of additional URLs for the Boards Manager.
--config-file string        The custom config file (if not specified the default will be used).
--format string             The output format for the logs, can be: text, json, jsonmini, yaml (default "text")
-h, --help                      help for arduino-cli
--log-file string           Path to the file where logs will be written.
--log-format string         The output format for the logs, can be: text, json
--log-level string          Messages with this level and above will be logged. Valid levels are: trace, debug, info, warn, error, fatal, panic
--no-color                  Disable colored output.
-v, --verbose                   Print the logs on the standard output.
Use "arduino-cli [command] --help" for more information about a command.
pi@pi:~ $ ./arduino-cli version
arduino-cli  Version: 0.23.0 Commit: 899dc91b Date: 2022-06-06T14:23:44Z
```

　実行ファイル１つだけなら、置き場所とかあんまり気にする必要はないね。"/usr/local/bin/"に配置する。

```text
pi@pi:~ $ sudo mv arduino-cli /usr/local/bin/
pi@pi:~ $ which arduino-cli
/usr/local/bin/arduino-cli
```

　これにてインストールは完了。

---
> オリジナル投稿：<br>
> DigisparkでArduino CLIを試す -1-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/3921422>

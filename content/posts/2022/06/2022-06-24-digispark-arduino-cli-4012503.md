+++
date = "2022-06-24T08:00:00"
draft = false
title = "DigisparkでArduino CLIを試す -2-"
description = "Arduino CLIの設定ファイルとボードマネージャを整え、Digistump AVR Boardsを使えるようにする。"

[taxonomies]
tags = ["Digispark", "Arduino CLI", "Raspberry Pi", "2022-06"]
+++

　インストールは終わったので、Digisparkのための環境設定をやっておく。

　Arduino IDEでは、設定ファイルにボードの追加のためのJSONパスを書き込んで、ボードマネージャからボード情報をインストールしていた。

> Digisparkに書けない (Pi3編) -1-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/3873729>

> Digisparkに書けない (Pi3編) -2-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/3873794>

　このあたり、CLIではどうなるのだろうか？

　また、ボードマネージャの情報や、作成したスケッチ類はArduino IDEでは"~/.arduino15/"以下に保存されていた。

```text
pi@pi:~/.arduino15 $ ls
cache                   logs                          packages
inventory.yaml          package_digistump_index.json  preferences.txt
library_index.json      package_index.json            staging
library_index.json.sig  package_index.json.sig
```

　このあたりの情報は、Arduino IDEと共存するのだろうか？ それともCLIでは別に入るのだろうか？

　まずボード情報の追加から。

　CLIなので、CLIで設定するか、設定情報である"arduino-cli.yaml"を直接操作することになりそう。

　CLIでやるには、"arduino-cli config add board_manager.additional_urls"でJSONのパス情報を渡して追加したあとに、"arduino-cli core install"で反映する。

```text
pi@pi:~ $ arduino-cli config add board_manager.additional_urls https://raw.githubusercontent.com/ArminJo/DigistumpArduino/master/package_digistump_index.json
Can't write config file: Config File "arduino-cli" Not Found in "[/home/pi/.arduino15]"
```

　利用するファイルパスは、Arduino IDEと同じようだ。しかし、書き込み権限がないという。

```text
pi@pi:~ $ ls -al /home/pi/ | grep .arduino15
drwxr-xr-x  6 pi   pi       4096 Jun 20 14:54 .arduino15
```

　環境設定が共有できるようなら、そのままでもインストール済みになっていると思われる。ボードマネージャのパッケージを検索してみよう。

```text
pi@pi:~ $ arduino-cli core search attiny
Downloading index: package_index.tar.bz2 downloaded
Downloading missing tool builtin:ctags@5.8-arduino11...
builtin:ctags@5.8-arduino11 downloaded
Installing builtin:ctags@5.8-arduino11...
builtin:ctags@5.8-arduino11 installed
Downloading missing tool builtin:serial-discovery@1.3.2...
builtin:serial-discovery@1.3.2 downloaded
Installing builtin:serial-discovery@1.3.2...
builtin:serial-discovery@1.3.2 installed
Downloading missing tool builtin:mdns-discovery@1.0.5...
builtin:mdns-discovery@1.0.5 downloaded
Installing builtin:mdns-discovery@1.0.5...
builtin:mdns-discovery@1.0.5 installed
Downloading missing tool builtin:serial-monitor@0.9.1...
builtin:serial-monitor@0.9.1 989.78 KiB / 1.74 MiB [======>-----]  55.41% 00m23s
(snip)
```

　気軽にやったら、なんかデフォルトパッケージのダウンロードをはじめてしまったようだ。しばし待つ。

```text
Installing builtin:serial-monitor@0.9.1...
builtin:serial-monitor@0.9.1 installed
No platforms matching your search.
```

　attinyはないということだ。つまり、環境設定は別になっているということか。

　ほんとは、"arduino-cli core init"とかをやる必要があったのかな？

```text
pi@pi:~ $ ls -al /home/pi/.arduino15
total 26176
drwxr-xr-x  7 pi pi     4096 Jun 20 15:18 .
drwxr-xr-x 18 pi pi     4096 Jun 20 14:56 ..
drwxr-xr-x  4 pi pi     4096 May 27 18:51 cache
-rw-r--r--  1 pi pi      168 Jun 20 14:54 inventory.yaml
-rw-r--r--  1 pi pi 26222410 Jun 16 17:10 library_index.json
-rw-r--r--  1 pi pi      543 Jun 16 17:10 library_index.json.sig
drwxr-xr-x  2 pi pi     4096 May 27 18:09 logs
-rw-r--r--  1 pi pi    20069 Jun 16 17:09 package_digistump_index.json
-rw-r--r--  1 pi pi   514288 Jun 20 15:18 package_index.json
-rw-r--r--  1 pi pi      543 Jun 20 15:18 package_index.json.sig
drwxr-xr-x  5 pi pi     4096 Jun 20 15:18 packages
-rw-------  1 pi pi     3480 Jun 16 16:40 preferences.txt
drwxr-xr-x  3 pi pi     4096 May 27 18:51 staging
drwxr-xr-x  2 pi pi     4096 Jun 20 15:21 tmp
```

　増えたのは"tmp"だけで、あとはそれぞれに更新されているようだ。

　調べてみると、configオプションにinitがあった。

```text
pi@pi:~ $ arduino-cli config -h
Arduino configuration commands.
Usage:
arduino-cli config [command]
Examples:
arduino-cli config init
Available Commands:
add         Adds one or more values to a setting.
delete      Deletes a settings key and all its sub keys.
dump        Prints the current configuration
init        Writes current configuration to a configuration file.
remove      Removes one or more values from a setting.
set         Sets a setting value.
Flags:
-h, --help   help for config
Global Flags:
--additional-urls strings   Comma-separated list of additional URLs for the Boards Manager.
--config-file string        The custom config file (if not specified the default will be used).
--format string             The output format for the logs, can be: text, json, jsonmini, yaml (default "text")
--log-file string           Path to the file where logs will be written.
--log-format string         The output format for the logs, can be: text, json
--log-level string          Messages with this level and above will be logged. Valid levels are: trace, debug, info, warn, error, fatal, panic
--no-color                  Disable colored output.
-v, --verbose                   Print the logs on the standard output.
Use "arduino-cli config [command] --help" for more information about a command.
```

　実行してみる。

```text
pi@pi:~ $ arduino-cli config init
Config file written to: /home/pi/.arduino15/arduino-cli.yaml
```

　設定ファイルの"arduino-cli.yaml"が作られた。

　もう一度、ボード設定を追加してみる。

```text
pi@pi:~/.arduino15 $ arduino-cli config add board_manager.additional_urls https://raw.githubusercontent.com/ArminJo/DigistumpArduino/master/package_digistump_index.json
```

　こんどは、普通に終わった。

　変更点を確認してみると、additional_urlsにJSONが追加されていた。

```text
pi@pi:~/.arduino15 $ diff arduino-cli.yaml.org arduino-cli.yaml
2c2,3
<   additional_urls: []
---
>   additional_urls:
>   - https://raw.githubusercontent.com/ArminJo/DigistumpArduino/master/package_digistump_index.json
```

　検索してみると、JSONの更新は行われたようだけど、attinyはないということだ。

```text
pi@pi:~ $ arduino-cli core search attiny
Downloading index: package_index.tar.bz2 downloaded
Downloading index: package_digistump_index.json downloaded
No platforms matching your search.
```

　"digistump"で検索すると表示された。

```text
pi@pi:~ $ arduino-cli core search digistump
ID            Version Name
digistump:avr 1.7.5   Digistump AVR Boards
```

　インストールする。

```text
pi@pi:~ $ arduino-cli core install digistump:avr
Platform digistump:avr@1.7.5 already installed
```

　これで準備完了ということか。

---
> オリジナル投稿：<br>
> DigisparkでArduino CLIを試す -2-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/4012503>

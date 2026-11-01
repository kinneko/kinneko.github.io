+++
date = "2023-07-10T08:00:00"
draft = false
title = "macOSにAndroidターゲットの画面を表示する"
description = "macOSにscrcpyを導入し、Android実機の画面を表示・操作する。"

[taxonomies]
tags = ["Android", "macOS", "scrcpy", "2023-07"]

[extra]
image = "/2023-07-10/6221599-title.jpeg"
+++

　BLEとかQRコード読みとか開発するには、実機が必要になる。リモートで、これらのデモを見せるには、macOS側で画面を表示してやる必要がある。

　アプリ化されているツールにそういうのがいろいろあるみたいだけど、いろいろ面倒そうなので、OSSのscrcpyを入れてみる。ライセンスはAPL2。動作環境はAPI 21/Android 5.0以降。そのへんの画面転送アプリよりは、いろんな機能を内包している。

> GitHub - Genymobile/scrcpy: Display and control your Android device<br>
> <https://github.com/Genymobile/scrcpy>

![](/2023-07-10/6221599-01.png)

　インストールはbrewか...

> scrcpy/doc/macos.md at master · Genymobile/scrcpy · GitHub<br>
> <https://github.com/Genymobile/scrcpy/blob/master/doc/macos.md>

　仕事で開発はじめちゃったので、諦めてbrewは入れるかな...

~~~text
% /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
==> Checking for `sudo` access (which may request your password)...
Password:
==> This script will install:
/opt/homebrew/bin/brew
/opt/homebrew/share/doc/homebrew
/opt/homebrew/share/man/man1/brew.1
/opt/homebrew/share/zsh/site-functions/_brew
/opt/homebrew/etc/bash_completion.d/brew
/opt/homebrew
==> The following new directories will be created:
/opt/homebrew/bin
/opt/homebrew/etc
/opt/homebrew/include
/opt/homebrew/lib
/opt/homebrew/sbin
/opt/homebrew/share
/opt/homebrew/var
/opt/homebrew/opt
/opt/homebrew/share/zsh
/opt/homebrew/share/zsh/site-functions
/opt/homebrew/var/homebrew
/opt/homebrew/var/homebrew/linked
/opt/homebrew/Cellar
/opt/homebrew/Caskroom
/opt/homebrew/Frameworks

Press RETURN/ENTER to continue or any other key to abort:
==> /usr/bin/sudo /usr/bin/install -d -o root -g wheel -m 0755 /opt/homebrew
==> /usr/bin/sudo /bin/mkdir -p /opt/homebrew/bin /opt/homebrew/etc /opt/homebrew/include /opt/homebrew/lib /opt/homebrew/sbin /opt/homebrew/share /opt/homebrew/var /opt/homebrew/opt /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions /opt/homebrew/var/homebrew /opt/homebrew/var/homebrew/linked /opt/homebrew/Cellar /opt/homebrew/Caskroom /opt/homebrew/Frameworks
==> /usr/bin/sudo /bin/chmod ug=rwx /opt/homebrew/bin /opt/homebrew/etc /opt/homebrew/include /opt/homebrew/lib /opt/homebrew/sbin /opt/homebrew/share /opt/homebrew/var /opt/homebrew/opt /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions /opt/homebrew/var/homebrew /opt/homebrew/var/homebrew/linked /opt/homebrew/Cellar /opt/homebrew/Caskroom /opt/homebrew/Frameworks
==> /usr/bin/sudo /bin/chmod go-w /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions
==> /usr/bin/sudo /usr/sbin/chown kinneko /opt/homebrew/bin /opt/homebrew/etc /opt/homebrew/include /opt/homebrew/lib /opt/homebrew/sbin /opt/homebrew/share /opt/homebrew/var /opt/homebrew/opt /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions /opt/homebrew/var/homebrew /opt/homebrew/var/homebrew/linked /opt/homebrew/Cellar /opt/homebrew/Caskroom /opt/homebrew/Frameworks
==> /usr/bin/sudo /usr/bin/chgrp admin /opt/homebrew/bin /opt/homebrew/etc /opt/homebrew/include /opt/homebrew/lib /opt/homebrew/sbin /opt/homebrew/share /opt/homebrew/var /opt/homebrew/opt /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions /opt/homebrew/var/homebrew /opt/homebrew/var/homebrew/linked /opt/homebrew/Cellar /opt/homebrew/Caskroom /opt/homebrew/Frameworks
==> /usr/bin/sudo /usr/sbin/chown -R kinneko:admin /opt/homebrew
==> /usr/bin/sudo /bin/mkdir -p /Users/kinneko/Library/Caches/Homebrew
==> /usr/bin/sudo /bin/chmod g+rwx /Users/kinneko/Library/Caches/Homebrew
==> /usr/bin/sudo /usr/sbin/chown -R kinneko /Users/kinneko/Library/Caches/Homebrew
==> Downloading and installing Homebrew...
remote: Enumerating objects: 243115, done.
remote: Counting objects: 100% (753/753), done.
remote: Compressing objects: 100% (451/451), done.
remote: Total 243115 (delta 297), reused 694 (delta 259), pack-reused 242362
Receiving objects: 100% (243115/243115), 71.25 MiB | 8.37 MiB/s, done.
Resolving deltas: 100% (177833/177833), done.
From https://github.com/Homebrew/brew
* [new branch]          dependabot/bundler/Library/Homebrew/json_schemer-0.2.25 -> origin/dependabot/bundler/Library/Homebrew/json_schemer-0.2.25
* [new branch]          dependabot/bundler/Library/Homebrew/parser-3.2.2.3 -> origin/dependabot/bundler/Library/Homebrew/parser-3.2.2.3
* [new branch]          master     -> origin/master
* [new tag]             0.1        -> 0.1
* [new tag]             0.2        -> 0.2
* [new tag]             0.3        -> 0.3
* [new tag]             0.4        -> 0.4
* [new tag]             0.5        -> 0.5
* [new tag]             0.6        -> 0.6
* [new tag]             0.7        -> 0.7
* [new tag]             0.7.1      -> 0.7.1
* [new tag]             0.8        -> 0.8
* [new tag]             0.8.1      -> 0.8.1
* [new tag]             0.9        -> 0.9
* [new tag]             0.9.1      -> 0.9.1
* [new tag]             0.9.2      -> 0.9.2
* [new tag]             0.9.3      -> 0.9.3
* [new tag]             0.9.4      -> 0.9.4
* [new tag]             0.9.5      -> 0.9.5
* [new tag]             0.9.8      -> 0.9.8
* [new tag]             0.9.9      -> 0.9.9
* [new tag]             1.0.0      -> 1.0.0
* [new tag]             1.0.1      -> 1.0.1
* [new tag]             1.0.2      -> 1.0.2
* [new tag]             1.0.3      -> 1.0.3
* [new tag]             1.0.4      -> 1.0.4
* [new tag]             1.0.5      -> 1.0.5
* [new tag]             1.0.6      -> 1.0.6
* [new tag]             1.0.7      -> 1.0.7
* [new tag]             1.0.8      -> 1.0.8
* [new tag]             1.0.9      -> 1.0.9
* [new tag]             1.1.0      -> 1.1.0
* [new tag]             1.1.1      -> 1.1.1
* [new tag]             1.1.10     -> 1.1.10
* [new tag]             1.1.11     -> 1.1.11
* [new tag]             1.1.12     -> 1.1.12
* [new tag]             1.1.13     -> 1.1.13
* [new tag]             1.1.2      -> 1.1.2
* [new tag]             1.1.3      -> 1.1.3
* [new tag]             1.1.4      -> 1.1.4
* [new tag]             1.1.5      -> 1.1.5
* [new tag]             1.1.6      -> 1.1.6
* [new tag]             1.1.7      -> 1.1.7
* [new tag]             1.1.8      -> 1.1.8
* [new tag]             1.1.9      -> 1.1.9
* [new tag]             1.2.0      -> 1.2.0
* [new tag]             1.2.1      -> 1.2.1
* [new tag]             1.2.2      -> 1.2.2
* [new tag]             1.2.3      -> 1.2.3
* [new tag]             1.2.4      -> 1.2.4
* [new tag]             1.2.5      -> 1.2.5
* [new tag]             1.2.6      -> 1.2.6
* [new tag]             1.3.0      -> 1.3.0
* [new tag]             1.3.1      -> 1.3.1
* [new tag]             1.3.2      -> 1.3.2
* [new tag]             1.3.3      -> 1.3.3
* [new tag]             1.3.4      -> 1.3.4
* [new tag]             1.3.5      -> 1.3.5
* [new tag]             1.3.6      -> 1.3.6
* [new tag]             1.3.7      -> 1.3.7
* [new tag]             1.3.8      -> 1.3.8
* [new tag]             1.3.9      -> 1.3.9
* [new tag]             1.4.0      -> 1.4.0
* [new tag]             1.4.1      -> 1.4.1
* [new tag]             1.4.2      -> 1.4.2
* [new tag]             1.4.3      -> 1.4.3
* [new tag]             1.5.0      -> 1.5.0
* [new tag]             1.5.1      -> 1.5.1
* [new tag]             1.5.10     -> 1.5.10
* [new tag]             1.5.11     -> 1.5.11
* [new tag]             1.5.12     -> 1.5.12
* [new tag]             1.5.13     -> 1.5.13
* [new tag]             1.5.14     -> 1.5.14
* [new tag]             1.5.2      -> 1.5.2
* [new tag]             1.5.3      -> 1.5.3
* [new tag]             1.5.4      -> 1.5.4
* [new tag]             1.5.5      -> 1.5.5
* [new tag]             1.5.6      -> 1.5.6
* [new tag]             1.5.7      -> 1.5.7
* [new tag]             1.5.8      -> 1.5.8
* [new tag]             1.5.9      -> 1.5.9
* [new tag]             1.6.0      -> 1.6.0
* [new tag]             1.6.1      -> 1.6.1
* [new tag]             1.6.10     -> 1.6.10
* [new tag]             1.6.11     -> 1.6.11
* [new tag]             1.6.12     -> 1.6.12
* [new tag]             1.6.13     -> 1.6.13
* [new tag]             1.6.14     -> 1.6.14
* [new tag]             1.6.15     -> 1.6.15
* [new tag]             1.6.16     -> 1.6.16
* [new tag]             1.6.17     -> 1.6.17
* [new tag]             1.6.2      -> 1.6.2
* [new tag]             1.6.3      -> 1.6.3
* [new tag]             1.6.4      -> 1.6.4
* [new tag]             1.6.5      -> 1.6.5
* [new tag]             1.6.6      -> 1.6.6
* [new tag]             1.6.7      -> 1.6.7
* [new tag]             1.6.8      -> 1.6.8
* [new tag]             1.6.9      -> 1.6.9
* [new tag]             1.7.0      -> 1.7.0
* [new tag]             1.7.1      -> 1.7.1
* [new tag]             1.7.2      -> 1.7.2
* [new tag]             1.7.3      -> 1.7.3
* [new tag]             1.7.4      -> 1.7.4
* [new tag]             1.7.5      -> 1.7.5
* [new tag]             1.7.6      -> 1.7.6
* [new tag]             1.7.7      -> 1.7.7
* [new tag]             1.8.0      -> 1.8.0
* [new tag]             1.8.1      -> 1.8.1
* [new tag]             1.8.2      -> 1.8.2
* [new tag]             1.8.3      -> 1.8.3
* [new tag]             1.8.4      -> 1.8.4
* [new tag]             1.8.5      -> 1.8.5
* [new tag]             1.8.6      -> 1.8.6
* [new tag]             1.9.0      -> 1.9.0
* [new tag]             1.9.1      -> 1.9.1
* [new tag]             1.9.2      -> 1.9.2
* [new tag]             1.9.3      -> 1.9.3
* [new tag]             2.0.0      -> 2.0.0
* [new tag]             2.0.1      -> 2.0.1
* [new tag]             2.0.2      -> 2.0.2
* [new tag]             2.0.3      -> 2.0.3
* [new tag]             2.0.4      -> 2.0.4
* [new tag]             2.0.5      -> 2.0.5
* [new tag]             2.0.6      -> 2.0.6
* [new tag]             2.1.0      -> 2.1.0
* [new tag]             2.1.1      -> 2.1.1
* [new tag]             2.1.10     -> 2.1.10
* [new tag]             2.1.11     -> 2.1.11
* [new tag]             2.1.12     -> 2.1.12
* [new tag]             2.1.13     -> 2.1.13
* [new tag]             2.1.14     -> 2.1.14
* [new tag]             2.1.15     -> 2.1.15
* [new tag]             2.1.16     -> 2.1.16
* [new tag]             2.1.2      -> 2.1.2
* [new tag]             2.1.3      -> 2.1.3
* [new tag]             2.1.4      -> 2.1.4
* [new tag]             2.1.5      -> 2.1.5
* [new tag]             2.1.6      -> 2.1.6
* [new tag]             2.1.7      -> 2.1.7
* [new tag]             2.1.8      -> 2.1.8
* [new tag]             2.1.9      -> 2.1.9
* [new tag]             2.2.0      -> 2.2.0
* [new tag]             2.2.1      -> 2.2.1
* [new tag]             2.2.10     -> 2.2.10
* [new tag]             2.2.11     -> 2.2.11
* [new tag]             2.2.12     -> 2.2.12
* [new tag]             2.2.13     -> 2.2.13
* [new tag]             2.2.14     -> 2.2.14
* [new tag]             2.2.15     -> 2.2.15
* [new tag]             2.2.16     -> 2.2.16
* [new tag]             2.2.17     -> 2.2.17
* [new tag]             2.2.2      -> 2.2.2
* [new tag]             2.2.3      -> 2.2.3
* [new tag]             2.2.4      -> 2.2.4
* [new tag]             2.2.5      -> 2.2.5
* [new tag]             2.2.6      -> 2.2.6
* [new tag]             2.2.7      -> 2.2.7
* [new tag]             2.2.8      -> 2.2.8
* [new tag]             2.2.9      -> 2.2.9
* [new tag]             2.3.0      -> 2.3.0
* [new tag]             2.4.0      -> 2.4.0
* [new tag]             2.4.1      -> 2.4.1
* [new tag]             2.4.10     -> 2.4.10
* [new tag]             2.4.11     -> 2.4.11
* [new tag]             2.4.12     -> 2.4.12
* [new tag]             2.4.13     -> 2.4.13
* [new tag]             2.4.14     -> 2.4.14
* [new tag]             2.4.15     -> 2.4.15
* [new tag]             2.4.16     -> 2.4.16
* [new tag]             2.4.2      -> 2.4.2
* [new tag]             2.4.3      -> 2.4.3
* [new tag]             2.4.4      -> 2.4.4
* [new tag]             2.4.5      -> 2.4.5
* [new tag]             2.4.6      -> 2.4.6
* [new tag]             2.4.7      -> 2.4.7
* [new tag]             2.4.8      -> 2.4.8
* [new tag]             2.4.9      -> 2.4.9
* [new tag]             2.5.0      -> 2.5.0
* [new tag]             2.5.1      -> 2.5.1
* [new tag]             2.5.10     -> 2.5.10
* [new tag]             2.5.11     -> 2.5.11
* [new tag]             2.5.12     -> 2.5.12
* [new tag]             2.5.2      -> 2.5.2
* [new tag]             2.5.3      -> 2.5.3
* [new tag]             2.5.4      -> 2.5.4
* [new tag]             2.5.5      -> 2.5.5
* [new tag]             2.5.6      -> 2.5.6
* [new tag]             2.5.7      -> 2.5.7
* [new tag]             2.5.8      -> 2.5.8
* [new tag]             2.5.9      -> 2.5.9
* [new tag]             2.6.0      -> 2.6.0
* [new tag]             2.6.1      -> 2.6.1
* [new tag]             2.6.2      -> 2.6.2
* [new tag]             2.7.0      -> 2.7.0
* [new tag]             2.7.1      -> 2.7.1
* [new tag]             2.7.2      -> 2.7.2
* [new tag]             2.7.3      -> 2.7.3
* [new tag]             2.7.4      -> 2.7.4
* [new tag]             2.7.5      -> 2.7.5
* [new tag]             2.7.6      -> 2.7.6
* [new tag]             2.7.7      -> 2.7.7
* [new tag]             3.0.0      -> 3.0.0
* [new tag]             3.0.1      -> 3.0.1
* [new tag]             3.0.10     -> 3.0.10
* [new tag]             3.0.11     -> 3.0.11
* [new tag]             3.0.2      -> 3.0.2
* [new tag]             3.0.3      -> 3.0.3
* [new tag]             3.0.4      -> 3.0.4
* [new tag]             3.0.5      -> 3.0.5
* [new tag]             3.0.6      -> 3.0.6
* [new tag]             3.0.7      -> 3.0.7
* [new tag]             3.0.8      -> 3.0.8
* [new tag]             3.0.9      -> 3.0.9
* [new tag]             3.1.0      -> 3.1.0
* [new tag]             3.1.1      -> 3.1.1
* [new tag]             3.1.10     -> 3.1.10
* [new tag]             3.1.11     -> 3.1.11
* [new tag]             3.1.12     -> 3.1.12
* [new tag]             3.1.2      -> 3.1.2
* [new tag]             3.1.3      -> 3.1.3
* [new tag]             3.1.4      -> 3.1.4
* [new tag]             3.1.5      -> 3.1.5
* [new tag]             3.1.6      -> 3.1.6
* [new tag]             3.1.7      -> 3.1.7
* [new tag]             3.1.8      -> 3.1.8
* [new tag]             3.1.9      -> 3.1.9
* [new tag]             3.2.0      -> 3.2.0
* [new tag]             3.2.1      -> 3.2.1
* [new tag]             3.2.10     -> 3.2.10
* [new tag]             3.2.11     -> 3.2.11
* [new tag]             3.2.12     -> 3.2.12
* [new tag]             3.2.13     -> 3.2.13
* [new tag]             3.2.14     -> 3.2.14
* [new tag]             3.2.15     -> 3.2.15
* [new tag]             3.2.16     -> 3.2.16
* [new tag]             3.2.17     -> 3.2.17
* [new tag]             3.2.2      -> 3.2.2
* [new tag]             3.2.3      -> 3.2.3
* [new tag]             3.2.4      -> 3.2.4
* [new tag]             3.2.5      -> 3.2.5
* [new tag]             3.2.6      -> 3.2.6
* [new tag]             3.2.7      -> 3.2.7
* [new tag]             3.2.8      -> 3.2.8
* [new tag]             3.2.9      -> 3.2.9
* [new tag]             3.3.0      -> 3.3.0
* [new tag]             3.3.1      -> 3.3.1
* [new tag]             3.3.10     -> 3.3.10
* [new tag]             3.3.11     -> 3.3.11
* [new tag]             3.3.12     -> 3.3.12
* [new tag]             3.3.13     -> 3.3.13
* [new tag]             3.3.14     -> 3.3.14
* [new tag]             3.3.15     -> 3.3.15
* [new tag]             3.3.16     -> 3.3.16
* [new tag]             3.3.2      -> 3.3.2
* [new tag]             3.3.3      -> 3.3.3
* [new tag]             3.3.4      -> 3.3.4
* [new tag]             3.3.5      -> 3.3.5
* [new tag]             3.3.6      -> 3.3.6
* [new tag]             3.3.7      -> 3.3.7
* [new tag]             3.3.8      -> 3.3.8
* [new tag]             3.3.9      -> 3.3.9
* [new tag]             3.4.0      -> 3.4.0
* [new tag]             3.4.1      -> 3.4.1
* [new tag]             3.4.10     -> 3.4.10
* [new tag]             3.4.11     -> 3.4.11
* [new tag]             3.4.2      -> 3.4.2
* [new tag]             3.4.3      -> 3.4.3
* [new tag]             3.4.4      -> 3.4.4
* [new tag]             3.4.5      -> 3.4.5
* [new tag]             3.4.6      -> 3.4.6
* [new tag]             3.4.7      -> 3.4.7
* [new tag]             3.4.8      -> 3.4.8
* [new tag]             3.4.9      -> 3.4.9
* [new tag]             3.5.0      -> 3.5.0
* [new tag]             3.5.1      -> 3.5.1
* [new tag]             3.5.10     -> 3.5.10
* [new tag]             3.5.2      -> 3.5.2
* [new tag]             3.5.3      -> 3.5.3
* [new tag]             3.5.4      -> 3.5.4
* [new tag]             3.5.5      -> 3.5.5
* [new tag]             3.5.6      -> 3.5.6
* [new tag]             3.5.7      -> 3.5.7
* [new tag]             3.5.8      -> 3.5.8
* [new tag]             3.5.9      -> 3.5.9
* [new tag]             3.6.0      -> 3.6.0
* [new tag]             3.6.1      -> 3.6.1
* [new tag]             3.6.10     -> 3.6.10
* [new tag]             3.6.11     -> 3.6.11
* [new tag]             3.6.12     -> 3.6.12
* [new tag]             3.6.13     -> 3.6.13
* [new tag]             3.6.14     -> 3.6.14
* [new tag]             3.6.15     -> 3.6.15
* [new tag]             3.6.16     -> 3.6.16
* [new tag]             3.6.17     -> 3.6.17
* [new tag]             3.6.18     -> 3.6.18
* [new tag]             3.6.19     -> 3.6.19
* [new tag]             3.6.2      -> 3.6.2
* [new tag]             3.6.20     -> 3.6.20
* [new tag]             3.6.21     -> 3.6.21
* [new tag]             3.6.3      -> 3.6.3
* [new tag]             3.6.4      -> 3.6.4
* [new tag]             3.6.5      -> 3.6.5
* [new tag]             3.6.6      -> 3.6.6
* [new tag]             3.6.7      -> 3.6.7
* [new tag]             3.6.8      -> 3.6.8
* [new tag]             3.6.9      -> 3.6.9
* [new tag]             4.0.0      -> 4.0.0
* [new tag]             4.0.1      -> 4.0.1
* [new tag]             4.0.10     -> 4.0.10
* [new tag]             4.0.11     -> 4.0.11
* [new tag]             4.0.12     -> 4.0.12
* [new tag]             4.0.13     -> 4.0.13
* [new tag]             4.0.14     -> 4.0.14
* [new tag]             4.0.15     -> 4.0.15
* [new tag]             4.0.16     -> 4.0.16
* [new tag]             4.0.17     -> 4.0.17
* [new tag]             4.0.18     -> 4.0.18
* [new tag]             4.0.19     -> 4.0.19
* [new tag]             4.0.2      -> 4.0.2
* [new tag]             4.0.20     -> 4.0.20
* [new tag]             4.0.21     -> 4.0.21
* [new tag]             4.0.22     -> 4.0.22
* [new tag]             4.0.23     -> 4.0.23
* [new tag]             4.0.24     -> 4.0.24
* [new tag]             4.0.3      -> 4.0.3
* [new tag]             4.0.4      -> 4.0.4
* [new tag]             4.0.5      -> 4.0.5
* [new tag]             4.0.6      -> 4.0.6
* [new tag]             4.0.7      -> 4.0.7
* [new tag]             4.0.8      -> 4.0.8
* [new tag]             4.0.9      -> 4.0.9
HEAD is now at 5bf89a3d2 Merge pull request #15585 from reitermarkus/cloudflare-header-check
==> Downloading https://ghcr.io/v2/homebrew/portable-ruby/portable-ruby/blobs/sha256:905b0c3896164ae8067a22fff2fd0b80b16d3c8bb72441403eedf69da71ec717
######################################################################### 100.0%
==> Pouring portable-ruby-2.6.10_1.arm64_big_sur.bottle.tar.gz
Warning: /opt/homebrew/bin is not in your PATH.
Instructions on how to configure your shell for Homebrew
can be found in the 'Next steps' section below.
==> Installation successful!

==> Homebrew has enabled anonymous aggregate formulae and cask analytics.
Read the analytics documentation (and how to opt-out) here:
https://docs.brew.sh/Analytics
No analytics data has been sent yet (nor will any be during this install run).

==> Homebrew is run entirely by unpaid volunteers. Please consider donating:
https://github.com/Homebrew/brew#donations

==> Next steps:
- Run these two commands in your terminal to add Homebrew to your PATH:
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/kinneko/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
- Run brew help to get started
- Further documentation:
https://docs.brew.sh

zshに環境変数をセット。

% (echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/kinneko/.zprofile
% cat ~/.zprofile

eval "$(/opt/homebrew/bin/brew shellenv)"

% eval "$(/opt/homebrew/bin/brew shellenv)"
% brew --version
Homebrew 4.0.24

scrcpyの動作にはadbが必要になる。adbって、Android Studioのセットで自動で入らないんだっけ？ ないみたいなので入れる。

% brew install android-platform-tools
==> Downloading https://formulae.brew.sh/api/cask.jws.json

==> Downloading https://dl.google.com/android/repository/platform-tools_r34.0.3-
######################################################################### 100.0%
==> Installing Cask android-platform-tools
==> Linking Binary 'adb' to '/opt/homebrew/bin/adb'
==> Linking Binary 'dmtracedump' to '/opt/homebrew/bin/dmtracedump'
==> Linking Binary 'etc1tool' to '/opt/homebrew/bin/etc1tool'
==> Linking Binary 'fastboot' to '/opt/homebrew/bin/fastboot'
==> Linking Binary 'hprof-conv' to '/opt/homebrew/bin/hprof-conv'
==> Linking Binary 'make_f2fs' to '/opt/homebrew/bin/make_f2fs'
==> Linking Binary 'make_f2fs_casefold' to '/opt/homebrew/bin/make_f2fs_casefold
==> Linking Binary 'mke2fs' to '/opt/homebrew/bin/mke2fs'
🍺  android-platform-tools was successfully installed!

んで、本命のscrcpyをインストール。芋づる式に依存関係のライブラリが入って死ぬ。そういう世界になっているのだけど、これってたぶん、そのうちなんか問題出るよなぁ...

% brew install scrcpy
==> Downloading https://formulae.brew.sh/api/formula.jws.json
##O#- #
==> Fetching dependencies for scrcpy: brotli, giflib, highway, imath, jpeg-turbo, libpng, xz, lz4, zstd, libtiff, little-cms2, openexr, webp, jpeg-xl, libvmaf, aom, aribb24, dav1d, freetype, fontconfig, frei0r, ca-certificates, gmp, libunistring, gettext, libidn2, libtasn1, nettle, p11-kit, openssl@1.1, libevent, libnghttp2, unbound, gnutls, lame, fribidi, pcre2, glib, xorgproto, libxau, libxdmcp, libxcb, libx11, libxext, libxrender, lzo, pixman, cairo, graphite2, icu4c, harfbuzz, libunibreak, libass, libbluray, cjson, mbedtls, librist, libsoxr, libvidstab, libogg, libvorbis, libvpx, opencore-amr, openjpeg, opus, rav1e, libsamplerate, flac, mpg123, libsndfile, rubberband, sdl2, snappy, speex, srt, svt-av1, leptonica, libb2, libarchive, pango, tesseract, theora, x264, x265, xvid, libsodium, zeromq, zimg, ffmpeg and libusb
==> Fetching brotli
==> Downloading https://ghcr.io/v2/homebrew/core/brotli/manifests/1.0.9
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/brotli/blobs/sha256:bcd00b6f423
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching giflib
==> Downloading https://ghcr.io/v2/homebrew/core/giflib/manifests/5.2.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/giflib/blobs/sha256:e9a78b55a43
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching highway
==> Downloading https://ghcr.io/v2/homebrew/core/highway/manifests/1.0.4
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/highway/blobs/sha256:c84a407105
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching imath
==> Downloading https://ghcr.io/v2/homebrew/core/imath/manifests/3.1.9
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/imath/blobs/sha256:8beb6dbb10be
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching jpeg-turbo
==> Downloading https://ghcr.io/v2/homebrew/core/jpeg-turbo/manifests/2.1.5.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/jpeg-turbo/blobs/sha256:9f88f50
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libpng
==> Downloading https://ghcr.io/v2/homebrew/core/libpng/manifests/1.6.40
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libpng/blobs/sha256:bd0c0853926
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching xz
==> Downloading https://ghcr.io/v2/homebrew/core/xz/manifests/5.4.3
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/xz/blobs/sha256:f9d3283059582bf
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching lz4
==> Downloading https://ghcr.io/v2/homebrew/core/lz4/manifests/1.9.4
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/lz4/blobs/sha256:8cf59a354786ad
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching zstd
==> Downloading https://ghcr.io/v2/homebrew/core/zstd/manifests/1.5.5
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/zstd/blobs/sha256:faf929cf92dad
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libtiff
==> Downloading https://ghcr.io/v2/homebrew/core/libtiff/manifests/4.5.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libtiff/blobs/sha256:760ba83767
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching little-cms2
==> Downloading https://ghcr.io/v2/homebrew/core/little-cms2/manifests/2.15
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/little-cms2/blobs/sha256:64597b
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching openexr
==> Downloading https://ghcr.io/v2/homebrew/core/openexr/manifests/3.1.8_1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/openexr/blobs/sha256:b132db1b52
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching webp
==> Downloading https://ghcr.io/v2/homebrew/core/webp/manifests/1.3.0_1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/webp/blobs/sha256:e694b99161c42
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching jpeg-xl
==> Downloading https://ghcr.io/v2/homebrew/core/jpeg-xl/manifests/0.8.2
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/jpeg-xl/blobs/sha256:fb0e98c304
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libvmaf
==> Downloading https://ghcr.io/v2/homebrew/core/libvmaf/manifests/2.3.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libvmaf/blobs/sha256:76b4b46c07
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching aom
==> Downloading https://ghcr.io/v2/homebrew/core/aom/manifests/3.6.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/aom/blobs/sha256:05e2be27ea35bb
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching aribb24
==> Downloading https://ghcr.io/v2/homebrew/core/aribb24/manifests/1.0.4
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/aribb24/blobs/sha256:14ac368a22
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching dav1d
==> Downloading https://ghcr.io/v2/homebrew/core/dav1d/manifests/1.2.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/dav1d/blobs/sha256:2d039d7cc3ed
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching freetype
==> Downloading https://ghcr.io/v2/homebrew/core/freetype/manifests/2.13.0_1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/freetype/blobs/sha256:2d2bcd370
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching fontconfig
==> Downloading https://ghcr.io/v2/homebrew/core/fontconfig/manifests/2.14.2
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/fontconfig/blobs/sha256:5fea615
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching frei0r
==> Downloading https://ghcr.io/v2/homebrew/core/frei0r/manifests/1.8.0
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/frei0r/blobs/sha256:c45ba867a2c
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching ca-certificates
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/manifests/2023-
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/blobs/sha256:f6
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching gmp
==> Downloading https://ghcr.io/v2/homebrew/core/gmp/manifests/6.2.1_1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/gmp/blobs/sha256:491220f1ff2c66
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libunistring
==> Downloading https://ghcr.io/v2/homebrew/core/libunistring/manifests/1.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libunistring/blobs/sha256:91c48
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching gettext
==> Downloading https://ghcr.io/v2/homebrew/core/gettext/manifests/0.21.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/gettext/blobs/sha256:90da957f7b
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libidn2
==> Downloading https://ghcr.io/v2/homebrew/core/libidn2/manifests/2.3.4_1-1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libidn2/blobs/sha256:e6c723cf6d
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libtasn1
==> Downloading https://ghcr.io/v2/homebrew/core/libtasn1/manifests/4.19.0
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libtasn1/blobs/sha256:19c6df6ba
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching nettle
==> Downloading https://ghcr.io/v2/homebrew/core/nettle/manifests/3.9.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/nettle/blobs/sha256:0b2001b44f4
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching p11-kit
==> Downloading https://ghcr.io/v2/homebrew/core/p11-kit/manifests/0.24.1_1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/p11-kit/blobs/sha256:df412a2d8b
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching openssl@1.1
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/manifests/1.1.1u
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/blobs/sha256:75fa14
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libevent
==> Downloading https://ghcr.io/v2/homebrew/core/libevent/manifests/2.1.12
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libevent/blobs/sha256:53ca41440
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libnghttp2
==> Downloading https://ghcr.io/v2/homebrew/core/libnghttp2/manifests/1.54.0
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libnghttp2/blobs/sha256:b6adaa1
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching unbound
==> Downloading https://ghcr.io/v2/homebrew/core/unbound/manifests/1.17.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/unbound/blobs/sha256:fee17cf7d5
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching gnutls
==> Downloading https://ghcr.io/v2/homebrew/core/gnutls/manifests/3.8.0
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/gnutls/blobs/sha256:d21c45d81ba
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching lame
==> Downloading https://ghcr.io/v2/homebrew/core/lame/manifests/3.100
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/lame/blobs/sha256:2ff2c6ad3cfd2
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching fribidi
==> Downloading https://ghcr.io/v2/homebrew/core/fribidi/manifests/1.0.13
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/fribidi/blobs/sha256:d7c97dc2da
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching pcre2
==> Downloading https://ghcr.io/v2/homebrew/core/pcre2/manifests/10.42
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/pcre2/blobs/sha256:69483f445671
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching glib
==> Downloading https://ghcr.io/v2/homebrew/core/glib/manifests/2.76.3
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/glib/blobs/sha256:bcb6039c3186a
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching xorgproto
==> Downloading https://ghcr.io/v2/homebrew/core/xorgproto/manifests/2023.2
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/xorgproto/blobs/sha256:de818c35
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libxau
==> Downloading https://ghcr.io/v2/homebrew/core/libxau/manifests/1.0.11
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libxau/blobs/sha256:1bd9a72f005
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libxdmcp
==> Downloading https://ghcr.io/v2/homebrew/core/libxdmcp/manifests/1.1.4
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libxdmcp/blobs/sha256:3846fc5ce
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libxcb
==> Downloading https://ghcr.io/v2/homebrew/core/libxcb/manifests/1.15_1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libxcb/blobs/sha256:42b2a0a1eee
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libx11
==> Downloading https://ghcr.io/v2/homebrew/core/libx11/manifests/1.8.4
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libx11/blobs/sha256:91e5e9c3b7b
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libxext
==> Downloading https://ghcr.io/v2/homebrew/core/libxext/manifests/1.3.5
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libxext/blobs/sha256:232f1d192c
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libxrender
==> Downloading https://ghcr.io/v2/homebrew/core/libxrender/manifests/0.9.11
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libxrender/blobs/sha256:2ed6a16
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching lzo
==> Downloading https://ghcr.io/v2/homebrew/core/lzo/manifests/2.10
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/lzo/blobs/sha256:76d0933f626d8a
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching pixman
==> Downloading https://ghcr.io/v2/homebrew/core/pixman/manifests/0.42.2-1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/pixman/blobs/sha256:999830935fa
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching cairo
==> Downloading https://ghcr.io/v2/homebrew/core/cairo/manifests/1.16.0_5
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/cairo/blobs/sha256:2fc4da602916
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching graphite2
==> Downloading https://ghcr.io/v2/homebrew/core/graphite2/manifests/1.3.14
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/graphite2/blobs/sha256:544e2c34
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching icu4c
==> Downloading https://ghcr.io/v2/homebrew/core/icu4c/manifests/73.2
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/icu4c/blobs/sha256:d51cb68a1292
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching harfbuzz
==> Downloading https://ghcr.io/v2/homebrew/core/harfbuzz/manifests/7.3.0_1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/harfbuzz/blobs/sha256:5374fcd43
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libunibreak
==> Downloading https://ghcr.io/v2/homebrew/core/libunibreak/manifests/5.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libunibreak/blobs/sha256:8d491d
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libass
==> Downloading https://ghcr.io/v2/homebrew/core/libass/manifests/0.17.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libass/blobs/sha256:0ba42a7412c
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libbluray
==> Downloading https://ghcr.io/v2/homebrew/core/libbluray/manifests/1.3.4
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libbluray/blobs/sha256:b321152d
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching cjson
==> Downloading https://ghcr.io/v2/homebrew/core/cjson/manifests/1.7.15
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/cjson/blobs/sha256:5cee282ea9e0
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching mbedtls
==> Downloading https://ghcr.io/v2/homebrew/core/mbedtls/manifests/3.4.0
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/mbedtls/blobs/sha256:367067a0ee
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching librist
==> Downloading https://ghcr.io/v2/homebrew/core/librist/manifests/0.2.7_3
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/librist/blobs/sha256:3e891436d6
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libsoxr
==> Downloading https://ghcr.io/v2/homebrew/core/libsoxr/manifests/0.1.3-1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libsoxr/blobs/sha256:cf7ef980c9
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libvidstab
==> Downloading https://ghcr.io/v2/homebrew/core/libvidstab/manifests/1.1.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libvidstab/blobs/sha256:bca6a78
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libogg
==> Downloading https://ghcr.io/v2/homebrew/core/libogg/manifests/1.3.5-2
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libogg/blobs/sha256:e528165137c
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libvorbis
==> Downloading https://ghcr.io/v2/homebrew/core/libvorbis/manifests/1.3.7-1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libvorbis/blobs/sha256:37bcbe57
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libvpx
==> Downloading https://ghcr.io/v2/homebrew/core/libvpx/manifests/1.13.0
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libvpx/blobs/sha256:16d6cb5c255
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching opencore-amr
==> Downloading https://ghcr.io/v2/homebrew/core/opencore-amr/manifests/0.1.6
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/opencore-amr/blobs/sha256:6dea7
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching openjpeg
==> Downloading https://ghcr.io/v2/homebrew/core/openjpeg/manifests/2.5.0_1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/openjpeg/blobs/sha256:d76df626b
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching opus
==> Downloading https://ghcr.io/v2/homebrew/core/opus/manifests/1.4
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/opus/blobs/sha256:0439a29659def
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching rav1e
==> Downloading https://ghcr.io/v2/homebrew/core/rav1e/manifests/0.6.6
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/rav1e/blobs/sha256:53745f5c67bf
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libsamplerate
==> Downloading https://ghcr.io/v2/homebrew/core/libsamplerate/manifests/0.2.2
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libsamplerate/blobs/sha256:3093
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching flac
==> Downloading https://ghcr.io/v2/homebrew/core/flac/manifests/1.4.3
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/flac/blobs/sha256:08f362bb71849
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching mpg123
==> Downloading https://ghcr.io/v2/homebrew/core/mpg123/manifests/1.31.3
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/mpg123/blobs/sha256:93f95c194f3
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libsndfile
==> Downloading https://ghcr.io/v2/homebrew/core/libsndfile/manifests/1.2.0_1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libsndfile/blobs/sha256:0cfcd4a
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching rubberband
==> Downloading https://ghcr.io/v2/homebrew/core/rubberband/manifests/3.2.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/rubberband/blobs/sha256:7e7eaf7
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching sdl2
==> Downloading https://ghcr.io/v2/homebrew/core/sdl2/manifests/2.26.5
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/sdl2/blobs/sha256:5427cf5fab57e
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching snappy
==> Downloading https://ghcr.io/v2/homebrew/core/snappy/manifests/1.1.10
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/snappy/blobs/sha256:a18f25dc10c
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching speex
==> Downloading https://ghcr.io/v2/homebrew/core/speex/manifests/1.2.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/speex/blobs/sha256:3cb6ffa6920e
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching srt
==> Downloading https://ghcr.io/v2/homebrew/core/srt/manifests/1.5.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/srt/blobs/sha256:2cf874a22d85df
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching svt-av1
==> Downloading https://ghcr.io/v2/homebrew/core/svt-av1/manifests/1.6.0
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/svt-av1/blobs/sha256:7457392076
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching leptonica
==> Downloading https://ghcr.io/v2/homebrew/core/leptonica/manifests/1.82.0_2
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/leptonica/blobs/sha256:22c92915
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libb2
==> Downloading https://ghcr.io/v2/homebrew/core/libb2/manifests/0.98.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libb2/blobs/sha256:7713b483f347
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libarchive
==> Downloading https://ghcr.io/v2/homebrew/core/libarchive/manifests/3.6.2_1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libarchive/blobs/sha256:255b8c7
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching pango
==> Downloading https://ghcr.io/v2/homebrew/core/pango/manifests/1.50.14
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/pango/blobs/sha256:34d3bddaee4e
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching tesseract
==> Downloading https://ghcr.io/v2/homebrew/core/tesseract/manifests/5.3.1_1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/tesseract/blobs/sha256:92c508f2
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching theora
==> Downloading https://ghcr.io/v2/homebrew/core/theora/manifests/1.1.1-4
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/theora/blobs/sha256:1e5271cb88e
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching x264
==> Downloading https://ghcr.io/v2/homebrew/core/x264/manifests/r3095-1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/x264/blobs/sha256:f1be2560ce482
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching x265
==> Downloading https://ghcr.io/v2/homebrew/core/x265/manifests/3.5-1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/x265/blobs/sha256:adc617eed2e06
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching xvid
==> Downloading https://ghcr.io/v2/homebrew/core/xvid/manifests/1.3.7
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/xvid/blobs/sha256:8974d7b8f816f
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libsodium
==> Downloading https://ghcr.io/v2/homebrew/core/libsodium/manifests/1.0.18_1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libsodium/blobs/sha256:ab7029c5
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching zeromq
==> Downloading https://ghcr.io/v2/homebrew/core/zeromq/manifests/4.3.4
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/zeromq/blobs/sha256:eb0ee61f9c1
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching zimg
==> Downloading https://ghcr.io/v2/homebrew/core/zimg/manifests/3.0.4
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/zimg/blobs/sha256:40efe797c8196
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching ffmpeg
==> Downloading https://ghcr.io/v2/homebrew/core/ffmpeg/manifests/6.0-1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/ffmpeg/blobs/sha256:d21fa5146f6
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching libusb
==> Downloading https://ghcr.io/v2/homebrew/core/libusb/manifests/1.0.26
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libusb/blobs/sha256:d9121e56c7d
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching scrcpy
==> Downloading https://ghcr.io/v2/homebrew/core/scrcpy/manifests/2.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/scrcpy/blobs/sha256:e748d763429
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Installing dependencies for scrcpy: brotli, giflib, highway, imath, jpeg-turbo, libpng, xz, lz4, zstd, libtiff, little-cms2, openexr, webp, jpeg-xl, libvmaf, aom, aribb24, dav1d, freetype, fontconfig, frei0r, ca-certificates, gmp, libunistring, gettext, libidn2, libtasn1, nettle, p11-kit, openssl@1.1, libevent, libnghttp2, unbound, gnutls, lame, fribidi, pcre2, glib, xorgproto, libxau, libxdmcp, libxcb, libx11, libxext, libxrender, lzo, pixman, cairo, graphite2, icu4c, harfbuzz, libunibreak, libass, libbluray, cjson, mbedtls, librist, libsoxr, libvidstab, libogg, libvorbis, libvpx, opencore-amr, openjpeg, opus, rav1e, libsamplerate, flac, mpg123, libsndfile, rubberband, sdl2, snappy, speex, srt, svt-av1, leptonica, libb2, libarchive, pango, tesseract, theora, x264, x265, xvid, libsodium, zeromq, zimg, ffmpeg and libusb
==> Installing scrcpy dependency: brotli
==> Pouring brotli--1.0.9.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/brotli/1.0.9: 25 files, 2.3MB
==> Installing scrcpy dependency: giflib
==> Pouring giflib--5.2.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/giflib/5.2.1: 19 files, 621.8KB
==> Installing scrcpy dependency: highway
==> Pouring highway--1.0.4.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/highway/1.0.4: 65 files, 2.6MB
==> Installing scrcpy dependency: imath
==> Pouring imath--3.1.9.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/imath/3.1.9: 49 files, 935KB
==> Installing scrcpy dependency: jpeg-turbo
==> Pouring jpeg-turbo--2.1.5.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/jpeg-turbo/2.1.5.1: 44 files, 2.6MB
==> Installing scrcpy dependency: libpng
==> Pouring libpng--1.6.40.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libpng/1.6.40: 27 files, 1.4MB
==> Installing scrcpy dependency: xz
==> Pouring xz--5.4.3.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/xz/5.4.3: 162 files, 2.6MB
==> Installing scrcpy dependency: lz4
==> Pouring lz4--1.9.4.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/lz4/1.9.4: 22 files, 696.6KB
==> Installing scrcpy dependency: zstd
==> Pouring zstd--1.5.5.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/zstd/1.5.5: 31 files, 2.3MB
==> Installing scrcpy dependency: libtiff
==> Pouring libtiff--4.5.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libtiff/4.5.1: 473 files, 8.2MB
==> Installing scrcpy dependency: little-cms2
==> Pouring little-cms2--2.15.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/little-cms2/2.15: 21 files, 1.4MB
==> Installing scrcpy dependency: openexr
==> Pouring openexr--3.1.8_1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/openexr/3.1.8_1: 194 files, 7.9MB
==> Installing scrcpy dependency: webp
==> Pouring webp--1.3.0_1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/webp/1.3.0_1: 63 files, 2.4MB
==> Installing scrcpy dependency: jpeg-xl
==> Pouring jpeg-xl--0.8.2.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/jpeg-xl/0.8.2: 43 files, 10.5MB
==> Installing scrcpy dependency: libvmaf
==> Pouring libvmaf--2.3.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libvmaf/2.3.1: 234 files, 7MB
==> Installing scrcpy dependency: aom
==> Pouring aom--3.6.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/aom/3.6.1: 23 files, 8.6MB
==> Installing scrcpy dependency: aribb24
==> Pouring aribb24--1.0.4.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/aribb24/1.0.4: 14 files, 220.4KB
==> Installing scrcpy dependency: dav1d
==> Pouring dav1d--1.2.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/dav1d/1.2.1: 15 files, 926.1KB
==> Installing scrcpy dependency: freetype
==> Pouring freetype--2.13.0_1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/freetype/2.13.0_1: 67 files, 2.4MB
==> Installing scrcpy dependency: fontconfig
==> Pouring fontconfig--2.14.2.arm64_big_sur.bottle.tar.gz
==> Regenerating font cache, this may take a while
==> /opt/homebrew/Cellar/fontconfig/2.14.2/bin/fc-cache -frv
🍺  /opt/homebrew/Cellar/fontconfig/2.14.2: 88 files, 2.5MB
==> Installing scrcpy dependency: frei0r
==> Pouring frei0r--1.8.0.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/frei0r/1.8.0: 127 files, 6MB
==> Installing scrcpy dependency: ca-certificates
==> Pouring ca-certificates--2023-05-30.arm64_big_sur.bottle.tar.gz
==> Regenerating CA certificate bundle from keychain, this may take a while...
🍺  /opt/homebrew/Cellar/ca-certificates/2023-05-30: 3 files, 216.2KB
==> Installing scrcpy dependency: gmp
==> Pouring gmp--6.2.1_1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/gmp/6.2.1_1: 21 files, 3.3MB
==> Installing scrcpy dependency: libunistring
==> Pouring libunistring--1.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libunistring/1.1: 56 files, 4.8MB
==> Installing scrcpy dependency: gettext
==> Pouring gettext--0.21.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/gettext/0.21.1: 1,983 files, 21.2MB
==> Installing scrcpy dependency: libidn2
==> Pouring libidn2--2.3.4_1.arm64_big_sur.bottle.1.tar.gz
🍺  /opt/homebrew/Cellar/libidn2/2.3.4_1: 79 files, 1MB
==> Installing scrcpy dependency: libtasn1
==> Pouring libtasn1--4.19.0.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libtasn1/4.19.0: 61 files, 718.5KB
==> Installing scrcpy dependency: nettle
==> Pouring nettle--3.9.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/nettle/3.9.1: 95 files, 3MB
==> Installing scrcpy dependency: p11-kit
==> Pouring p11-kit--0.24.1_1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/p11-kit/0.24.1_1: 67 files, 3.9MB
==> Installing scrcpy dependency: openssl@1.1
==> Pouring openssl@1.1--1.1.1u.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/openssl@1.1/1.1.1u: 8,101 files, 18MB
==> Installing scrcpy dependency: libevent
==> Pouring libevent--2.1.12.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libevent/2.1.12: 57 files, 2.2MB
==> Installing scrcpy dependency: libnghttp2
==> Pouring libnghttp2--1.54.0.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libnghttp2/1.54.0: 13 files, 727KB
==> Installing scrcpy dependency: unbound
==> Pouring unbound--1.17.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/unbound/1.17.1: 58 files, 5.9MB
==> Installing scrcpy dependency: gnutls
==> Pouring gnutls--3.8.0.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/gnutls/3.8.0: 1,281 files, 10.7MB
==> Installing scrcpy dependency: lame
==> Pouring lame--3.100.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/lame/3.100: 27 files, 2.2MB
==> Installing scrcpy dependency: fribidi
==> Pouring fribidi--1.0.13.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/fribidi/1.0.13: 67 files, 733.8KB
==> Installing scrcpy dependency: pcre2
==> Pouring pcre2--10.42.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/pcre2/10.42: 230 files, 6.2MB
==> Installing scrcpy dependency: glib
==> Pouring glib--2.76.3.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/glib/2.76.3: 455 files, 22.3MB
==> Installing scrcpy dependency: xorgproto
==> Pouring xorgproto--2023.2.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/xorgproto/2023.2: 267 files, 3.9MB
==> Installing scrcpy dependency: libxau
==> Pouring libxau--1.0.11.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libxau/1.0.11: 21 files, 139.7KB
==> Installing scrcpy dependency: libxdmcp
==> Pouring libxdmcp--1.1.4.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libxdmcp/1.1.4: 11 files, 146.6KB
==> Installing scrcpy dependency: libxcb
==> Pouring libxcb--1.15_1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libxcb/1.15_1: 2,461 files, 7.4MB
==> Installing scrcpy dependency: libx11
==> Pouring libx11--1.8.4.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libx11/1.8.4: 1,054 files, 7.1MB
==> Installing scrcpy dependency: libxext
==> Pouring libxext--1.3.5.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libxext/1.3.5: 87 files, 446.2KB
==> Installing scrcpy dependency: libxrender
==> Pouring libxrender--0.9.11.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libxrender/0.9.11: 12 files, 214KB
==> Installing scrcpy dependency: lzo
==> Pouring lzo--2.10.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/lzo/2.10: 31 files, 580.4KB
==> Installing scrcpy dependency: pixman
==> Pouring pixman--0.42.2.arm64_big_sur.bottle.1.tar.gz
🍺  /opt/homebrew/Cellar/pixman/0.42.2: 11 files, 1.2MB
==> Installing scrcpy dependency: cairo
==> Pouring cairo--1.16.0_5.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/cairo/1.16.0_5: 126 files, 6.4MB
==> Installing scrcpy dependency: graphite2
==> Pouring graphite2--1.3.14.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/graphite2/1.3.14: 18 files, 312.9KB
==> Installing scrcpy dependency: icu4c
==> Pouring icu4c--73.2.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/icu4c/73.2: 268 files, 80.3MB
==> Installing scrcpy dependency: harfbuzz
==> Pouring harfbuzz--7.3.0_1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/harfbuzz/7.3.0_1: 76 files, 9.3MB
==> Installing scrcpy dependency: libunibreak
==> Pouring libunibreak--5.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libunibreak/5.1: 17 files, 344.9KB
==> Installing scrcpy dependency: libass
==> Pouring libass--0.17.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libass/0.17.1: 11 files, 532.4KB
==> Installing scrcpy dependency: libbluray
==> Pouring libbluray--1.3.4.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libbluray/1.3.4: 21 files, 1.1MB
==> Installing scrcpy dependency: cjson
==> Pouring cjson--1.7.15.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/cjson/1.7.15: 23 files, 282.6KB
==> Installing scrcpy dependency: mbedtls
==> Pouring mbedtls--3.4.0.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/mbedtls/3.4.0: 160 files, 12.0MB
==> Installing scrcpy dependency: librist
==> Pouring librist--0.2.7_3.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/librist/0.2.7_3: 28 files, 802.9KB
==> Installing scrcpy dependency: libsoxr
==> Pouring libsoxr--0.1.3.arm64_big_sur.bottle.1.tar.gz
🍺  /opt/homebrew/Cellar/libsoxr/0.1.3: 29 files, 340KB
==> Installing scrcpy dependency: libvidstab
==> Pouring libvidstab--1.1.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libvidstab/1.1.1: 25 files, 187.9KB
==> Installing scrcpy dependency: libogg
==> Pouring libogg--1.3.5.arm64_big_sur.bottle.2.tar.gz
🍺  /opt/homebrew/Cellar/libogg/1.3.5: 103 files, 552.9KB
==> Installing scrcpy dependency: libvorbis
==> Pouring libvorbis--1.3.7.arm64_big_sur.bottle.1.tar.gz
🍺  /opt/homebrew/Cellar/libvorbis/1.3.7: 157 files, 2.4MB
==> Installing scrcpy dependency: libvpx
==> Pouring libvpx--1.13.0.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libvpx/1.13.0: 20 files, 3.8MB
==> Installing scrcpy dependency: opencore-amr
==> Pouring opencore-amr--0.1.6.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/opencore-amr/0.1.6: 17 files, 689.4KB
==> Installing scrcpy dependency: openjpeg
==> Pouring openjpeg--2.5.0_1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/openjpeg/2.5.0_1: 536 files, 13.8MB
==> Installing scrcpy dependency: opus
==> Pouring opus--1.4.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/opus/1.4: 15 files, 996.5KB
==> Installing scrcpy dependency: rav1e
==> Pouring rav1e--0.6.6.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/rav1e/0.6.6: 14 files, 140.5MB
==> Installing scrcpy dependency: libsamplerate
==> Pouring libsamplerate--0.2.2.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libsamplerate/0.2.2: 32 files, 3MB
==> Installing scrcpy dependency: flac
==> Pouring flac--1.4.3.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/flac/1.4.3: 284 files, 6.9MB
==> Installing scrcpy dependency: mpg123
==> Pouring mpg123--1.31.3.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/mpg123/1.31.3: 33 files, 2.0MB
==> Installing scrcpy dependency: libsndfile
==> Pouring libsndfile--1.2.0_1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libsndfile/1.2.0_1: 53 files, 1.2MB
==> Installing scrcpy dependency: rubberband
==> Pouring rubberband--3.2.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/rubberband/3.2.1: 13 files, 1.7MB
==> Installing scrcpy dependency: sdl2
==> Pouring sdl2--2.26.5.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/sdl2/2.26.5: 93 files, 6.4MB
==> Installing scrcpy dependency: snappy
==> Pouring snappy--1.1.10.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/snappy/1.1.10: 18 files, 180.5KB
==> Installing scrcpy dependency: speex
==> Pouring speex--1.2.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/speex/1.2.1: 25 files, 904.4KB
==> Installing scrcpy dependency: srt
==> Pouring srt--1.5.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/srt/1.5.1: 20 files, 4.4MB
==> Installing scrcpy dependency: svt-av1
==> Pouring svt-av1--1.6.0.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/svt-av1/1.6.0: 24 files, 3.5MB
==> Installing scrcpy dependency: leptonica
==> Pouring leptonica--1.82.0_2.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/leptonica/1.82.0_2: 53 files, 6.9MB
==> Installing scrcpy dependency: libb2
==> Pouring libb2--0.98.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libb2/0.98.1: 8 files, 126.8KB
==> Installing scrcpy dependency: libarchive
==> Pouring libarchive--3.6.2_1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libarchive/3.6.2_1: 62 files, 3.7MB
==> Installing scrcpy dependency: pango
==> Pouring pango--1.50.14.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/pango/1.50.14: 68 files, 3.4MB
==> Installing scrcpy dependency: tesseract
==> Pouring tesseract--5.3.1_1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/tesseract/5.3.1_1: 73 files, 32.6MB
==> Installing scrcpy dependency: theora
==> Pouring theora--1.1.1.arm64_big_sur.bottle.4.tar.gz
🍺  /opt/homebrew/Cellar/theora/1.1.1: 97 files, 2.1MB
==> Installing scrcpy dependency: x264
==> Pouring x264--r3095.arm64_big_sur.bottle.1.tar.gz
🍺  /opt/homebrew/Cellar/x264/r3095: 11 files, 4.2MB
==> Installing scrcpy dependency: x265
==> Pouring x265--3.5.arm64_big_sur.bottle.1.tar.gz
🍺  /opt/homebrew/Cellar/x265/3.5: 11 files, 6.7MB
==> Installing scrcpy dependency: xvid
==> Pouring xvid--1.3.7.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/xvid/1.3.7: 10 files, 1.3MB
==> Installing scrcpy dependency: libsodium
==> Pouring libsodium--1.0.18_1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libsodium/1.0.18_1: 73 files, 780.9KB
==> Installing scrcpy dependency: zeromq
==> Pouring zeromq--4.3.4.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/zeromq/4.3.4: 83 files, 6.0MB
==> Installing scrcpy dependency: zimg
==> Pouring zimg--3.0.4.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/zimg/3.0.4: 27 files, 1MB
==> Installing scrcpy dependency: ffmpeg
==> Pouring ffmpeg--6.0.arm64_big_sur.bottle.1.tar.gz
🍺  /opt/homebrew/Cellar/ffmpeg/6.0: 284 files, 50MB
==> Installing scrcpy dependency: libusb
==> Pouring libusb--1.0.26.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libusb/1.0.26: 22 files, 595.3KB
==> Installing scrcpy
==> Pouring scrcpy--2.1.arm64_big_sur.bottle.tar.gz
==> Caveats
At runtime, adb must be accessible from your PATH.

You can install adb from Homebrew Cask:
brew install --cask android-platform-tools

zsh completions have been installed to:
/opt/homebrew/share/zsh/site-functions
==> Summary
🍺  /opt/homebrew/Cellar/scrcpy/2.1: 10 files, 330.1KB
==> Running `brew cleanup scrcpy`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Caveats
==> scrcpy
At runtime, adb must be accessible from your PATH.

You can install adb from Homebrew Cask:
brew install --cask android-platform-tools

zsh completions have been installed to:
/opt/homebrew/share/zsh/site-functions

~~~

　起動する。

~~~text
% scrcpy
scrcpy 2.1 <https://github.com/Genymobile/scrcpy>
/opt/homebrew/Cellar/scrcpy/2.1/share/scrcpy/scrcpy-server: 1 file pushed, 0 skipped. 152.4 MB/s (56955 bytes in 0.000s)
[server] INFO: Device: [Google] google Pixel 6a (Android 13)
INFO: Renderer: metal
INFO: Texture: 1080x2400
~~~

　ワンテンポ遅れて画面が表示される。２回目からは高速に起動する。画面のタッチ操作も普通にできる。

![](/2023-07-10/6221599-02.png)

　QRコード画面もちゃんと出てくる。

![](/2023-07-10/6221599-03.png)

　キーボードショートカットでの操作、オーディオの転送、録画、クリップボード転送、ファイルのD&Dでのコピーなどの機能もあるようだけど、いまのところ、そこまではいらないかな。

---
> オリジナル投稿：<br>
> macOSにAndroidターゲットの画面を表示する｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/6221599>

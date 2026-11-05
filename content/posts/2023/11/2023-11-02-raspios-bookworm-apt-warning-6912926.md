+++
date = "2023-11-02T08:00:00"
draft = false
title = "RaspiOS bookwormでaptの警告を消す"
description = "Raspberry Pi OS bookwormのapt警告を調べ、署名鍵の移行を試した記録。"

[taxonomies]
tags = ["Raspberry Pi", "Raspberry Pi OS", "Linux", "2023-11"]
+++
　bookwormをインストールしてapt-get updateコマンドを実行したらエラーになった。

```text
kinneko@raspberrypi:~ $ sudo apt-get update
Get:1 http://archive.raspberrypi.com/debian bookworm InRelease [23.6 kB]
Hit:2 http://raspbian.raspberrypi.com/raspbian bookworm InRelease
Get:3 http://archive.raspberrypi.com/debian bookworm/main arm64 Packages [337 kB]
Get:4 http://archive.raspberrypi.com/debian bookworm/main armhf Packages [344 kB]
Fetched 704 kB in 6s (123 kB/s)
Reading package lists... Done
N: Repository 'http://archive.raspberrypi.com/debian bookworm InRelease' changed its 'Suite' value from 'testing' to 'stable'
W: http://raspbian.raspberrypi.com/raspbian/dists/bookworm/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
```

　Nのほうは、リポジトリのSuite値がtestingからstableに変更されたことを通知している。リリースサイクルの中では普通に起きることなのだけど、リリース後なのにこれが出るのはイメージを作成した人がヒドいという感じ。updateを再実行するとクリアされる。

```text
N: Repository 'http://archive.raspberrypi.com/debian bookworm InRelease' changed its 'Suite' value from 'testing' to 'stable'
```

　再実行したらNのほうは消えた。

```text
kinneko@raspberrypi:~ $ sudo apt-get update
Hit:1 http://raspbian.raspberrypi.com/raspbian bookworm InRelease
Hit:2 http://archive.raspberrypi.com/debian bookworm InRelease
Reading package lists... Done
W: http://raspbian.raspberrypi.com/raspbian/dists/bookworm/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
```

　もう一個のWのほう。リポジトリのキーが古い方法で保存されていて、それは今後非推奨だという警告。鍵を更新しなくてはいけない。

　このまま使っても実害はないのだけれど、実行するたびに警告が出るのは気持ち悪いので、修正しておく。

　まず、現在の鍵の状態をapt-keyコマンドで調べる。

```text
kinneko@raspberrypi:~ $ sudo apt-key list
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
/etc/apt/trusted.gpg
--------------------
pub   rsa2048 2012-04-01 [SC]
A0DA 38D0 D76E 8B5D 6388  7281 9165 938D 90FD DD2E
uid           [ unknown] Mike Thompson (Raspberry Pi Debian armhf ARMv6+VFP) <mpthompson@gmail.com>
sub   rsa2048 2012-04-01 [E]
```

```text
/etc/apt/trusted.gpg.d/raspberrypi-archive-stable.gpg
-----------------------------------------------------
pub   rsa2048 2012-06-17 [SC]
CF8A 1AF5 02A2 AA2D 763B  AE7E 82B1 2992 7FA3 303E
uid           [ unknown] Raspberry Pi Archive Signing Key
sub   rsa2048 2012-06-17 [E]
```

　apt-keyコマンドはすでに非推奨だよということで、警告が出ている。

　raspbian.raspberrypi.comのほうは、/etc/apt/trusted.gpgに鍵が置かれている。これが古い管理方式ということだろう。

　raspberrypi-archive-stable.gpgは新しい管理方式に則って、/etc/apt/trusted.gpg.d/の下に鍵が置かれている。

　解決方法は２つある。いずれの方法も推奨はされていないようだ。

　本来はサーバーから署名鍵を取得して登録するのだけど、個別にどこで配布しているのか書かれていない。Debianでは、通常はパッケージとして管理されていて、その中に含まれている。RaspiOSでは、そのような管理はされていないようだ。

　まずは、単純でちょっと汚い方法。登録されている鍵を、単純に新しい場所にコピーする。

```text
kinneko@raspberrypi:~ $ sudo cp /etc/apt/trusted.gpg /etc/apt/trusted.gpg.d
```

　apt-get updateを実行しても、エラー表示は出なくなる。

```text
kinneko@raspberrypi:~ $ sudo apt-get update
Hit:1 http://archive.raspberrypi.com/debian bookworm InRelease
Hit:2 http://raspbian.raspberrypi.com/raspbian bookworm InRelease
Reading package lists... Done
```

　鍵のリストには、前の鍵も表示されている。

```text
kinneko@raspberrypi:~ $ sudo apt-key list
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
/etc/apt/trusted.gpg
--------------------
pub   rsa2048 2012-04-01 [SC]
A0DA 38D0 D76E 8B5D 6388  7281 9165 938D 90FD DD2E
uid           [ unknown] Mike Thompson (Raspberry Pi Debian armhf ARMv6+VFP) <mpthompson@gmail.com>
sub   rsa2048 2012-04-01 [E]
```

```text
/etc/apt/trusted.gpg.d/raspberrypi-archive-stable.gpg
-----------------------------------------------------
pub   rsa2048 2012-06-17 [SC]
CF8A 1AF5 02A2 AA2D 763B  AE7E 82B1 2992 7FA3 303E
uid           [ unknown] Raspberry Pi Archive Signing Key
sub   rsa2048 2012-06-17 [E]
```

```text
/etc/apt/trusted.gpg.d/trusted.gpg
----------------------------------
pub   rsa2048 2012-04-01 [SC]
A0DA 38D0 D76E 8B5D 6388  7281 9165 938D 90FD DD2E
uid           [ unknown] Mike Thompson (Raspberry Pi Debian armhf ARMv6+VFP) <mpthompson@gmail.com>
sub   rsa2048 2012-04-01 [E]
```

　不要になった鍵ファイルを削除すると表示されなくなる。

```text
kinneko@raspberrypi:~ $ sudo rm /etc/apt/trusted.gpg
kinneko@raspberrypi:~ $ sudo apt-key list
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
/etc/apt/trusted.gpg.d/raspberrypi-archive-stable.gpg
-----------------------------------------------------
pub   rsa2048 2012-06-17 [SC]
CF8A 1AF5 02A2 AA2D 763B  AE7E 82B1 2992 7FA3 303E
uid           [ unknown] Raspberry Pi Archive Signing Key
sub   rsa2048 2012-06-17 [E]
```

```text
/etc/apt/trusted.gpg.d/trusted.gpg
----------------------------------
pub   rsa2048 2012-04-01 [SC]
A0DA 38D0 D76E 8B5D 6388  7281 9165 938D 90FD DD2E
uid           [ unknown] Mike Thompson (Raspberry Pi Debian armhf ARMv6+VFP) <mpthompson@gmail.com>
sub   rsa2048 2012-04-01 [E]
```

　この方法が実害がなく、一番簡単でよいと思う。ファイル名は、制約条件にはならないようなので、わかりやすいようにraspbian.gpgとかにしておくといいかもしれない。

```text
kinneko@raspberrypi:~ $ sudo mv /etc/apt/trusted.gpg.d/trusted.gpg /etc/apt/trusted.gpg.d/raspbian.gpg
```

```text
kinneko@raspberrypi:~ $ sudo apt-key list
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
/etc/apt/trusted.gpg.d/raspberrypi-archive-stable.gpg
-----------------------------------------------------
pub   rsa2048 2012-06-17 [SC]
CF8A 1AF5 02A2 AA2D 763B  AE7E 82B1 2992 7FA3 303E
uid           [ unknown] Raspberry Pi Archive Signing Key
sub   rsa2048 2012-06-17 [E]
```

```text
/etc/apt/trusted.gpg.d/raspbian.gpg
-----------------------------------
pub   rsa2048 2012-04-01 [SC]
A0DA 38D0 D76E 8B5D 6388  7281 9165 938D 90FD DD2E
uid           [ unknown] Mike Thompson (Raspberry Pi Debian armhf ARMv6+VFP) <mpthompson@gmail.com>
sub   rsa2048 2012-04-01 [E]
```

　２つ目は、今回の場合はあんまり意味のない方法。

　trusted.gpgに複数の鍵が登録されていることがあるので、そこから、必要な署名鍵だけを抽出してやるのだけど、よく見ると、この署名鍵には鍵が１つしか含まれていないので、抽出することは意味がないな... 一応のメモとして読んでほしい。

　署名鍵のハッシュの末尾の８桁を指定して抽出する。ファイル名はraspbian2.gpgとしておく。

```text
kinneko@raspberrypi:~ $ sudo apt-key export 90FDDD2E | sudo gpg --dearmour -o /etc/apt/trusted.gpg.d/raspbian2.gpg
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
```

　まぁ、今回の場合は、raspbian2.gpgもraspbian.gpgも、どっちもまったく同じものだよねw

```text
kinneko@raspberrypi:~ $ diff /etc/apt/trusted.gpg.d/raspbian.gpg /etc/apt/trusted.gpg.d/raspbian2.gpg
```

```text
kinneko@raspberrypi:~ $ file /etc/apt/trusted.gpg.d/raspbian*
/etc/apt/trusted.gpg.d/raspbian2.gpg: OpenPGP Public Key Version 4, Created Sun Apr  1 21:02:33 2012, RSA (Encrypt or Sign, 2048 bits); User ID; Signature; OpenPGP Certificate
/etc/apt/trusted.gpg.d/raspbian.gpg:  OpenPGP Public Key Version 4, Created Sun Apr  1 21:02:33 2012, RSA (Encrypt or Sign, 2048 bits); User ID; Signature; OpenPGP Certificate
```

```text
kinneko@raspberrypi:~ $ sudo apt-key list
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
/etc/apt/trusted.gpg.d/raspberrypi-archive-stable.gpg
-----------------------------------------------------
pub   rsa2048 2012-06-17 [SC]
CF8A 1AF5 02A2 AA2D 763B  AE7E 82B1 2992 7FA3 303E
uid           [ unknown] Raspberry Pi Archive Signing Key
sub   rsa2048 2012-06-17 [E]
```

```text
/etc/apt/trusted.gpg.d/raspbian2.gpg
------------------------------------
pub   rsa2048 2012-04-01 [SC]
A0DA 38D0 D76E 8B5D 6388  7281 9165 938D 90FD DD2E
uid           [ unknown] Mike Thompson (Raspberry Pi Debian armhf ARMv6+VFP) <mpthompson@gmail.com>
sub   rsa2048 2012-04-01 [E]
```

```text
/etc/apt/trusted.gpg.d/raspbian.gpg
-----------------------------------
pub   rsa2048 2012-04-01 [SC]
A0DA 38D0 D76E 8B5D 6388  7281 9165 938D 90FD DD2E
uid           [ unknown] Mike Thompson (Raspberry Pi Debian armhf ARMv6+VFP) <mpthompson@gmail.com>
sub   rsa2048 2012-04-01 [E]
```

　あっても問題はないのだけど、今回はraspbian2.gpgを削除しておく。

```text
kinneko@raspberrypi:~ $ sudo rm /etc/apt/trusted.gpg.d/raspbian2.gpg
```

　実害がないとはいえ、こんな手間はかけさせないでほしいな...

　bookwormのフィードバックスレッドには、すでに報告が上がっていた。実害がないので、たぶんRaspiOSのアップデートでは修正されないと思われる。

> Bookworm feedback thread - Page 15 - Raspberry Pi Forums<br>
> <https://forums.raspberrypi.com/viewtopic.php?p=2145952#p2145952>

　pi-genで自分でbookwormをビルドするときには、修正しておこう。

---
> オリジナル投稿：<br>
> RaspiOS bookwormでaptの警告を消す｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/6912926>

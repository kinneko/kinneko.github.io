+++
date = "2023-02-22T08:00:00"
draft = false
title = "続報：aptでUbuntu Proの宣伝が表示されるのをやめる -2-"
description = "Ubuntu Proのapt宣伝表示を止める対策を検証する。"

[taxonomies]
tags = ["Ubuntu", "Ubuntu Pro", "apt", "2023-02"]

[extra]
image = "/2023-02-22/5330741-title.jpeg"
+++

　さて、ようやく準備が整った。(2/19)

　前回の記事でミニマイズドでインストールすると、Proの罠にかからないようだというのが判明したのは面白かった。どうしてそうなるのかは追ってない。

　ようやく追試に入れる。

　前回書いた５つの対策方法はこれ。

1. ubuntu-advantage-toolsを削除する
2. 20apt-esm-hook.confを削除して空のファイルを置く
3. 88-esm-announceを削除して空のファイルを置く
4. /var/lib/ubuntu-advantage/messages/*.tmplを削除する
5. /etc/default/motd-newsに設定があるのでENABLEDを0にする

　1は乱暴、2-4はパッケージアップデートで上書きされる可能性が高いので、オススメできない。5はデフォルトで提供される機能なので上書きされない可能性が高いという感じ。

　機能が本番適用になったようなので、検証してみる。

1. ubuntu-advantage-toolsを削除する

　これは、ubuntu-advantage-toolsがcoreパッケージの依存に関わるようになっているので、削除はできないようだ。つらい。

　しかし、ミニマイズドでインストールすると、ubuntu-advantage-toolsはインストールされない。おそらく、依存するパッケージのパッケージングが異なるものが使われているのだと思われる。こういう分裂は面倒なのだけど、この場合は、ミニマイズドからパッケージを入れてゆけば、ubuntu-advantage-toolsの依存関係を回避できる可能性があるとうことだろう。

　一応、パッケージを削除する作業をしてみる。

```text
kinneko@utm:~$ sudo apt-get remove --purge ubuntu-advantage-tools -s
[sudo] password for kinneko:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  distro-info python3-debian
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  ubuntu-advantage-tools* ubuntu-minimal* ubuntu-server* update-manager-core*
  update-notifier-common*
0 upgraded, 0 newly installed, 5 to remove and 0 not upgraded.
Purg ubuntu-server [1.497]
Purg update-notifier-common [3.192.59.2]
Purg update-manager-core [1:22.10.4]
Purg ubuntu-minimal [1.497]
Purg ubuntu-advantage-tools [27.13.5~22.10.1]
```

　update-manager-core*とupdate-notifier-common*はubuntu-advantage-tools*関連っぽい名前付け。

　update-manager-coreのほうは、今回の通知問題の元凶のスケルトン

```text
kinneko@utm:~$ dpkg -L update-manager-core
/.
/usr
/usr/bin
/usr/bin/hwe-support-status
/usr/bin/ubuntu-security-status
/usr/share
/usr/share/apport
/usr/share/apport/package-hooks
/usr/share/apport/package-hooks/source_update-manager.py
/usr/share/doc
/usr/share/doc/update-manager-core
/usr/share/doc/update-manager-core/AUTHORS
/usr/share/doc/update-manager-core/README
/usr/share/doc/update-manager-core/TODO
/usr/share/doc/update-manager-core/copyright
/var
/var/lib
/var/lib/update-manager
/var/lib/update-notifier
/usr/share/doc/update-manager-core/changelog.gz
```

　update-notifier-commonは、今回の通知問題の元凶の実態ファイル。

```text
kinneko@utm:~$ dpkg -L update-notifier-common
/.
/etc
/etc/apt
/etc/apt/apt.conf.d
/etc/apt/apt.conf.d/10periodic
/etc/apt/apt.conf.d/15update-stamp
/etc/apt/apt.conf.d/20archive
/etc/apt/apt.conf.d/99update-notifier
/etc/kernel
/etc/kernel/postinst.d
/etc/update-motd.d
/etc/update-motd.d/90-updates-available
/etc/update-motd.d/95-hwe-eol
/etc/update-motd.d/98-fsck-at-reboot
/etc/update-motd.d/98-reboot-required
/etc/update-notifier
/lib
/lib/systemd
/lib/systemd/system
/lib/systemd/system/update-notifier-download.service
/lib/systemd/system/update-notifier-download.timer
/lib/systemd/system/update-notifier-motd.service
/lib/systemd/system/update-notifier-motd.timer
/usr
/usr/lib
/usr/lib/update-notifier
/usr/lib/update-notifier/apt-cdrom-check
/usr/lib/update-notifier/apt_check.py
/usr/lib/update-notifier/backend_helper.py
/usr/lib/update-notifier/cddistupgrader
/usr/lib/update-notifier/list-oem-metapackages
/usr/lib/update-notifier/package-data-downloader
/usr/lib/update-notifier/package-system-locked
/usr/lib/update-notifier/update-motd-fsck-at-reboot
/usr/lib/update-notifier/update-motd-hwe-eol
/usr/lib/update-notifier/update-motd-reboot-required
/usr/lib/update-notifier/update-motd-updates-available
/usr/share
/usr/share/doc
/usr/share/doc/update-notifier-common
/usr/share/doc/update-notifier-common/changelog.gz
/usr/share/doc/update-notifier-common/copyright
/usr/share/locale
(locale関係は長いのでsnip)
/usr/share/package-data-downloads
/usr/share/polkit-1
/usr/share/polkit-1/actions
/usr/share/polkit-1/actions/com.ubuntu.update-notifier.policy
/usr/share/update-notifier
/usr/share/update-notifier/notify-reboot-required
/usr/share/update-notifier/notify-updates-outdated
/usr/share/update-notifier/package-data-downloads-failed
/usr/share/update-notifier/package-data-downloads-failed-permanently
/usr/share/update-notifier/plugins
/usr/share/update-notifier/plugins/cache-changed
/usr/share/update-notifier/upgrader-patches
/usr/share/update-notifier/upgrader-patches/update-manager-downloader-fix2.diff
/var
/var/lib
/var/lib/update-notifier
/var/lib/update-notifier/package-data-downloads
/var/lib/update-notifier/package-data-downloads/partial
/var/lib/update-notifier/user.d
/etc/kernel/postinst.d/update-notifier
/usr/lib/update-notifier/apt-check
```

　どちらも消えても問題なさそう。

　ubuntu-minimal* ubuntu-server*はディストリビューションの状態を定義するメタパッケージで、依存関係を定義しているだけで中身は特にないパッケージ。これに書かれた依存関係が削除をできなくするガンというわけね。

```text
kinneko@utm:~$ dpkg -L ubuntu-minimal
/.
/usr
/usr/share
/usr/share/doc
/usr/share/doc/ubuntu-minimal
/usr/share/doc/ubuntu-minimal/changelog.gz
/usr/share/doc/ubuntu-minimal/copyright
```

　依存ごと全部削除しちゃった後に、ミニマイズドに含まれるメタパッケージを入れればいいのじゃなかろうか。もしくは依存関係の定義ファイルをいじって、依存消して進めるか。

　まずは、バージョンチェック。

```text
kinneko@utm:~$ dpkg -l ubuntu-minimal*
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name           Version      Architecture Description
+++-==============-============-============-=================================
ii  ubuntu-minimal 1.497        arm64        Minimal core of Ubuntu
```

```text
kinneko@utm:~$ dpkg -l ubuntu-server*|more
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                  Version      Architecture Description
+++-=====================-============-============-============================
=====
ii  ubuntu-server         1.497        arm64        The Ubuntu Server system
ii  ubuntu-server-minimal 1.497        arm64        The Ubuntu Server minimal sy
stem
```

　依存が書かれているのの確認。

```text
kinneko@utm:~$ apt-cache depends ubuntu-minimal| grep ubuntu-advantage-tools
  Depends: ubuntu-advantage-tools
```

　おや、こっちには依存関係の記述はないな？ 芋づるで他のパッケージの依存かな？

```text
kinneko@utm:~$ apt-cache depends ubuntu-server| grep ubuntu-advantage-tools
kinneko@utm:~$ apt-cache depends ubuntu-server-minimal| grep ubuntu-advantage-tools
```

　影響はなさそうなので、ubuntu-minimalの依存ファイルを直接書き換えてみる。

```text
kinneko@utm:~$ sudo vi /var/lib/dpkg/status
Package: ubuntu-minimal
Status: install ok installed
Priority: optional
Section: metapackages
Installed-Size: 54
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: arm64
Source: ubuntu-meta
Version: 1.497
Depends: adduser, apt, apt-utils, console-setup, debconf, debconf-i18n, e2fsprogs, eject, init, iproute2, iputils-ping, isc-dhcp-client, kbd, kmod, less, locales, lsb-release, mawk, mount, netbase, netcat-openbsd, netplan.io, passwd, procps, python3, sensible-utils, sudo, tzdata, ubuntu-advantage-tools, ubuntu-keyring, udev, vim-tiny, whiptail
Recommends: rsyslog, usrmerge
```

　依存関係から、ubuntu-advantage-toolsを削る。

　ubuntu-serverのほうは、update-notifier-commonが依存している。これも削る。

Package: ubuntu-server
Status: install ok installed
Priority: optional
Section: metapackages
Installed-Size: 54
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: arm64
Source: ubuntu-meta
Version: 1.497
Depends: apport, bcache-tools, btrfs-progs, byobu, cloud-guest-utils, cloud-initramfs-copymods, cloud-initramfs-dyn-netconf, curl, dirmngr, ethtool, fonts-ubuntu-console, git, gnupg, htop, lvm2, mdadm, motd-news-config, multipath-tools, overlayroot, patch, pollinate, screen, software-properties-common, sosreport, tmux, update-notifier-common, vim, xfsprogs

　ubuntu-server-minimalは無関係のようだ。

Package: ubuntu-server-minimal
Status: install ok installed
Priority: optional
Section: metapackages
Installed-Size: 54
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: arm64
Source: ubuntu-meta
Version: 1.497
Depends: apparmor, apport, apt, bcache-tools, btrfs-progs, cloud-init, cryptsetup, dbus, e2fsprogs, lvm2, mdadm, multipath-tools, netbase, open-iscsi, pollinate, snapd, ssh-import-id, sudo, systemd, systemd-resolved, systemd-sysv, ubuntu-drivers-common, ubuntu-release-upgrader-core, udev, xfsprogs

　依存関係で、消えるようなことはなくなった。

```text
kinneko@utm:~$ sudo apt-get remove --purge ubuntu-advantage-tools -s
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  distro-info python3-debian
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  ubuntu-advantage-tools* update-manager-core* update-notifier-common*
0 upgraded, 0 newly installed, 3 to remove and 2 not upgraded.
Purg update-notifier-common [3.192.59.2]
Purg update-manager-core [1:22.10.4]
Purg ubuntu-advantage-tools [27.13.5~22.10.1]
```

　ディストリビューションを定義するようなメタパッケージの内容はあまり変化することはないので、上書きで問題になるようなことは、メジャーアップグレードを行うようなことがなけれれば気にしなくていいだろう。

　実際に削除を行う前に、他の方法も試しておく。

　2-4は意味がないのでパス。
5. /etc/default/motd-newsに設定があるのでENABLEDを0にする

　こちらは、エディタで直編集しなくても、proコマンドを使うと、設定できるようになった模様。しかし、aptの話なのに別のツールで設定するとか、ナシだよなぁ... どうせやるなら、ubuコマンドかなんかにforkしたらいいのに。

$ sudo pro config set apt_news=false

　前に見た設定ファイルはここ。

```text
kinneko@utm:~$ grep ENABLED /etc/default/motd-news
ENABLED=1
```

　非表示コマンドを実行して同じところが変わるかどうか確認してみる。違う...

```text
kinneko@utm:~$ sudo pro config set apt_news=false
kinneko@utm:~$ grep ENABLED /etc/default/motd-news
ENABLED=1
```

　proコマンドのログは、"/var/log/ubuntu-advantage.log"に格納される。ログによると、変更を加えたファイルは"/etc/ubuntu-advantage/uaclient.conf"のようだ。

　ファイルを確認すると"apt_news: false"が含まれている。

```text
kinneko@utm:~$ cat /etc/ubuntu-advantage/uaclient.conf
# Ubuntu Pro client config file.
# If you modify this file, run "pro refresh config" to ensure changes are
# picked up by Ubuntu Pro client.
```

contract_url: https://contracts.canonical.com
daemon_log_file: /var/log/ubuntu-advantage-daemon.log
data_dir: /var/lib/ubuntu-advantage
log_file: /var/log/ubuntu-advantage.log
log_level: debug
security_url: https://ubuntu.com/security
timer_log_file: /var/log/ubuntu-advantage-timer.log
ua_config:
apt_http_proxy: null
apt_https_proxy: null
apt_news: false
apt_news_url: https://motd.ubuntu.com/aptnews.json
global_apt_http_proxy: null
global_apt_https_proxy: null
http_proxy: null
https_proxy: null
metering_timer: 14400
ua_apt_http_proxy: null
ua_apt_https_proxy: null
update_messaging_timer: 21600

　というわけで、依存関係DBをいじって、ubuntu-advantage-toolsを削除する方法で対処することにしたが... 失敗した。
　パッケージDBを操作すると、アップデートに引っかかるようだ。サインストールすることになって、芋づる式にubuntu-advantage-toolsも入ってしまうよ...

```text
kinneko@utm:~$ sudo apt-get remove --purge ubuntu-advantage-tools
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  distro-info python3-debian
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  ubuntu-advantage-tools* update-manager-core* update-notifier-common*
0 upgraded, 0 newly installed, 3 to remove and 2 not upgraded.
After this operation, 2,528 kB disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 78408 files and directories currently installed.)
Removing update-notifier-common (3.192.59.2) ...
Removing update-manager-core (1:22.10.4) ...
dpkg: warning: while removing update-manager-core, directory '/var/lib/update-manager' not empty so not removed
Removing ubuntu-advantage-tools (27.13.5~22.10.1) ...
Processing triggers for man-db (2.10.2-2) ...
(Reading database ... 78043 files and directories currently installed.)
Purging configuration files for update-notifier-common (3.192.59.2) ...
Purging configuration files for ubuntu-advantage-tools (27.13.5~22.10.1) ...
```

```text
kinneko@utm:~$ sudo apt-get update
Hit:1 http://ports.ubuntu.com/ubuntu-ports kinetic InRelease
Hit:2 http://ports.ubuntu.com/ubuntu-ports kinetic-updates InRelease
Hit:3 http://ports.ubuntu.com/ubuntu-ports kinetic-backports InRelease
Hit:4 http://ports.ubuntu.com/ubuntu-ports kinetic-security InRelease
Reading package lists... Done
kinneko@utm:~$ sudo apt upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following NEW packages will be installed:
  ubuntu-advantage-tools update-manager-core update-notifier-common
The following packages will be upgraded:
  ubuntu-minimal ubuntu-server
2 upgraded, 3 newly installed, 0 to remove and 0 not upgraded.
Need to get 16.7 kB/352 kB of archives.
After this operation, 2,528 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
```

　パッケージロックしておけばいいかな？

```text
kinneko@utm:~$ sudo apt-mark hold ubuntu-minimal ubuntu-server
ubuntu-minimal set on hold.
ubuntu-server set on hold.
```

　ホールドされているのを確認する。問題なくできている。

```text
kinneko@utm:~$ cat /var/lib/dpkg/status | grep "Status: hold ok installed" -B 1
Package: ubuntu-minimal
Status: hold ok installed
--
Package: ubuntu-server
Status: hold ok installed
```

　再度アップグレードしてみる。問題なくできた。

```text
kinneko@utm:~$ sudo apt upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages were automatically installed and are no longer required:
  distro-info python3-debian
Use 'sudo apt autoremove' to remove them.
The following packages have been kept back:
  ubuntu-minimal ubuntu-server
0 upgraded, 0 newly installed, 0 to remove and 2 not upgraded.
```

---
> オリジナル投稿：<br>
> 続報：aptでUbuntu Proの宣伝が表示されるのをやめる -2-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/5330741>

+++
date = "2023-02-21T08:00:00"
draft = false
title = "続報：aptでUbuntu Proの宣伝が表示されるのをやめる -1-"
description = "Ubuntu Proのapt宣伝表示をUbuntu 22.04/22.10で検証する。"

[taxonomies]
tags = ["Ubuntu", "Ubuntu Pro", "apt", "2023-02"]

[extra]
image = "/2023-02-21/5329406-title.jpeg"
+++

　去年の10月に「aptでUbuntu Proの宣伝が表示されるのをやめる」という記事を書いた。(2/19)

> aptでUbuntu Proの宣伝が表示されるのをやめる｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/4603882>

> aptでUbuntu Proの宣伝が表示されるのをやめる
> 2022年10月21日 08:00
> 　22.10では、aptコマンドを実行するとUbuntu Proの宣伝が表示されるそうだ。 Try Ubuntu Pro beta with a free personal subscription on up to 5 machines. Learn more at https://ubuntu.com/pro 　個人的にはあんまり気にならない１行表示の広告。ユーザーのクレームがあるので、そのうちやめるのじゃないかな？ 　...
> 全体公開
> kinneko

　当時は一旦表示は止まっていたのだけど、最近、また出るようになっているそうだ。

> Ubuntu Advantage is being wired deeper into the distro • The Register<br>
> <https://www.theregister.com/2023/02/17/ubuntu_advantage/>

　テスト用の環境をUTMで準備する。22.04.1 LTSを新規にインストールした。

```text
kinneko@utm:~$ cat /etc/os-release
PRETTY_NAME="Ubuntu 22.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.1 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
```

　aptのバージョン。

```text
kinneko@utm:~$ dpkg -l apt
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name           Version      Architecture Description
+++-==============-============-============-=================================
ii  apt            2.4.6        arm64        commandline package manager
```

　ubuntu-advantage-toolsはインストールされていない。

```text
kinneko@utm:~$ dpkg -l ubuntu-advantage-tools
dpkg-query: no packages found matching ubuntu-advantage-tools
```

　パッケージリポジトリをアップデートする。

```text
kinneko@utm:~$ sudo apt-get update
[sudo] password for kinneko:
Hit:1 http://ports.ubuntu.com/ubuntu-ports jammy InRelease
Hit:2 http://ports.ubuntu.com/ubuntu-ports jammy-updates InRelease
Hit:3 http://ports.ubuntu.com/ubuntu-ports jammy-backports InRelease
Hit:4 http://ports.ubuntu.com/ubuntu-ports jammy-security InRelease
Reading package lists... Done
```

　おや？ パッケージアップグレードには、ubuntu-advantage-toolsが入ってこない。

```text
kinneko@utm:~$ sudo apt-get upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages have been kept back:
  cloud-init libudev1 python3-software-properties software-properties-common
  udev
The following packages will be upgraded:
  apport apt base-files cryptsetup cryptsetup-bin cryptsetup-initramfs
  distro-info-data gzip initramfs-tools initramfs-tools-bin
  initramfs-tools-core kbd libapt-pkg6.0 libcryptsetup12 libdrm-common libdrm2
  libglib2.0-0 libglib2.0-bin libglib2.0-data libldap-2.5-0 libldap-common
  libnetplan0 libnss-systemd libpam-systemd libpython3-stdlib libsasl2-2
  libsasl2-modules libsasl2-modules-db libsystemd0 netplan.io
  python-apt-common python3 python3-apport python3-apt python3-distupgrade
  python3-distutils python3-lib2to3 python3-minimal python3-problem-report
  python3-tz python3-update-manager snapd systemd systemd-sysv
  systemd-timesyncd ubuntu-release-upgrader-core
46 upgraded, 0 newly installed, 0 to remove and 5 not upgraded.
Need to get 33.0 MB of archives.
After this operation, 502 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
```

　ダメだこりゃ。22.04は対象にはなっていないという確認で終わったわ。

　しょうがないので、22.10を入れる。

```text
kinneko@utm:~$ cat /etc/os-release
PRETTY_NAME="Ubuntu 22.10"
NAME="Ubuntu"
VERSION_ID="22.10"
VERSION="22.10 (Kinetic Kudu)"
VERSION_CODENAME=kinetic
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=kinetic
LOGO=ubuntu-logo
```

```text
kinneko@utm:~$ sudo apt update
[sudo] password for kinneko:
Hit:1 http://ports.ubuntu.com/ubuntu-ports kinetic InRelease
Hit:2 http://ports.ubuntu.com/ubuntu-ports kinetic-updates InRelease
Hit:3 http://ports.ubuntu.com/ubuntu-ports kinetic-backports InRelease
Hit:4 http://ports.ubuntu.com/ubuntu-ports kinetic-security InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
10 packages can be upgraded. Run 'apt list --upgradable' to see them.
```

　なんか、dpkg -lしたら、表示がページャーを経由している感じ。なんか改悪だな。

![](/2023-02-21/5329406-01.png)

　んで、ubuntu-advantage-toolsは入っていない...

　なんだよもう...

　インストール時にミニマルを入れたからかな？

![](/2023-02-21/5329406-02.png)

　upgradeしても入らない。

```text
kinneko@utm:~$ sudo apt-get upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  cloud-init distro-info-data kbd libglib2.0-0 libglib2.0-bin libglib2.0-data
  python-apt-common python3-apt snapd systemd-hwe-hwdb
10 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 24.5 MB of archives.
After this operation, 1849 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
```

　しょうがないので、インストールしなおす。ubuntu-advantage-toolsは入っている。

```text
kinneko@utm:~$ dpkg -l apt
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name           Version      Architecture Description
+++-==============-============-============-=================================
ii  apt            2.5.3        arm64        commandline package manager
```

```text
kinneko@utm:~$ dpkg -l ubuntu-advantage-tools
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                   Version         Architecture Description
+++-======================-===============-============-=======================>
ii  ubuntu-advantage-tools 27.11.2~22.10.1 arm64        management tools for Ub>
lines 1-6/6 (END)
```

　アップデートする。

```text
kinneko@utm:~$ sudo apt-get update
[sudo] password for kinneko:
Hit:1 http://ports.ubuntu.com/ubuntu-ports kinetic InRelease
Get:2 http://ports.ubuntu.com/ubuntu-ports kinetic-updates InRelease [118 kB]
Hit:3 http://ports.ubuntu.com/ubuntu-ports kinetic-backports InRelease
Hit:4 http://ports.ubuntu.com/ubuntu-ports kinetic-security InRelease
Get:5 http://ports.ubuntu.com/ubuntu-ports kinetic-updates/main arm64 Packages [290 kB]
Fetched 408 kB in 4s (107 kB/s)
Reading package lists... Done
```

```text
kinneko@utm:~$ sudo apt-get upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  cloud-init distro-info-data kbd libglib2.0-0 libglib2.0-bin libglib2.0-data
  python-apt-common python3-apt snapd sosreport systemd-hwe-hwdb
  ubuntu-advantage-tools update-notifier-common
13 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 25.2 MB of archives.
After this operation, 2,268 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
```

　ubuntu-advantage-toolsは、27.13.5~22.10.1に上がった。前が27.11.2~22.10.1だったので、バージョンは少し上がった感じか。

　ようやく準備ができた。

　手間はかかったが、minimizedではubuntu-advantage-toolsが入らないという知見を得た。

---
> オリジナル投稿：<br>
> 続報：aptでUbuntu Proの宣伝が表示されるのをやめる -1-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/5329406>

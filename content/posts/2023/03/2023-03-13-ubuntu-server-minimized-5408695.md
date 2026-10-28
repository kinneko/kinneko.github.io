+++
date = "2023-03-13 08:00:00"
draft = false
title = "Ubunt Server 20.04LTSをminimizedでインストールする"
description = "Ubuntu Serverのminimized構成でUbuntu Pro関連パッケージとSnapの依存関係を確認する。"

[taxonomies]
tags = ["Ubuntu", "Linux", "2023-03"]

[extra]
image = "/2023-03-13/5408695-cover.jpeg"
+++

　前回の宿題が少し残っていた。

　Ubunt Server 20.04LTSをminimizedで入れたときにはubuntu-advantage-toolsがインストールされていないのではないかという問題。

> 続報：aptでUbuntu Proの宣伝が表示されるのをやめる -1-｜kinneko｜pixivFANBOX<br>
> <https://www.fanbox.cc/@kinneko/posts/5329406>

　フルインストールすると、メタパッケージのubuntu-serverとubuntu-server-minimalが入っていて、そのうちubuntu-serverだけがubuntu-advantage-toolsに依存していたのだけど、minimizedでインストールしたときには、ubuntu-advantage-toolsが入っていないようで、どう解決されているのか確認しておく。

　UTMでさくさくインストールしてみる。

　インストール時のこの画面で、minimizedを選ぶだけ。あとは普通にインストールする。sshdだけ入れて、他のサーバーは動作させない。

![](/2023-03-13/5408695-02.png)

　パッケージ数を確認。そんなに小さくもない。412パッケージも入っている。

```text
kinneko@utm:~$ dpkg -l |wc
417    4207   57942
```

　メタパッケージとしてubuntu-server-minimalだけが入っている。

```text
kinneko@utm:~$ dpkg -l | grep ubuntu-server
ii  ubuntu-server-minimal                 1.481                                   arm64        The Ubuntu Server minimal system
```

　つまり、minimaizedでインストールしたときには、ubuntu-advantage-toolsがインストールされておらず、Fullでインストールしたときには、ubuntu-advantage-toolsがインストールされていたという問題は、ubuntu-serverパッケージが入っていないからという結論でいいようだ。

　一応、ubuntu-advantage-toolsはインストールされていないのを確認する。詳細は前に書いた記事を参照。

> 続報：aptでUbuntu Proの宣伝が表示されるのをやめる -2-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/5330741>

```text
kinneko@utm:~$ dpkg -l | grep ubuntu-advantage-tools
```

　ついでに、snap環境を削除してみる。詳細は前に書いた記事を参照。

> Ubuntu 20.04でSnapを無効にする｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/993518>

　snapは入っている。

```text
kinneko@utm:~$ dpkg -l | grep snap
ii  lxd-installer                         1                                       all          Wrapper to install lxd snap on demand
ii  snapd                                 2.57.5+22.04ubuntu0.1                   arm64        Daemon and tooling that enable snap packages
```

　snapがubuntu-server-minimalの依存パッケージに入っていないか確認する。入っていないので削除できる。

```text
kinneko@utm:~$ cat /var/lib/dpkg/status | grep ubuntu-server-minimal -A 10
Package: ubuntu-server-minimal
Status: install ok installed
Priority: optional
Section: metapackages
Installed-Size: 53
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: arm64
Source: ubuntu-meta
Version: 1.481
Depends: apparmor, apport, apt, bcache-tools, btrfs-progs, cloud-init, cryptsetup, dbus, lvm2, mdadm, multipath-tools, netbase, ntfs-3g, open-iscsi, pollinate, snapd, ssh-import-id, sudo, systemd, systemd-sysv, ubuntu-drivers-common, ubuntu-release-upgrader-core, udev, xfsprogs
Recommends: needrestart, unattended-upgrades
```

　snapで管理されているパッケージがインストールされていないか調べる。ないようだ。

```text
kinneko@utm:~$ snap list
No snaps are installed yet. Try 'snap install hello-world'.
```

　snap関連パッケージは２つ。

```text
kinneko@utm:~$ dpkg -l | grep snap
ii  lxd-installer                         1                                       all          Wrapper to install lxd snap on demand
ii  snapd                                 2.57.5+22.04ubuntu0.1                   arm64        Daemon and tooling that enable snap packages
```

　どちらも削除しようと思ったら、こちらはsnapdがubuntu-server-minimalの依存関係になっていて削除できない。なかなか厳しい。とりあえず放置する。

```text
kinneko@utm:~$ sudo apt-get remove --purge snapd lxd-installer
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following package was automatically installed and is no longer required:
squashfs-tools
Use 'sudo apt autoremove' to remove it.
The following packages will be REMOVED:
lxd-installer* snapd* ubuntu-server-minimal*
0 upgraded, 0 newly installed, 3 to remove and 52 not upgraded.
After this operation, 96.4 MB disk space will be freed.
Do you want to continue? [Y/n] n
```

　snapdを削除できなかったので、snap関連のディレクトリも残ったまま。

```text
kinneko@utm:~$  ls ~/snap
ls: cannot access '/home/kinneko/snap': No such file or directory
kinneko@utm:~$ ls /snap
README
kinneko@utm:~$ ls /var/snap
kinneko@utm:~$ ls /var/lib/snapd
apparmor     cookie   environment  inhibit           seccomp  state.json  void
assertions   dbus-1   features     lib               snaps    state.lock
auto-import  desktop  firstboot    maintenance.json  ssl      system-key
```

　ほんとは、100台くらいまでパッケージのダイエットをやりたいところなのだけど、今回はやらない。

　しかし、パッケージ数が多い割には、viすら入ってないので不便ではある。

```text
kinneko@utm:~$ sudo vi /var/lib/dpkg/status
sudo: vi: command not found
```

　インストールされているパッケージ一覧を残しておこう。

```text
kinneko@utm:~$ dpkg -l|grep ii|awk '{print $2}'|wc
412     412    6341
```

```text
kinneko@utm:~$ dpkg -l|grep ii|awk '{print $2}'
adduser
apparmor
apport
apport-symptoms
apt
base-files
base-passwd
bash
bcache-tools
binutils
binutils-aarch64-linux-gnu
binutils-common:arm64
bsdutils
btrfs-progs
busybox-initramfs
ca-certificates
cloud-guest-utils
cloud-init
console-setup
console-setup-linux
coreutils
cpio
cryptsetup
cryptsetup-bin
cryptsetup-initramfs
curl
dash
dbus
dbus-user-session
debconf
debianutils
diffutils
dirmngr
distro-info-data
dmeventd
dmsetup
dpkg
e2fsprogs
eatmydata
efibootmgr
fdisk
finalrd
findutils
firmware-sof-signed
fuse3
gawk
gcc-12-base:arm64
gdisk
gettext-base
gir1.2-glib-2.0:arm64
gir1.2-packagekitglib-1.0
gnupg
gnupg-l10n
gnupg-utils
gpg
gpg-agent
gpg-wks-client
gpg-wks-server
gpgconf
gpgsm
gpgv
grep
groff-base
grub-common
grub-efi-arm64
grub-efi-arm64-bin
grub-efi-arm64-signed
grub2-common
gzip
hostname
init-system-helpers
initramfs-tools
initramfs-tools-bin
initramfs-tools-core
iproute2
isc-dhcp-client
isc-dhcp-common
iso-codes
kbd
keyboard-configuration
klibc-utils
kmod
kpartx
libacl1:arm64
libaio1:arm64
libapparmor1:arm64
libappstream4:arm64
libapt-pkg6.0:arm64
libargon2-1:arm64
libassuan0:arm64
libatm1:arm64
libattr1:arm64
libaudit-common
libaudit1:arm64
libbinutils:arm64
libblkid1:arm64
libbpf0:arm64
libbrotli1:arm64
libbsd0:arm64
libbz2-1.0:arm64
libc-bin
libc6:arm64
libcap-ng0:arm64
libcap2:arm64
libcap2-bin
libcbor0.8:arm64
libcom-err2:arm64
libcrypt1:arm64
libcryptsetup12:arm64
libctf-nobfd0:arm64
libctf0:arm64
libcurl3-gnutls:arm64
libcurl4:arm64
libdb5.3:arm64
libdbus-1-3:arm64
libdebconfclient0:arm64
libdevmapper-event1.02.1:arm64
libdevmapper1.02.1:arm64
libdns-export1110
libdrm-common
libdrm2:arm64
libdw1:arm64
libeatmydata1:arm64
libedit2:arm64
libefiboot1:arm64
libefivar1:arm64
libelf1:arm64
libexpat1:arm64
libext2fs2:arm64
libfdisk1:arm64
libffi8:arm64
libfido2-1:arm64
libfreetype6:arm64
libfuse3-3:arm64
libgcc-s1:arm64
libgcrypt20:arm64
libgdbm-compat4:arm64
libgdbm6:arm64
libgirepository-1.0-1:arm64
libglib2.0-0:arm64
libglib2.0-bin
libglib2.0-data
libgmp10:arm64
libgnutls30:arm64
libgpg-error0:arm64
libgssapi-krb5-2:arm64
libgstreamer1.0-0:arm64
libhogweed6:arm64
libicu70:arm64
libidn2-0:arm64
libinih1:arm64
libintl-perl
libintl-xs-perl
libip4tc2:arm64
libisc-export1105:arm64
libisns0:arm64
libjson-c5:arm64
libk5crypto3:arm64
libkeyutils1:arm64
libklibc:arm64
libkmod2:arm64
libkrb5-3:arm64
libkrb5support0:arm64
libksba8:arm64
libldap-2.5-0:arm64
libldap-common
liblocale-gettext-perl
liblvm2cmd2.03:arm64
liblz4-1:arm64
liblzma5:arm64
liblzo2-2:arm64
libmd0:arm64
libmnl0:arm64
libmodule-find-perl
libmodule-scandeps-perl
libmount1:arm64
libmpdec3:arm64
libmpfr6:arm64
libncurses6:arm64
libncursesw6:arm64
libnetplan0:arm64
libnettle8:arm64
libnghttp2-14:arm64
libnpth0:arm64
libnsl2:arm64
libnss-systemd:arm64
libntfs-3g89
libopeniscsiusr
libp11-kit0:arm64
libpackagekit-glib2-18:arm64
libpam-cap:arm64
libpam-modules:arm64
libpam-modules-bin
libpam-runtime
libpam-systemd:arm64
libpam0g:arm64
libpci3:arm64
libpcre2-8-0:arm64
libpcre3:arm64
libperl5.34:arm64
libplymouth5:arm64
libpng16-16:arm64
libpolkit-agent-1-0:arm64
libpolkit-gobject-1-0:arm64
libpopt0:arm64
libproc-processtable-perl:arm64
libprocps8:arm64
libpsl5:arm64
libpython3-stdlib:arm64
libpython3.10-minimal:arm64
libpython3.10-stdlib:arm64
libreadline8:arm64
librtmp1:arm64
libsasl2-2:arm64
libsasl2-modules:arm64
libsasl2-modules-db:arm64
libseccomp2:arm64
libselinux1:arm64
libsemanage-common
libsemanage2:arm64
libsepol2:arm64
libsgutils2-2:arm64
libsigsegv2:arm64
libsmartcols1:arm64
libsort-naturally-perl
libsqlite3-0:arm64
libss2:arm64
libssh-4:arm64
libssl3:arm64
libstdc++6:arm64
libstemmer0d:arm64
libsystemd0:arm64
libtasn1-6:arm64
libterm-readkey-perl
libtinfo6:arm64
libtirpc-common
libtirpc3:arm64
libuchardet0:arm64
libudev1:arm64
libunistring2:arm64
libunwind8:arm64
liburcu8:arm64
libusb-1.0-0:arm64
libuuid1:arm64
libwrap0:arm64
libx11-6:arm64
libx11-data
libxau6:arm64
libxcb1:arm64
libxdmcp6:arm64
libxext6:arm64
libxml2:arm64
libxmlb2:arm64
libxmuu1:arm64
libxtables12:arm64
libxxhash0:arm64
libyaml-0-2:arm64
libzstd1:arm64
linux-base
linux-firmware
linux-generic
linux-headers-5.15.0-67
linux-headers-5.15.0-67-generic
linux-headers-generic
linux-image-5.15.0-67-generic
linux-image-generic
linux-modules-5.15.0-67-generic
linux-modules-extra-5.15.0-67-generic
login
logsave
lsb-base
lsb-release
lvm2
lxd-installer
mawk
mdadm
media-types
mokutil
mount
multipath-tools
ncurses-base
ncurses-bin
ncurses-term
needrestart
netbase
netplan.io
networkd-dispatcher
ntfs-3g
open-iscsi
openssh-client
openssh-server
openssh-sftp-server
openssl
os-prober
packagekit
packagekit-tools
passwd
pci.ids
pciutils
perl
perl-base
perl-modules-5.34
pinentry-curses
pkexec
plymouth
plymouth-theme-ubuntu-text
policykit-1
polkitd
pollinate
procps
publicsuffix
python-apt-common
python-babel-localedata
python3
python3-apport
python3-apt
python3-attr
python3-babel
python3-blinker
python3-certifi
python3-cffi-backend:arm64
python3-chardet
python3-click
python3-colorama
python3-configobj
python3-cryptography
python3-dbus
python3-distro
python3-distro-info
python3-distupgrade
python3-distutils
python3-gi
python3-httplib2
python3-idna
python3-importlib-metadata
python3-jeepney
python3-jinja2
python3-json-pointer
python3-jsonpatch
python3-jsonschema
python3-jwt
python3-keyring
python3-launchpadlib
python3-lazr.restfulclient
python3-lazr.uri
python3-lib2to3
python3-markupsafe
python3-minimal
python3-more-itertools
python3-netifaces:arm64
python3-oauthlib
python3-pkg-resources
python3-problem-report
python3-pyparsing
python3-pyrsistent:arm64
python3-requests
python3-secretstorage
python3-serial
python3-setuptools
python3-six
python3-software-properties
python3-systemd
python3-tz
python3-update-manager
python3-urllib3
python3-wadllib
python3-xkit
python3-yaml
python3-zipp
python3.10
python3.10-minimal
readline-common
sbsigntool
secureboot-db
sed
sensible-utils
sg3-utils
sg3-utils-udev
shared-mime-info
shim-signed
snapd
software-properties-common
squashfs-tools
ssh-import-id
sudo
systemd
systemd-sysv
systemd-timesyncd
sysvinit-utils
tar
thin-provisioning-tools
tzdata
ubuntu-drivers-common
ubuntu-keyring
ubuntu-release-upgrader-core
ubuntu-server-minimal
ucf
udev
unattended-upgrades
usbutils
usrmerge
util-linux
wget
wireless-regdb
xauth
xdg-user-dirs
xfsprogs
xkb-data
xxd
xz-utils
zlib1g:arm64
zstd
```

---
> オリジナル投稿：<br>
> Ubunt Server 20.04LTSをminimizedでインストールする｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/5408695>

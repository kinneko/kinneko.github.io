+++
date = "2024-02-09 08:00:00"
draft = false
title = "Raspiコンソールで動画表示 -2-"
description = "omxplayerで絶望を味わい、ふつーにvlcを動かしてみることにした。"

[taxonomies]
tags = ["Raspberry Pi", "VLC", "動画", "2024-02"]

[extra]
image = "2024-02-09/7419088-title.jpeg"
+++

　omxplayerで絶望を味わい、ふつーにvlcを動かしてみることにした。

　vlcをインストールする。

```text
kinneko@raspberrypi:~ $ sudo apt-get install vlc
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  adwaita-icon-theme at-spi2-common at-spi2-core dconf-gsettings-backend
  dconf-service fonts-freefont-ttf gsettings-desktop-schemas
  gtk-update-icon-cache hicolor-icon-theme liba52-0.7.4 libaa1 libaacs0
  libarchive13 libaribb24-0 libass9 libasyncns0 libatk-bridge2.0-0 libatk1.0-0
  libatspi2.0-0 libauthen-sasl-perl libavc1394-0 libavcodec59 libavfilter8
  libavformat59 libavutil57 libbasicusageenvironment1 libbdplus0 libblas3
  libbluray2 libbs2b0 libcaca0 libcddb2 libchromaprint1 libcjson1
  libclone-perl libcodec2-1.0 libcolord2 libdata-dump-perl libdc1394-25
  libdca0 libdconf1 libdrm-amdgpu1 libdrm-nouveau2 libdrm-radeon1 libdvbpsi10
  libdvdnav4 libegl-mesa0 libegl1 libencode-locale-perl libepoxy0 libevdev2
  libfaad2 libfile-basedir-perl libfile-desktopentry-perl libfile-listing-perl
  libfile-mimeinfo-perl libflite1 libfont-afm-perl libgbm1 libgfortran5 libgl1
  libgl1-mesa-dri libglapi-mesa libgles2 libglvnd0 libglx-mesa0 libglx0
  libgme0 libgroupsock8 libgsm1 libgtk-3-0 libgtk-3-bin libgtk-3-common
  libhtml-form-perl libhtml-format-perl libhtml-parser-perl
  libhtml-tagset-perl libhtml-tree-perl libhttp-cookies-perl
  libhttp-daemon-perl libhttp-date-perl libhttp-message-perl
  libhttp-negotiate-perl libinput-bin libinput10 libio-html-perl
  libio-socket-ssl-perl libio-stringy-perl libipc-system-simple-perl libixml10
  libkate1 liblapack3 libldb2 liblilv-0-0 liblirc-client0 liblivemedia77
  libllvm15 liblua5.2-0 liblwp-mediatypes-perl liblwp-protocol-https-perl
  liblzo2-2 libmad0 libmailtools-perl libmbedcrypto7 libmd4c0 libmp3lame0
  libmpcdec6 libmpeg2-4 libmpg123-0 libmtdev1 libmysofa1 libnet-dbus-perl
  libnet-http-perl libnet-smtp-ssl-perl libnet-ssleay-perl libnfs13 libnorm1
  libnotify4 libopenmpt-modplug1 libopenmpt0 libopus0 libpgm-5.3-0
  libplacebo208 libpocketsphinx3 libpostproc56 libprotobuf-lite32
  libproxy-tools libproxy1v5 libpulse0 libqt5dbus5 libqt5gui5 libqt5network5
  libqt5qml5 libqt5qmlmodels5 libqt5quick5 libqt5svg5 libqt5waylandclient5
  libqt5waylandcompositor5 libqt5widgets5 libqt5x11extras5 librabbitmq4
  libraw1394-11 libregexp-ipv6-perl libresid-builder0c2a librist4
  librubberband2 libsdl-image1.2 libsdl1.2debian libsecret-1-0
  libsecret-common libsensors-config libsensors5 libserd-0-0 libshine3
  libshout3 libsidplay2 libsmbclient libsnappy1v5 libsndfile1 libsodium23
  libsord-0-0 libsoxr0 libspatialaudio0 libspeex1 libspeexdsp1 libsphinxbase3
  libsratom-0-0 libsrt1.5-gnutls libssh-gcrypt-4 libswresample4 libswscale6
  libtag1v5 libtag1v5-vanilla libtdb1 libtevent0 libtheora0 libtie-ixhash-perl
  libtimedate-perl libtry-tiny-perl libtwolame0 libudfread0 libupnp13
  liburi-perl libusageenvironment3 libva-drm2 libva-x11-2 libva2
  libvdpau-va-gl1 libvdpau1 libvidstab1.1 libvlc-bin libvlc5 libvlccore9
  libvncclient1 libvorbisenc2 libvorbisfile3 libvpx7 libvulkan1
  libwacom-common libwacom9 libwayland-client0 libwayland-cursor0
  libwayland-egl1 libwayland-server0 libwebpmux3 libwww-perl
  libwww-robotrules-perl libx11-protocol-perl libx264-164 libxaw7
  libxcb-composite0 libxcb-dri2-0 libxcb-dri3-0 libxcb-glx0 libxcb-icccm4
  libxcb-image0 libxcb-keysyms1 libxcb-present0 libxcb-randr0
  libxcb-render-util0 libxcb-shape0 libxcb-sync1 libxcb-util1 libxcb-xfixes0
  libxcb-xinerama0 libxcb-xinput0 libxcb-xkb1 libxcb-xv0 libxcomposite1
  libxcursor1 libxdamage1 libxfixes3 libxft2 libxi6 libxinerama1
  libxkbcommon-x11-0 libxkbcommon0 libxkbfile1 libxml-parser-perl
  libxml-twig-perl libxml-xpathengine-perl libxmu6 libxrandr2 libxshmfence1
  libxtst6 libxv1 libxvidcore4 libxxf86dga1 libxxf86vm1 libz3-4 libzimg2
  libzmq5 libzvbi-common libzvbi0 mesa-va-drivers mesa-vdpau-drivers
  mesa-vulkan-drivers ocl-icd-libopencl1 perl-openssl-defaults
  pocketsphinx-en-us qt5-gtk-platformtheme qtwayland5 samba-libs va-driver-all
  vdpau-driver-all vlc-bin vlc-data vlc-l10n vlc-plugin-access-extra
  vlc-plugin-base vlc-plugin-notify vlc-plugin-qt vlc-plugin-samba
  vlc-plugin-skins2 vlc-plugin-video-output vlc-plugin-video-splitter
  vlc-plugin-visualization x11-utils x11-xserver-utils xdg-utils zutty
Suggested packages:
  lrzip libdigest-hmac-perl libgssapi-perl libbluray-bdj colord libdvdcss2
  gvfs lirc libcrypt-ssleay-perl notification-daemon opus-tools pulseaudio
  qgnomeplatform-qt5 qt5-image-formats-plugins qt5-qmltooling-plugins
  libraw1394-doc lm-sensors serdi sordi speex libsub-name-perl
  libbusiness-isbn-perl libwacom-bin libauthen-ntlm-perl libunicode-map8-perl
  libunicode-string-perl xml-twig-tools opencl-icd debhelper
  nvidia-legacy-390xx-vdpau-driver nvidia-legacy-340xx-vdpau-driver
  vlc-plugin-fluidsynth vlc-plugin-jack vlc-plugin-pipewire vlc-plugin-svg
  mesa-utils nickle cairo-5c xorg-docs-core
The following NEW packages will be installed:
  adwaita-icon-theme at-spi2-common at-spi2-core dconf-gsettings-backend
  dconf-service fonts-freefont-ttf gsettings-desktop-schemas
  gtk-update-icon-cache hicolor-icon-theme liba52-0.7.4 libaa1 libaacs0
  libarchive13 libaribb24-0 libass9 libasyncns0 libatk-bridge2.0-0 libatk1.0-0
  libatspi2.0-0 libauthen-sasl-perl libavc1394-0 libavcodec59 libavfilter8
  libavformat59 libavutil57 libbasicusageenvironment1 libbdplus0 libblas3
  libbluray2 libbs2b0 libcaca0 libcddb2 libchromaprint1 libcjson1
  libclone-perl libcodec2-1.0 libcolord2 libdata-dump-perl libdc1394-25
  libdca0 libdconf1 libdrm-amdgpu1 libdrm-nouveau2 libdrm-radeon1 libdvbpsi10
  libdvdnav4 libegl-mesa0 libegl1 libencode-locale-perl libepoxy0 libevdev2
  libfaad2 libfile-basedir-perl libfile-desktopentry-perl libfile-listing-perl
  libfile-mimeinfo-perl libflite1 libfont-afm-perl libgbm1 libgfortran5 libgl1
  libgl1-mesa-dri libglapi-mesa libgles2 libglvnd0 libglx-mesa0 libglx0
  libgme0 libgroupsock8 libgsm1 libgtk-3-0 libgtk-3-bin libgtk-3-common
  libhtml-form-perl libhtml-format-perl libhtml-parser-perl
  libhtml-tagset-perl libhtml-tree-perl libhttp-cookies-perl
  libhttp-daemon-perl libhttp-date-perl libhttp-message-perl
  libhttp-negotiate-perl libinput-bin libinput10 libio-html-perl
  libio-socket-ssl-perl libio-stringy-perl libipc-system-simple-perl libixml10
  libkate1 liblapack3 libldb2 liblilv-0-0 liblirc-client0 liblivemedia77
  libllvm15 liblua5.2-0 liblwp-mediatypes-perl liblwp-protocol-https-perl
  liblzo2-2 libmad0 libmailtools-perl libmbedcrypto7 libmd4c0 libmp3lame0
  libmpcdec6 libmpeg2-4 libmpg123-0 libmtdev1 libmysofa1 libnet-dbus-perl
  libnet-http-perl libnet-smtp-ssl-perl libnet-ssleay-perl libnfs13 libnorm1
  libnotify4 libopenmpt-modplug1 libopenmpt0 libopus0 libpgm-5.3-0
  libplacebo208 libpocketsphinx3 libpostproc56 libprotobuf-lite32
  libproxy-tools libproxy1v5 libpulse0 libqt5dbus5 libqt5gui5 libqt5network5
  libqt5qml5 libqt5qmlmodels5 libqt5quick5 libqt5svg5 libqt5waylandclient5
  libqt5waylandcompositor5 libqt5widgets5 libqt5x11extras5 librabbitmq4
  libraw1394-11 libregexp-ipv6-perl libresid-builder0c2a librist4
  librubberband2 libsdl-image1.2 libsdl1.2debian libsecret-1-0
  libsecret-common libsensors-config libsensors5 libserd-0-0 libshine3
  libshout3 libsidplay2 libsmbclient libsnappy1v5 libsndfile1 libsodium23
  libsord-0-0 libsoxr0 libspatialaudio0 libspeex1 libspeexdsp1 libsphinxbase3
  libsratom-0-0 libsrt1.5-gnutls libssh-gcrypt-4 libswresample4 libswscale6
  libtag1v5 libtag1v5-vanilla libtdb1 libtevent0 libtheora0 libtie-ixhash-perl
  libtimedate-perl libtry-tiny-perl libtwolame0 libudfread0 libupnp13
  liburi-perl libusageenvironment3 libva-drm2 libva-x11-2 libva2
  libvdpau-va-gl1 libvdpau1 libvidstab1.1 libvlc-bin libvlc5 libvlccore9
  libvncclient1 libvorbisenc2 libvorbisfile3 libvpx7 libvulkan1
  libwacom-common libwacom9 libwayland-client0 libwayland-cursor0
  libwayland-egl1 libwayland-server0 libwebpmux3 libwww-perl
  libwww-robotrules-perl libx11-protocol-perl libx264-164 libxaw7
  libxcb-composite0 libxcb-dri2-0 libxcb-dri3-0 libxcb-glx0 libxcb-icccm4
  libxcb-image0 libxcb-keysyms1 libxcb-present0 libxcb-randr0
  libxcb-render-util0 libxcb-shape0 libxcb-sync1 libxcb-util1 libxcb-xfixes0
  libxcb-xinerama0 libxcb-xinput0 libxcb-xkb1 libxcb-xv0 libxcomposite1
  libxcursor1 libxdamage1 libxfixes3 libxft2 libxi6 libxinerama1
  libxkbcommon-x11-0 libxkbcommon0 libxkbfile1 libxml-parser-perl
  libxml-twig-perl libxml-xpathengine-perl libxmu6 libxrandr2 libxshmfence1
  libxtst6 libxv1 libxvidcore4 libxxf86dga1 libxxf86vm1 libz3-4 libzimg2
  libzmq5 libzvbi-common libzvbi0 mesa-va-drivers mesa-vdpau-drivers
  mesa-vulkan-drivers ocl-icd-libopencl1 perl-openssl-defaults
  pocketsphinx-en-us qt5-gtk-platformtheme qtwayland5 samba-libs va-driver-all
  vdpau-driver-all vlc vlc-bin vlc-data vlc-l10n vlc-plugin-access-extra
  vlc-plugin-base vlc-plugin-notify vlc-plugin-qt vlc-plugin-samba
  vlc-plugin-skins2 vlc-plugin-video-output vlc-plugin-video-splitter
  vlc-plugin-visualization x11-utils x11-xserver-utils xdg-utils zutty
0 upgraded, 282 newly installed, 0 to remove and 7 not upgraded.
Need to get 170 MB of archives.
After this operation, 602 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
(snip)
```

　依存パッケージが大量にインストールされて泣ける。

　コマンドラインでvlcを動かすには、cvlcコマンドを使用する。とりあえず起動してみる。

```text
kinneko@raspberrypi:~ $ cvlc
VLC media player 3.0.20 Vetinari (revision 3.0.20-0-g6f0d0ab126b)
[002d5528] vlcpulse audio output error: PulseAudio server connection failure: Connection refused
[002ef4a8] main interface error: no suitable interface module
[00256b50] main libvlc error: interface "globalhotkeys,none" initialization failed
[002ef4a8] dummy interface: using the dummy interface module...
[002d3bc0] main playlist: playlist is empty
```

　LiteにはAudio関係の動作環境がないようだ。vlcの依存関係でもインストールされない。これはどうなんだろ。

```text
kinneko@raspberrypi:~ $ pulseaudio --check
-bash: pulseaudio: command not found
```

　動画の再生だけでも確認してみる。

　動画のサンプルは、Blenderのサンプルで有名なBig Buck Bunnyからsample-videos.comで配っている1MB 720pのファイルを使う。

> Download Sample Videos / Dummy Videos For Demo Use<br>
> <https://sample-videos.com/>

> <https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4>

![](/2024-02-09/7419088-01.png)

　Raspiにダウンロードする。

```text
kinneko@raspberrypi:~ $ curl -OL https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 1030k  100 1030k    0     0   322k      0  0:00:03  0:00:03 --:--:--  322k
```

　再生してみる。

```text
kinneko@raspberrypi:~ $ cvlc big_buck_bunny_720p_1mb.mp4
VLC media player 3.0.20 Vetinari (revision 3.0.20-0-g6f0d0ab126b)
[018d5528] vlcpulse audio output error: PulseAudio server connection failure: Connection refused
[018d5c08] main interface error: no suitable interface module
[01856b50] main libvlc error: interface "globalhotkeys,none" initialization failed
[018d5c08] dummy interface: using the dummy interface module...
[b357d248] gles2 generic error: parent window not available
[b357d248] xcb generic error: window not available
[b357c610] mmal_xsplitter vout display: Try drm
[b357d248] drm_vout generic: <<< OpenDrmVout: Fmt=DPV0
[b357d248] drm_vout generic error: Failed to get xlease
[b3513000] avcodec decoder: Using DRM Video Accel for hardware decoding
[018d5528] alsa audio output error: cannot estimate delay: Broken pipe
[018d5528] alsa audio output error: cannot estimate delay: Broken pipe
```

　普通に再生できるね。最初のロードには２秒くらいのタイムラグはある。見た目的にはコマ落ちなどはない様子。

![](/2024-02-09/7419088-02.png)

　loopオプションで連続再生する。ファイル名が表示されるのはよくないな。

```text
kinneko@raspberrypi:~ $ cvlc big_buck_bunny_720p_1mb.mp4 --loop
```

![](/2024-02-09/7419088-03.png)

```text
kinneko@raspberrypi:~ $ cvlc big_buck_bunny_720p_1mb.mp4 --loop --no-video-title-show
```

![](/2024-02-09/7419088-04.png)

　同じファイルの再生は、loopではなくrepeatがよさげだ。こっちのほうが動画の切り替え時にチラチラが少しだけなくなる感じ。

```text
kinneko@raspberrypi:~ $ cvlc big_buck_bunny_720p_1mb.mp4 --repeat --no-video-title
```

　再生時のログはこんな感じ。ハードウエアデコードはされているようだ。

```text
[b256b990] avcodec decoder: Using DRM Video Accel for hardware decoding
```

　ループ再生を延々とさせても、20度くらいの雰囲気環境で、SoCは人肌くらいなので、さほど負荷にはなっていない模様。

　とりあえず、動画再生だけならすんなり動いて拍子抜け。cvlcを動かすだけであれば、こんなに依存パッケージはいらないはずなので、カスタムのメタパッケージ化ができるようにしてほしいところだ。

---
> オリジナル投稿：<br>
> Raspiコンソールで動画表示 -2-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/7419088>

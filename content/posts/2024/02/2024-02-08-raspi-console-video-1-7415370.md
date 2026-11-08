+++
date = "2024-02-08 08:00:00"
draft = false
title = "Raspiコンソールで動画表示 -1-"
description = "マシンパワー的にはちょっと無理ゲーなのだけど、コンソールで動画表示というリクエストが来たので一応試してみる。"

[taxonomies]
tags = ["Raspberry Pi", "動画", "2024-02"]

[extra]
image = "2024-02-08/7415370-title.jpeg"
+++

　マシンパワー的にはちょっと無理ゲーなのだけど、コンソールで動画表示というリクエストが来たので一応試してみる。

　うまく動けば儲けものくらいの感じ。たぶんパワー的には見るに耐えないかな... GPU使えればいいんだけど。

　シリーズというと、このへんの続きか。

> RaspiOSでfbiでfb0に描画｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/6923189>

> RaspiコンソールでPDF表示 -1-<br>
> <https://kinneko.fanbox.cc/posts/7402751>

> RaspiコンソールでPDF表示 -2-<br>
> <https://kinneko.fanbox.cc/posts/7414663>

<https://kinneko.fanbox.cc/posts/7414663>

　コマンドラインで動画再生だと、mplayerがあるのだけど、これはソフトウエアデコードで、フレーム落ちが起きてまったくダメらしい。

　GPUが使えるRaspi用の専用環境としては、omxplayerというのがあった。Raspbianの動画ベンチマークなどにも使用されていたようなのだけど、プロジェクトは2020年にPi4対応が十分でないということでvlcのほうにリソースを移行してしまったようだ。もとのホストであったomxplayer.sconde.netも残っていない。

> 問題があったのは、OSDと字幕にopenvgを使用しているがPi4ではサポートされていないこと、openmaxを使っているがこれは非推奨になって長く64bit kernelでは対応していないこと、また動画のデコードがハードウエアのみで、ソフトウエアデコードに対応していないなどの点だそうだ。

　最近の動画再生環境は、コンソールのものも含めてRaspiのハードウエアコーデックにも対応してきているvlcに統一されてきている。

　ただ、vlcをインストールすると282パッケージもインストールされてしまうので、ちょっと多すぎて躊躇する。

　さらに、VLCサポートチームから、こんなステートメントも出ていて、効果低いならどうするかなと悩ましい。

> VLC の次のバージョン (間もなく実現します) では、64 ビットと 32 ビットのほとんどの環境でハードウェア アクセラレーションがサポートされるようになるはずです。 この経路は、OMXplayerによって設定された経路よりも常に効率が低くなり、Linuxによって課せられる制限があり、一部の機能を実現するのが難しいため、OMXplayerとまったく同じことを行うことはできません。

　しかし、omxplayerは、PiZeroな32bit Lite環境のOSでは、まだ十分使えると思う。GPUに対応している動画デコーダー対応を含んでいるというのが一番のメリットだ。

　もし、やってみて、ダメそうならvlcのコマンド版を試してみることにしよう。

　omxplayerのソースコードはここに残されている。

> popcornmix/omxplayer: omxplayer<br>
> <https://github.com/popcornmix/omxplayer>

![](/2024-02-08/7415370-01.png)

　当然ながら、もう標準のパッケージには存在しない...

```text
kinneko@raspberrypi:~ $ apt-cache search omxplayer
```

　自前ビルドか... それは避けたいな...

　さて、インストールしている最新のRaspiOSは、bookwormなのだけど、これはスクリーンの制御がkmsを前提に設計されている。以前は、kms/fkmsのどちらかを選ぶこともできたのだけど、Pi4以降は64bit標準化などとの兼ね合いで、fkmsは廃止されつつある。omxplayerが廃れたのは、このあたりにも原因がある。

　kms/fkmsは、ディスプレイの解像度やリフレッシュレートなどの設定を管理する方法の違いを表している。

　kmsはKernel Mode Settingの略で、これらの設定がkernel内で行われている。最近は普通こちらの実装になる。

　fkmsは、Fake/Firmware Kernel Mode Settingの略で、カーネル内で完全にハードウェア制御を行うのではなく、ファームウェアやユーザースペースのツールと連携して画面設定を行う。完全なKMSのサポートが難しいハードウェアや、リソースが限られているデバイスでよく使用される。Raspiでは、fkmsではGPUというかVPUに対して、直接制御を行うようになっている。

　現在の起動パラメータを確認しても、KMS優先でドライバ側などから自動設定はされないようにブロックされている。

```text
kinneko@raspberrypi:~ $ cat /boot/firmware/config.txt | grep kms
dtoverlay=vc4-kms-v3d
disable_fw_kms_setup=1
```

　デバイスドライバもkmsがロードされているのが確認できる。

```text
kinneko@raspberrypi:~ $ lsmod | grep vc4
vc4                   333682  2
drm_display_helper      6660  1 vc4
cec                    39194  1 vc4
drm_dma_helper          9949  1 vc4
drm_kms_helper        181417  4 drm_dma_helper,vc4
snd_soc_core          242250  2 vc4,snd_soc_hdmi_codec
drm                   521035  5 drm_dma_helper,vc4,drm_display_helper,drm_kms_helper

kinneko@raspberrypi:~ $ lsmod | grep kms
drm_kms_helper        181417  4 drm_dma_helper,vc4
fb_sys_fops             2245  1 drm_kms_helper
syscopyarea             3264  1 drm_kms_helper
sysfillrect             3764  1 drm_kms_helper
sysimgblt               3427  1 drm_kms_helper
drm                   521035  5 drm_dma_helper,vc4,drm_display_helper,drm_kms_helper
```

　bookwormでも、お手軽にraspi-configあたりで設定できないかしらん。raspi-configを起動してみる。

```text
kinneko@raspberrypi:~ $ sudo raspi-config
```

![](/2024-02-08/7415370-02.png)

　「Advanced Options」に「GL Driver」項目がすでにない...

![](/2024-02-08/7415370-03.png)

　現在のドライバには、fkmsドライバは入っていない。

```text
kinneko@raspberrypi:~ $ uname -a
Linux raspberrypi 6.1.0-rpi7-rpi-v6 #1 Raspbian 1:6.1.63-1+rpt1 (2023-11-24) armv6l GNU/Linux

kinneko@raspberrypi:~ $ cat /boot/firmware/config.txt | grep kms
dtoverlay=vc4-kms-v3d
disable_fw_kms_setup=1
```

　あかん。ダメかも。調べても動きそうな話は出てこない...

> New bookworm must boot with kms ？ - Raspberry Pi Forums<br>
> <https://forums.raspberrypi.com/viewtopic.php?t=358235>

　omxplayerは、fkmsで直接GPUパラメータにアクセスして動作するので、kms設定の場合は動作することができない。

　kernelからビルドし直すのは、一過性の実験ならいいのだけど、サポートしてゆくのはしんどいな...

　vlcに日和るか...

---
> オリジナル投稿：<br>
> Raspiコンソールで動画表示 -1-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/7415370>

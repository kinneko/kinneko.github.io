+++
date = "2022-06-29T08:00:00"
draft = false
title = "DigisparkでArduino CLIを試す -5-"
description = "Arduino CLIでDigisparkへの書き込みとコマンド操作を試します。"

[taxonomies]
tags = ["Digispark", "Arduino CLI", "2022-06"]
+++
　ビルドして、バイナリファイルが吐けるようになったので、次は書き込みをする。

　CLIがArduino IDEと違うのは、ビルドと書き込みを連続してやってくれる自動化された方法が提供されないことだ。CLIでは、これらを別々にやる必要がある。

　一発でやれないだけで、たいした手間ではない。むしろビルドするのは一回だけで、毎回やらずにバイナリの書き込みだけやれるので、作業的には楽になるかもしれない。

　ビルドは前回すませているので、アップロードだけを行う。ビルド時に指定したのと同様にFQBNと設定オプションを「-b」で渡し、新規にシリアルポートの情報を「-p」オプションで渡してやる。

```text
pi@pi:~ $ arduino-cli upload -p /dev/ttyAMA0 -b digistump:avr:digispark-tiny:clock=clock165 digispark_sleepless
> Please plug in the device (will time out in 60 seconds) ...
(snip)
```

　「Please plug in the device」が表示されたら、Arduino IDEの時と同様に、DigisparkをUSBに差し込むだけで書き込みが行われる。

　「-i」オプションで、ビルド済みのhexファイルを直接指定することもできる。

```text
pi@pi:~ $ arduino-cli upload -p /dev/ttyAMA0 -b digistump:avr:digispark-tiny:clock=clock165 -i ./digispark_sleepless/build/digistump.avr.digispark-tiny/digispark_sleepless.ino.hex
> Please plug in the device (will time out in 60 seconds) ...
(snip)
```

　Arduino IDEでは、スケッチを開くとボードの設定も設定したものを自動的に反映してくれる。これは、どこかに情報を記録してあるのだろう。

　CLIでビルドするときに、オプションを全部コマンドラインで指定しないといけないのは面倒だ。Arduino IDEと同じように保存しておいて自動適用したい。

　これは「board attach」オプションで指定できるようだ。

```text
pi@pi:~ $ arduino-cli board attach -b digistump:avr:digispark-tiny:clock=clock165 digispark_sleepless
Selected fqbn: digistump:avr:digispark-tiny:clock=clock165
```

　ポートの情報も設定してみたけれど、どうも保存できないようだ。不便だな...

```text
pi@pi:~ $ arduino-cli board attach -p /dev/ttyAMA0 digispark_sleepless
Attach board error: No supported board found at serial:///dev/ttyAMA0
```

```text
pi@pi:~ $ arduino-cli board attach -p /dev/ttyAMA0
Attach board error: Can't open sketch: no valid sketch found in /home/pi: missing /home/pi/pi.ino
```

　スケッチの個別設定は、「sketch.json」ファイルに保存されるようだ。

```text
pi@pi:~ $ cat digispark_sleepless/sketch.json
{
  "cpu": {
    "fqbn": "digistump:avr:digispark-tiny:clock=clock165"
  }
}
```

　というわけで、シリアルポートだけは指定しないといけないようだ。

```text
pi@pi:~ $ arduino-cli upload -p /dev/ttyAMA0  digispark_sleepless
> Please plug in the device (will time out in 60 seconds) ...
(snip)
```

　あとは、簡単なコマンドTipsをメモっておく。

　定期的に、ライブラリやボード情報のアップデートをしておく。

```text
$ arduino-cli core upgrade
```

　インストール済みのライブラリのリスト表示。

```text
$ arduino-cli lib list
```

　あとの細かいオプションは、マニュアルを見てほしい。

> arduino-cli - Arduino CLI<br>
> <https://arduino.github.io/arduino-cli/0.23/commands/arduino-cli/>

　Raspi3は1GBしかRAMがないので、起動時にHDMIが認識していないとメモリ節約になるかどうか調べてみる。あんまり減らない感じなら、RaspiOS Liteを入れたほうがいいかもしれない。そのほうが起動も早くなるだろう。

　HDMI接続起動時。起動直後。

```text
pi@pi:~ $ free -h
               total        used        free      shared  buff/cache   available
Mem:           923Mi       179Mi       467Mi        11Mi       275Mi       680Mi
Swap:           99Mi          0B        99Mi
```

　HDMI取り外し起動時。起動直後。

```text
pi@pi:~ $ free -h
               total        used        free      shared  buff/cache   available
Mem:           923Mi        79Mi       666Mi       1.0Mi       177Mi       792Mi
Swap:           99Mi          0B        99Mi
```

　あんまり変化ないな... RaspiOS Liteにするほうがいいかな。再構築は暇があったらやる予定w

　Arduino CLIを導入したことで、Raspi3だけで製造を自動化する野望にだいぶ近づいてきた。

---
> オリジナル投稿：<br>
> DigisparkでArduino CLIを試す -5-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/4012952>

+++
date = "2023-07-13T08:00:00"
draft = false
title = "Flutter: ソフトキーボードが出ると画面にトラジマが"
description = "Flutterでソフトキーボード表示時に発生するBOTTOM OVERFLOWED表示と、ColumnからListViewへの変更による対処。"

[taxonomies]
tags = ["Flutter", "2023-07"]

[extra]
image = "/2023-07-13/6263156-cover.jpeg"
+++

　入力画面で、ソフトキーボードを表示させると、画面にトラジマのエリアが表示されてしまう。

　こんなやつ。

![](/2023-07-13/6263156-01.png)

　よく見ると、"BOTTOM OVERFLOWED BY 43 PIXELS"と小さく表示されている。

　これはなんだろうと思っていたら、デバッグ用のオーバーレイ表示だそうだ。

　Text()、TextFormField()、Column()などを使っている時に、画面範囲を超えるとエラーとして表示されるということらしい。

　この場合は、Column()の中にTextField()を並べて使っていて、ソフトキーボードで描画エリアが狭くなったので、エラーになってしまったようだ。

　オーバーレイエリアは、Flutterのデバッグモードでのみ表示されるので、リリースモードでは表示されない。

　いつも、flutter runでビルドしていたのは、特にデバッグとか指定していないのだけど、デバッグモードだったのね。

　ビルドをリリースモードで行うと、表示されなくなる。

```text
% flutter run --release
Launching lib/main.dart on Pixel 6a in release mode...
Running Gradle task 'assembleRelease'...                           40.2s
✓  Built build/app/outputs/flutter-apk/app-release.apk (9.5MB).
Installing build/app/outputs/flutter-apk/app-release.apk...      1,781ms

Flutter run key commands.
h List all available interactive commands.
c Clear the screen
q Quit (terminate the application on the device).
```

![](/2023-07-13/6263156-02.png)

　なるほど、確かに出なくなったわ。

　しかし、実害はないのだけど、バグはバグってことね。

　ここでは、Column()をListView()に変更して対処する。

```dart
        //child: Column(
        child: ListView(
```

![](/2023-07-13/6263156-03.png)

　Saveボタンが横長になったのだけど、それは特に問題ないな。

　あとは、Column()のときにはドラッグに反応しなかったのだけど、ListView()にするとドラッグに反応して画面がウネウネする。それは、問題ないかな。

　ウネウネを避けたい事情がある場合は、Column()をSingleChildScrollView()で囲うと、描画がスクリーンをはみ出ていない場合は、ウネウネ動作がなくなるという方法もある。

---
> オリジナル投稿：<br>
> Flutter: ソフトキーボードが出ると画面にトラジマが｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/6263156>

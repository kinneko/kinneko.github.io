+++
date = "2021-07-28T08:00:00"
draft = false
title = "Markdownでプレゼンが書けるSlidevを試す -1-"
description = "Markdownできれいなプレゼンが書けたらいいなと前から思っていたのだけど、なかなかいい感じのツールがなかった。最近、Slidevというツールが出てきたという話を読んだ。さっそく試す。"

[taxonomies]
tags = ["Slidev", "Markdown", "2021-07"]

[extra]
image = "/2021-07-28/2494578-title.jpeg"
+++
　Markdownできれいなプレゼンが書けたらいいなと前から思っていたのだけど、なかなかいい感じのツールがなかった。最近、Slidevというツールが出てきたという話を読んだ。さっそく試す。

　Slidevの読み方は、発音記号でslʌɪdɪv。カタカナにすると「スラィディブ」かな。確認は発音記号読み上げサイト「IPA Reader」が使える。 http://ipa-reader.xyz/

　本家サイトはこちら。

> Home | Slidev<br>
> <https://sli.dev/>

![](/2021-07-28/2494578-01.png)

　画面の上のほうに黄色っぽい吹き出しに警告が書かれている。"Slidev is still under heavy development. API and usages are not set in stone yet. "（Slidevはまだ開発中だ。APIと使用方法はまだ確定していない。）

　ソースコードはGithubにある。タイムスタンプを見ると、ほとんど毎日更新されているのがわかる。作者のAnthony Fuさんは、Vue.jsのコアチームメンバーなのだそうだ。期待できそう。

> slidevjs/slidev: Presentation Slides for Developers (Beta)<br>
> <https://github.com/slidevjs/slidev>

　34秒で何ができるかがわかるデモ動画はこちら。わかるんだけど、わからないw 使ってみないとダメだな。

> デモ動画 - YouTube<br>
> <https://www.youtube.com/watch?v=eW7v-2ZKZOU>

　はじめ方はここ。

> Getting Started | Slidev<br>
> <https://sli.dev/guide/>

　動作にはnode.jsの14以降が必要だそうだ。nodeがあればnpmでインストールできる。

　nodeのインストールは少しやっかいで、「M1 MBPにnode.jsをインストールする」に書いた通りだ。

　nodeをx86_64環境で実行するシェルを起動する。

````text
kinneko@kinnekonoMacBook-Pro ~ % arch -x86_64 zsh
kinneko@kinnekonoMacBook-Pro ~ % arch
i386
kinneko@kinnekonoMacBook-Pro ~ % nvm current
v14.17.3
kinneko@kinnekonoMacBook-Pro ~ % node -v
v14.17.3
````

　slidevをインストールする。

````text
kinneko@kinnekonoMacBook-Pro ~ % npm init slidev@latest
npx: 22個のパッケージを4.414秒でインストールしました。
````

````text
●■▲
Slidev Creator  v0.22.5

✖ Project name: … slidev
````

　プロジェクト名を聞かれた。いきなりinitされたのかな？

　めんどくさいので、一旦強制終了して、コマンドラインで使えるようにグローバルインストールにする。

````text
kinneko@kinnekonoMacBook-Pro ~ % npm i -g @slidev/cli
^[OP⸨   ░░░░░░░░░░░░░░░⸩ ⠏ fetchMetadata: sill resolveWithNewModule gray-matter@
/Users/kinneko/.nvm/versions/node/v14.17.3/bin/slidev -> /Users/kinneko/.nvm/versions/node/v14.17.3/lib/node_modules/@slidev/cli/bin/slidev.js

> esbuild@0.12.15 postinstall /Users/kinneko/.nvm/versions/node/v14.17.3/lib/node_modules/@slidev/cli/node_modules/esbuild
> node install.js


> vue-demi@0.11.2 postinstall /Users/kinneko/.nvm/versions/node/v14.17.3/lib/node_modules/@slidev/cli/node_modules/vue-demi
> node ./scripts/postinstall.js

+ @slidev/cli@0.22.5
added 280 packages from 1175 contributors in 79.527s
````

　インストールされた模様。

````text
kinneko@kinnekonoMacBook-Pro ~ % slidev --version
0.22.5
````

````text
kinneko@kinnekonoMacBook-Pro ~ % slidev --help
slidev [args]

コマンド:
slidev [entry]             Start a local server for Slidev        [デフォルト]
slidev build [entry]       Build hostable SPA
slidev format [entry]      Format the markdown file
slidev theme [subcommand]  Theme related operations
slidev export [entry]      Export slides to PDF

位置:
entry  path to the slides markdown entry    [文字列] [デフォルト: "slides.md"]

オプション:
-t, --theme    overide theme                                          [文字列]
-p, --port     port                                                     [数値]
-o, --open     open in browser                      [真偽] [デフォルト: false]
--remote   listen public host and enable remote control
[真偽] [デフォルト: false]
--log      log level
[文字列] [選択してください: "error", "warn", "info", "silent"] [デフォルト:
"warn"]
-f, --force    force the optimizer to ignore the cache and re-bundle
[真偽] [デフォルト: false]
-h, --help     ヘルプを表示                                             [真偽]
-v, --version  バージョンを表示                                         [真偽]
````

　slides.mdがデフォルトのmdファイルのようだ。起動時にファイル名を渡してやると、任意のmdファイル名を使うことができる。slidevTestディレクトリを掘って、そこにtest.mdを作る。

````text
kinneko@kinnekonoMacBook-Pro ~ % mkdir -p ~/Documents/slidevTest
kinneko@kinnekonoMacBook-Pro ~ % cd ~/Documents/slidevTest
kinneko@kinnekonoMacBook-Pro slidevTest % vi test.md
kinneko@kinnekonoMacBook-Pro slidevTest % cat test.md
# Slidev

Hello World

---

# Page 2

Directly use code blocks for highlighting

```ts
console.log('Hello, World!')
```

---

# Page 3
````

　test.mdを指定して、slidevサーバーを起動する。

````text
kinneko@kinnekonoMacBook-Pro slidevTest % slidev test.md
? The theme "@slidev/theme-default" was not found globally, do you want to install it now? › (Y/n)
````

　テーマの指定をしていないので、デフォルトのテーマでいいか聞かれた。とりあえずデフォルトで起動する。

````text
kinneko@kinnekonoMacBook-Pro slidevTest % slidev test.md
✔ The theme "@slidev/theme-default" was not found globally, do you want to install it now? … yes
+ @slidev/theme-default@0.19.1
added 5 packages from 2 contributors in 5.895s
^[OP

●■▲
Slidev  v0.22.5 (global)

theme   @slidev/theme-default
entry   /Users/kinneko/Documents/slidevTest/test.md

slide show      > http://localhost:3030/
presenter mode  > http://localhost:3030/presenter
remote control  > pass --remote to enable

shortcuts       > restart | open | edit
````

　これで起動しているようだ。http://localhost:3030/をブラウザで開いてみると、以下のようなプレゼンができるようになっていた。

![](/2021-07-28/2494578-02.png)

![](/2021-07-28/2494578-03.png)

![](/2021-07-28/2494578-04.png)

　プレゼン終わりの画面は、自分で作らなくても自動で表示してくれるようだ。

![](/2021-07-28/2494578-05.png)

　画面の右下にカーソルを持っていくと、ツールバーが表示される。

![](/2021-07-28/2494578-06.png)

　ナナメの矢印はフルスクリーンモードへの切り替えのようだ。左右の矢印はページ送り。四角が並んでいるのはサムネイル表示。

![](/2021-07-28/2494578-07.png)

　お日様アイコンは、ダークモードへの切り替えだった。

![](/2021-07-28/2494578-08.png)

![](/2021-07-28/2494578-09.png)

　丸に人型があるアイコンは、カメラ表示をオーバーレイする機能だった。ブラウザでカメラの利用を許可すると、右下に丸くトリミングされたカメラの映像が表示される。

![](/2021-07-28/2494578-10.png)

　カメラ表示部分は、任意の場所にドラッグで移動できる。サイズの変更はできないようだ。オンラインで実施するプレゼンを作るときには、このサイズを空けておくことを意識するといいかもしれない。

![](/2021-07-28/2494578-11.png)

　カメラアイコンでは、プレゼンの録画ができるようだ。マイクの利用が許可されていると録音もできるので、事前に録画が必要な場合には便利そう。フォーマットはwebmになるようだ。

![](/2021-07-28/2494578-12.png)

　マイク付きの人型アイコンでは、プレゼンテーションモードになった。右上には経過時間も表示されている。ノートや次のスライドも表示されている。

![](/2021-07-28/2494578-13.png)

　鉛筆アイコンは、マーカーで書き込みできるのかと思ったら、インタラクティブな編集モードになった。

![](/2021-07-28/2494578-14.png)

　スライダーアイコンは、表示部分のサイズが調整できるようだ。ブラウザ画面にフィットさせるのがデフォルトで、あとは1:1を選ぶことができる。たぶん、実寸的なことだろうか？

![](/2021-07-28/2494578-15.png)

　1:1を選択すると額縁がついた感じになった。

![](/2021-07-28/2494578-16.png)

　とりあえず基本的な機能がわかった。これだけでも、コロナ下でのリモートプレゼン時代のツールとして、なかなか細かい作り込みがされているのがわかる。

　次はマークダウンの書き方で何が表現できるかを調べてみよう。

---

> オリジナル投稿：<br>
> Markdownでプレゼンが書けるSlidevを試す -1-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/2494578>

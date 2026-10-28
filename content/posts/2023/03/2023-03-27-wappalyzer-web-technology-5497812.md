+++
date = "2023-03-27 08:00:00"
draft = false
title = "WappalyzerでWebターゲットの状態を把握する"
description = "Wappalyzerは。見ているWebサイトが、どんなバックエンド技術で構築されているか分析するブラウザプラグイン。"

[taxonomies]
tags = ["Wappalyzer", "Firefox", "2023-03"]

[extra]
image = "2023-03-27/5497812-title.jpeg"
+++

　Wappalyzerは。見ているWebサイトが、どんなバックエンド技術で構築されているか分析するブラウザプラグイン。

　便利そうなので入れてみる。本家はこちら。

> Find out what websites are built with - Wappalyzer<br>
> <https://www.wappalyzer.com/>

![](/2023-03-27/5497812-01.png)

　画面の下のほうに、対応している環境の一覧があるので、その中から、自分が使っているFirefoxを選ぶとアドオンのページに移動した。

> Wappalyzer by Wappalyzer<br>
> <https://addons.mozilla.org/en-US/firefox/addon/wappalyzer/>

![](/2023-03-27/5497812-02.png)

　通常通りインストールすると、別のタブでインストール成功の画面が表示される。動画で簡単な使い方が解説されている。

> Installation successful - Wappalyzer<br>
> <https://www.wappalyzer.com/installed/?utm_source=installed&utm_medium=extension&utm_campaign=wappalyzer>

![](/2023-03-27/5497812-03.png)

　アドオンはデフォルトでは有効にならないようだ。設定を開いて、OKを押す。

![](/2023-03-27/5497812-04.png)

　先程のページで結果を見る。なるほど、いろいろなパーツが使われているのがわかる。

![](/2023-03-27/5497812-05.png)

　しかし、こいつのせいか、タブを開きすぎているせいなのかわからないけど、firefoxが死ぬほど重くなったので、オフにしてFirefoxを再起動した。必要なときだけONにすることにしよう。

　再起動したあとにONにしてみたけど、重くなった様子はない。原因はタブの開きすぎかw

![](/2023-03-27/5497812-06.png)

　それぞれの技術のリンクを開くと、利用傾向などがわかるページが開く。これが便利かと言われるとそうでもない感じ。

![](/2023-03-27/5497812-07.png)

　表示の右上にあるスイッチで、サイトごとのオンオフを設定できる。

　月のマークは、ダークモードの表示切り替え用。

　歯車アイコンは設定。Firefoxでは機能拡張の設定ページが開く。

![](/2023-03-27/5497812-08.png)

　できる設定はそれほどない。

![](/2023-03-27/5497812-09.png)

　Exportボタンで、表示されている内容をCSVで保存できる。

![](/2023-03-27/5497812-10.png)

　MORE INFOタブを開くと、$9/月のプランがあると表示される。発行されるAPIキーを投入すると使えるようだ。

![](/2023-03-27/5497812-11.png)

　WappalyzerのソースコードはGithubにある。

> GitHub - wappalyzer/wappalyzer: Identify technology on websites.<br>
> <https://github.com/wappalyzer/wappalyzer>

　判定用のJSONファイルであるapps.jsonを見ると、HTTPヘッダ、Cookie、JavaScriptなどに含まれている文字列から判定しているようだ。

　拡張機能を使いたくないのであれば、WappalyzerのサイトからURLを入力することで調べることもできる。

![](/2023-03-27/5497812-12.png)

![](/2023-03-27/5497812-13.png)

　ただし、ユーザー認証が必要なWebサイトでは何も表示されない。

![](/2023-03-27/5497812-14.png)

　ただし、これが使えるのは1回こっきりで、次はサインインページに誘導された。

![](/2023-03-27/5497812-15.png)

---
> オリジナル投稿：<br>
> WappalyzerでWebターゲットの状態を把握する｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/5497812>

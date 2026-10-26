+++
date = "2023-01-27 08:00:00"
draft = false
title = "Route53でドメインを登録してみる"
description = "サブドメインの登録と運用などはやったことがあるけど、ドメインまるごとのゾーン管理をRoute53でやったことがなかった。やるチャンスがあったので、やってみた。"

[taxonomies]
tags = ["AWS", "Route 53", "DNS", "2023-01"]

[extra]
image = "2023-01-27/5141754-cover.jpeg"
+++
　サブドメインの登録と運用などはやったことがあるけど、ドメインまるごとのゾーン管理をRoute53でやったことがなかった。やるチャンスがあったので、やってみた。

　残念ながら、.希望の第二レベルドメインは、comは取得済みだったので、jpにする。

　AWSでjpドメインの取得はできないので、対応したレジストラで取得して、Route53のDNSを指定してもらうということになる。

　と、思ったら、AWSは、jpも対応してたわ。前はできなかったのだけどな... 可能になったってアナウンスあった？

　ダッシュボードにあった、「ドメインの登録」で一応jpドメイン入力してみたら、表示出てきた。

![](/2023-01-27/5141754-01.png)

![](/2023-01-27/5141754-02.png)

　年間$90とか出てきた。えらく高くね？ jpドメインだと年3k円くらいだと思うのだけど。

　今回は、金額の高さと管理の都合上、別に取得してもらう必要があるので、お名前.comで取得してもらった。いや、お名前.com使うのどうかとは思うのだけど... そのへんは選択権がなかったわ。

　Route53のメニューから「ホストゾーン」を選ぶ。いまのところ、管理しているドメインのゾーンは１つもない。オレンジ色の「ホストゾーンの作成」ボタンがあるので押す。

![](/2023-01-27/5141754-03.png)

　「ホストゾーンの作成」画面に移動する。

![](/2023-01-27/5141754-04.png)

　「ホストゾーン設定」には３つの入力項目がある。

・ドメイン名

　ホストするドメイン名を入れる。

・説明

　なんでもいい。メモ的なものなので、今回は何も入れない。

・タイプ

　インターネットから引ける名前を運用するので、「パブリックホストゾーン」を選ぶ。

　「プライベートホストゾーン」はVPC内で名前引きを提供するときに使う。

　入力して、画面右下にあるオレンジ色の「ホストゾーンの作成」ボタンを押す。

![](/2023-01-27/5141754-05.png)

　登録されたので、「ホストゾーンの詳細」を表示する。

![](/2023-01-27/5141754-06.png)

　「ネームサーバー」のところに、４つホストが書かれている。これを、レジストラのインターフェイスからNSとして登録する。通常はns.[なんとかかんとか].jpという名前で登録される。ns1-4みたいになっていることもある。

　お名前.comの場合は、dns1.onamae.com、dns2.onamae.comにNSレコードが割り当てられているようだ。

![](/2023-01-27/5141754-07.png)

　お名前.comでドメイン名を取得した段階では、whoisで登録情報を確認すると、以下のようになっている。

```text
$ whois mozomozo.jp
[ JPRS database provides information on network administration. Its use is    ]
[ restricted to network administration purposes. For further information,     ]
[ use 'whois -h whois.jprs.jp help'. To suppress Japanese output, add'/e'     ]
[ at the end of command, e.g. 'whois -h whois.jprs.jp xxx/e'.                 ]
Domain Information:
[Domain Name]                   MOZOMOZO.JP
[Registrant]                    (Not displayed by registrant's request)
                                For details -> https://jprs.jp/about/dom-rule/whois-concealment/ (only in Japanese)
[Name Server]                   dns1.onamae.com
[Name Server]                   dns2.onamae.com
[Signing Key]
[Created on]                    2023/01/18
[Expires on]                    2024/01/31
[Status]                        Active
[Last Updated]                  2023/01/18 15:20:37 (JST)
Contact Information:
[Name]                          Whois Privacy Protection Service by onamae.com
[Email]                         proxy@whoisprotectservice.com
[Web Page]
[Postal code]                   150-8512
[Postal Address]                Shibuya-ku
                                26-1 Sakuragaoka-cho
                                Cerulean Tower 11F
[Phone]                         +81.354562560
[Fax]
```

　ドメインの取得を依頼した担当者に、ネームサーバーの４つのアドレスを連絡して、更新してもらうと以下のようになる。

```text
$ whois mozomozo.jp
[ JPRS database provides information on network administration. Its use is    ]
[ restricted to network administration purposes. For further information,     ]
[ use 'whois -h whois.jprs.jp help'. To suppress Japanese output, add'/e'     ]
[ at the end of command, e.g. 'whois -h whois.jprs.jp xxx/e'.                 ]
Domain Information:
[Domain Name]                   MOZOMOZO.JP
[Registrant]                    (Not displayed by registrant's request)
                                For details -> https://jprs.jp/about/dom-rule/whois-concealment/ (only in Japanese)
[Name Server]                   ns-XXXX.awsdns-46.org
[Name Server]                   ns-XXXX.awsdns-21.co.uk
[Name Server]                   ns-XXX.awsdns-51.com
[Name Server]                   ns-XXX.awsdns-57.net
[Signing Key]
[Created on]                    2023/01/18
[Expires on]                    2024/01/31
[Status]                        Active
[Last Updated]                  2023/01/20 14:08:47 (JST)
Contact Information:
[Name]                          Whois Privacy Protection Service by onamae.com
[Email]                         proxy@whoisprotectservice.com
[Web Page]
[Postal code]                   150-8512
[Postal Address]                Shibuya-ku
                                26-1 Sakuragaoka-cho
                                Cerulean Tower 11F
[Phone]                         +81.354562560
[Fax]
```

　さて、ドメインの管理をまるごと受けてしまったので、メールやらなんやら準備するものが多いな。めんどくさいことだ。

---
> オリジナル投稿：<br>
> Route53でドメインを登録してみる｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/5141754>

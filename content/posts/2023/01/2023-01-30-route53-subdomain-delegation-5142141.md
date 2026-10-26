+++
date = "2023-01-30 08:00:00"
draft = false
title = "Route53 to Route53でサブドメインを委譲してみる"
description = "前に、他で運用しているドメインのサブドメインを委譲してもらってRoute53で運用しているのだけど、Route53で運用中のドメインのサブドメインの委譲をやったことはなかった。"

[taxonomies]
tags = ["AWS", "Route 53", "DNS", "2023-01"]

[extra]
image = "2023-01-30/5142141-cover.jpeg"
+++
　前に、他で運用しているドメインのサブドメインを委譲してもらってRoute53で運用しているのだけど、Route53で運用中のドメインのサブドメインの委譲をやったことはなかった。

　基本は同じなんだろうけど。

　状況は、本番用のAWSアカウトにRoute53でドメインを登録して、開発上のAWSアカウントのRoute53にサブドメインを登録委譲して、そのサブドメインを開発用に使うという感じ。

　サービススタート前なので、AWSアカウントを分けて運用するのはコスト面で意味がないと思うのだけど、先方のポリシーがそうなっているので、しょうがないしょうがない。

　作業としては、mozomozo.jpを本番用AWSアカウントに設定して、dev.mozomozo.jpを開発用AWSアカウントに設定して、サブドメインの権限委譲を行う。

　たとえば、Webサーバーを運用するとして、本番はwww.mozomozo.jpでアクセスできるようにして、開発時はwww.dev.mozomozo,jpでアクセスできるようにするという感じ。

　一応、AWSからガイドドキュメントは出ているので、それに従う。

> Route 53 を使用してホストされるドメインのサブドメインの作成<br>
> <https://aws.amazon.com/jp/premiumsupport/knowledge-center/create-subdomain-route-53/>

　まずは、サブドメインを運用するAWSアカウントでRoute53を開く。「ホストゾーンの作成」を選ぶ。

![](/2023-01-30/5142141-01.png)

　ドメイン名のところに、管理委譲を受けるサブドメイン名を入力する。ここではdevとする。

　パブリックホストゾーンを選んで「ホストゾーンの作成」ボタンを押す。

![](/2023-01-30/5142141-02.png)

　登録完了。

![](/2023-01-30/5142141-03.png)

　「ホストゾーンの詳細」からネームサーバー４つをメモる。

![](/2023-01-30/5142141-04.png)

　この時点で、AUTHORITY SECTIONの設定を確認する。まだサブドメインに権限委譲されていないので、mozomozo.jpになっている。

```text
$ dig -q dev.mozomozo.jp
; <<>> DiG 9.18.1-1ubuntu1.2-Ubuntu <<>> -q dev.mozomozo.jp
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 58309
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;dev.mozomozo.jp.			IN	A
;; AUTHORITY SECTION:
mozomozo.jp.		208	IN	SOA	ns-XXX.awsdns-XXX.net. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 86400
;; Query time: 40 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Fri Jan 20 05:48:19 UTC 2023
;; MSG SIZE  rcvd: 126
```

　ドメインを登録したAWSアカウントに移動して、Route53からサブドメイン名を登録する。

　ホストゾーンで、登録したドメインのホストゾーンを開く。

![](/2023-01-30/5142141-05.png)

　オレンジ色の「レコードを作成」ボタンを押す。

![](/2023-01-30/5142141-06.png)

　「レコードを作成」画面に移動する。

![](/2023-01-30/5142141-07.png)

　レコード名には、サブドメイン名（ここではdev）を入れる。レコードタイプは「NS」を選択する。

![](/2023-01-30/5142141-08.png)

　値に、先ほどコピーした４つのホスト名を入れる。

![](/2023-01-30/5142141-09.png)

　オレンジ色の「レコードを作成」ボタンを押す。

![](/2023-01-30/5142141-10.png)

　変更後のAUTHORITY SECTIONの設定を確認する。サブドメインに権限委譲されているので、dev.mozomozo.jpになっている。

```text
% dig dev.mozomozo.jp
; <<>> DiG 9.10.6 <<>> dev.mozomozo.jp
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 24468
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;dev.mozomozo.jp.			IN	A
;; AUTHORITY SECTION:
dev.mozomozo.jp.		478	IN	SOA	ns-XXXX.awsdns-XXX.org. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 86400
;; Query time: 15 msec
;; SERVER: 2001:268:fd07:4::1#53(2001:268:fd07:4::1)
;; WHEN: Fri Jan 20 16:17:39 JST 2023
;; MSG SIZE  rcvd: 127
```

　TTLは、NSレコードだと172800秒とかを設定するのが一般的なのだけど、AWSのレコードのTTLのデフォルトでは300秒になっているので、AWSではクエリが発生すると課金されるので増やしておくとよい。

---
> オリジナル投稿：<br>
> Route53 to Route53でサブドメインを委譲してみる｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/5142141>

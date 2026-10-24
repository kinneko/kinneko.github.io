+++
date = "2022-11-21T08:00:00"
draft = false
title = "AWS: root/IAMでもMFAデバイスが複数使用可能に！ -1-"
description = "AWSのroot/IAMユーザーに複数のMFAデバイスを登録し、FIDOキーでサインインを確かめる。"

[taxonomies]
tags = ["AWS", "IAM", "MFA", "FIDO", "2022-11"]

[extra]
image = "/2022-11-21/4780029-title.jpeg"
+++

　喜ばしい！

> AWS Identity and Access Management now supports multiple multi-factor authentication (MFA) devices<br>
> <https://aws.amazon.com/jp/about-aws/whats-new/2022/11/aws-identity-access-management-multi-factor-authentication-devices/>

![](/2022-11-21/4780029-02.png)

　でも、もう記事になったりしているのね。先を越されたわ。

> IAMユーザーやAWSアカウントのルートユーザー に複数の MFA デバイスを割り当てる事ができるようになりました | DevelopersIO<br>
> <https://dev.classmethod.jp/articles/multiple-mfa-devices-can-now-be-assigned-to-iam/>

　まぁ、もちょっと詳しく書けばいいだけのこと。

　rootでMFAを設定していない人には、IAM開くとこんな警告が出るので、「MFAを追加」ボタンを押すと設定画面に出る。

![](/2022-11-21/4780029-03.png)

　ところで、すでにMFAを１つ設定してある人は、この画面にはどうやって行くのだ？？？

　以前は、ナビゲーションバーの右端にあるアカウントを開くと、その中にMFA設定に移動するリンクがあった。今はない感じだ。

　そのかわりに「セキュリティ認証情報」があるので、それをクリックすると「セキュリティ認証情報」の画面が表示される。

![](/2022-11-21/4780029-04.png)

　「セキュリティ認証情報」の中に「多要素認証 (MFA)」があるので、クリックすると展開される。中身はまだ英語で日本語化されていない。「MFA を有効化」ボタンがあるので押す。

![](/2022-11-21/4780029-05.png)

　「MFA デバイスの管理」ダイアログが表示される。

![](/2022-11-21/4780029-06.png)

```text
MFA デバイスの管理
名前
Maximum 128 characters. Use alphanumeric and '+ = , . @ - _' characters.
割り当てる MFA デバイスのタイプを選択:
◯ 仮想 MFA デバイス
モバイルデバイスまたはコンピュータにインストールされた Authenticator アプリケーション
◯ Security key
Authenticate by using a FIDO security key, such as Yubikey
◯ その他のハードウェア MFA デバイス
Hardware TOTP token
サポートされている MFA デバイスの詳細については、 AWS Multi-Factor Authentication を参照してください。

```

> IAM - Multi-Factor Authentication<br>
> <https://aws.amazon.com/jp/iam/features/mfa/?audit=2019q1>

　AWS IAM Identity Centerのように鍵の名前は自動登録されて後で自分で変更するのではなく、登録する鍵の名前を自分で決める必要がある。でも、何も入力しないで進めると、勝手に付けてくれる。

![](/2022-11-21/4780029-07.png)

　名前を適当につけて、続行ボタンを押す。

![](/2022-11-21/4780029-08.png)

![](/2022-11-21/4780029-09.png)

　FIDOキーを入れてタッチ。背景の絵も少し変わっている。

![](/2022-11-21/4780029-10.png)

　成功通知はまだ英語。８つまで登録できると書いてある。（ここはもう日本語の前の表示に戻って本数の明記が消えてしまっている。）

![](/2022-11-21/4780029-11.png)

　二本目も同じようにして登録した。というわけで、複数本登録できるのは確認できた。

![](/2022-11-21/4780029-12.png)

　IAMダッシュボードの表示でもレコメンドにチェックが付いている。

![](/2022-11-21/4780029-13.png)

　サインインしてみる。

![](/2022-11-21/4780029-14.png)

　キーの選択などは出てこない。

![](/2022-11-21/4780029-15.png)

　当たり前だけど、普通にできるな。

![](/2022-11-21/4780029-16.png)

　サインインの時のFIDOキーのタッチ面のイラストは、こちらは変更されていない。

![](/2022-11-21/4780029-17.png)

　続く。

> AWS: root/IAMでもMFAデバイスが複数使用可能に！ -2-<br>
> <https://kinneko.fanbox.cc/posts/4785345>

---

> オリジナル投稿：<br>
> AWS: root/IAMでもMFAデバイスが複数使用可能に！ -1-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/4780029>

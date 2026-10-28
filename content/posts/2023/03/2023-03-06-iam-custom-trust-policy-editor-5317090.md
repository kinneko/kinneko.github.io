+++
date = "2023-03-06 08:00:00"
draft = false
title = "カスタム信頼ポリシーのエディタ変だわ"
description = "AWSControlTowerExecutionなIAM Roleを作るのに、カスタム信頼ポリシーを使った。"

[taxonomies]
tags = ["AWS IAM", "AWS Control Tower", "2023-03"]

[extra]
image = "2023-03-06/5317090-cover.jpeg"
+++

　AWSControlTowerExecutionなIAM Roleを作るのに、カスタム信頼ポリシーを使った。

　IAM Roleのカスタム信頼ポリシーの画面のJSONのエディタに、必要なポリシーをペーストした。

![](/2023-03-06/5317090-01.png)

　新しいステートメントを追加ボタンを押す。

　なんかデフォルトで、AssumeRoleのやつが追加された。

![](/2023-03-06/5317090-02.png)

　いやいや、これじゃないということで、ステートメントで「削除」を選ぶ。

　削除するか確認するダイアログが出る。削除ボタンを押す。

![](/2023-03-06/5317090-03.png)

　これで、そのまま進んでしまうと、確認のあとで「Has prohibited field Resource」のエラーでRoleの作成に失敗する。

![](/2023-03-06/5317090-04.png)

　なにやら禁止リソースが定義されているということのようだ。

　エディタに戻る。

![](/2023-03-06/5317090-05.png)

　あれ？ なんか行数多い...

　「"Resource": []」が追加されているよ... なんでだよ...

　というわけで、削除してうまくいった。

---
> オリジナル投稿：<br>
> カスタム信頼ポリシーのエディタ変だわ｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/5317090>

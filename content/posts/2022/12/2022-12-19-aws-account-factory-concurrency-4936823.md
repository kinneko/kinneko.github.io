+++
date = "2022-12-19T08:00:00"
draft = false
title = "AWS: Account Factoryが並列動作可能になった"
description = "AWS Control TowerのAccount Factoryでアカウント作成などの並列操作が可能になった。"

[taxonomies]
tags = ["AWS Control Tower", "Account Factory", "2022-12"]

[extra]
image = "/2022-12-19/4936823-title.jpeg"
+++

　AWS Control Towerで新しいAWSアカウントを作成するのには、Account Factoryという機能を使う。

　実態は、裏でCFnの塊を動かしているのだけど、１つのアカウントの登録処理に40分ほどかかって、かつ、その間は別のアカウントの登録処理を行うことができなかった。そして、たまに詰まって止まったりする。ヤメロ。

　それについて、12/15に予告なしのリリースが出た。

> Introducing concurrent account provisioning operations for AWS Control Tower<br>
> <https://aws.amazon.com/jp/about-aws/whats-new/2022/12/aws-control-tower-concurrent-account-provisioning-operations/>

![](/2022-12-19/4936823-01.png)

> Introducing concurrent account provisioning operations for AWS Control Tower

> Posted On: Dec 15, 2022

> We are excited to announce support for concurrent account factory actions in AWS Control Tower, allowing you to create, update, or enroll up to five accounts at a time. AWS Control Tower account factory makes it easy for you to provision accounts and automate deployment of AWS resources, roles and policies within those accounts to support a range of business functions across your organization. With this new feature enhancement, you now have the autonomy to create and manage your accounts on-demand, supporting greater automation and decreased operational workload.

> When you need to submit an account action, there’s no longer a need to wait for each process to complete before submitting the next or re-registering your entire Organizational Unit (OU). You can now use the same process to submit up to five actions in succession and view completion status of each. As a result, this frees you up to focus on more important tasks while your accounts finish building in the background.

> AWS Control Tower offers a streamlined way to set up and govern a new, secure, multi-account AWS environment based on AWS best practices. Customers will create new accounts using AWS Control Tower’s account factory and enable governance features such as guardrails, centralized logging and monitoring in supported AWS Regions. To learn more, visit the AWS Control Tower homepage or see the AWS Control Tower User Guide. For a full list of AWS Regions where AWS Control Tower is available, see the AWS Region Table.

　また、薄くない本を書き換えないといけない案件。影響が軽微でよかったよ。

> 【年末セール２割引中！】AWS Control Towerの薄くない本<br>
> <https://booth.pm/ja/items/4135460>

　多くのアカウントの取り込みを控えているので、並列動作はありがたい。でも、新規以外でも並列動作できるかは書いてないのだよね。

　案内は、中身的には、「５つまで並列で動作できるようになった」って案内だけ。それ以外のことがまったく書いてないのが笑う。ほんとに、対象が新規登録なのか、既存アカウントの統合も含むのかさえ書かれていない。

　Google様の翻訳はこんな感じ。最後のセンテンスはただの宣伝なので入れていない。

> 『AWS Control Tower での同時アカウント ファクトリ アクションのサポートを発表できることを嬉しく思います。これにより、一度に最大 5 つのアカウントを作成、更新、または登録できます。 AWS Control Tower アカウント ファクトリを使用すると、アカウントを簡単にプロビジョニングし、それらのアカウント内で AWS リソース、ロール、およびポリシーのデプロイを自動化して、組織全体のさまざまなビジネス機能をサポートできます。 この新しい機能強化により、オンデマンドでアカウントを作成および管理する自律性が得られ、自動化の向上と運用ワークロードの削減がサポートされます。

> アカウント アクションを送信する必要がある場合、各プロセスが完了するのを待ってから次のアクションを送信したり、組織単位 (OU) 全体を再登録したりする必要はありません。 同じプロセスを使用して、最大 5 つのアクションを連続して送信し、それぞれの完了ステータスを表示できるようになりました。 その結果、アカウントがバックグラウンドで構築を完了している間、より重要なタスクに集中することができます。』

　ありがたいやら、めんどくさいやら...

---

> オリジナル投稿：<br>
> AWS: Account Factoryが並列動作可能になった｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/4936823>

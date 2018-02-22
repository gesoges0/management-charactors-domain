# make_girls
女の子の画像を自動生成するためのプロジェクトだよ!

プロジェクトの流れ
+ 顔画像の抽出/ 保存
+ 画像のラベル付け

## crop face
画像から顔のみを抽出するよ!
ディレクトリ構成は以下のようなものにする.
wikipediaの放映年代を調べて, yahoo検索から1アニメについて約20の画像をクローリングする.
```sh
anime_img
├1970
｜｜ hoge.png
｜｜ fuga.png
｜｜ piyo.png
├1971
｜　
└2017
```
hoge.pngは以下のような画像になっているよ.
<img src="img/57569.png" alt="元画像" title="元画像"><br>
<img src="img/57569_0.png" alt="元画像" title="元画像">
<img src="img/57569_1.png" alt="元画像" title="元画像">
<img src="img/57569_2.png" alt="元画像" title="元画像">
<img src="img/57569_3.png" alt="元画像" title="元画像">


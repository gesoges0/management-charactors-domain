# make_girls
女の子の画像を自動生成するためのプロジェクトだよ!

プロジェクトの流れ
+ 顔画像の抽出/ 保存
+ 画像のラベル付け

## 顔画像の抽出
画像から顔のみを抽出するよ!
wikipediaの放映年代を調べて, yahoo検索から1アニメについて約20の画像をクローリングしておく.
データの公開が恐らくダメだと思うので自分でやってくだせえ.
ディレクトリ構成は以下のようにして画像をクローリングしてね.
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
次に以下のコードを実行する.
```
$ git clone git@github.com:elasticnet12345/make_girls.git
$ cd make_girls/src
$ python face_crop.py 
```
hoge.pngは以下のような画像になっているよ.
<img src="img/57569.png" alt="元画像" title="元画像"><br>
<img src="img/croped_face.png" alt="croped" title="croped"><br>







# make_girls
女の子の画像を自動生成するためのプロジェクトだよ!
<a href="http://make.girls.moe/#/">make.girls.more</a>を参考にしているよ.

プロジェクトの流れ
+ 顔画像の抽出/ 保存
+ 顔パーツのパラメータ設定

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
アニメ画像のカスケード分類器は<a href="https://github.com/nagadomi/lbpcascade_animeface">ココ</a>からダウンロードしてね.
```
$ git clone git@github.com:elasticnet12345/make_girls.git
$ cd make_girls/src
$ wget https://raw.githubusercontent.com/nagadomi/lbpcascade_animeface/master/lbpcascade_animeface.xml
$ python face_crop.py 
```
hoge.pngは以下のような画像になっているよ.
<img src="img/57569.png" alt="元画像" title="元画像"><br>
抽出した顔画像は以下のようになっているよ.
5人いるけど4人しか抽出されていないのは一定の大きさ以下は画質が悪いデータを学習データになるべく入れたくないため,
一定のサイズ以下の画像は保存しないようにしているからだよ.
<img src="img/croped_face.png" alt="croped" title="croped"><br>

## 顔パーツのパラメータ設定








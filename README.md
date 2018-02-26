# make_girls
女の子の画像を自動生成するためのプロジェクトだよ!
<a href="http://make.girls.moe/#/">make.girls.more</a>を参考にしているよ.

プロジェクトの流れ
+ 顔画像の抽出/ 保存
+ 顔パーツのパラメータ設定

## 顔画像の抽出
画像から顔のみを抽出するよ!
wikipediaのアニメ一覧を調べて, yahoo検索から1アニメについて約20の画像をクローリングしておく.
あとyahoo検索でアニメの名前を検索するより, pixivをクローリングしたほうが良質な画像が得られることが最近わかった.
<a href="http://www.mathgram.xyz/entry/scraping/pixiv">ココ</a>を参考にして!
データの公開が恐らくダメだと思うので自分でやってくだせえ.

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
<a href="http://make.girls.moe/#/">本家</a>で使われているパラメータのうち, <br>
- 髪の色(金, 茶, 黒, 青, 桃, 紫, 緑, 赤, 銀, 白, 橙)
- 髪型(ロング, ショート, ツインテ, ドリルヘア, ポニテ) 
- 目の色(青, 赤, 茶, 緑, 紫, 黄, 桃, 黒, 橙)
- 開口(ON, OFF)
- 帽子(ON, OFF)
- メガネ(ON, OFF)

顔パーツを登録する操作を単純化するために下のようなGUIを作った(制作途中).
各画像に対して引数--dst_dirで指定したディレクトリにJSONファイルを吐く.
ある程度JSONファイルが溜まったら, CSVに統合しデータベースをつくる.
```
$ python set_label_GUI.py --src_dir=data --dst_dir=json_output
```
<img src="img/GUI.png" alt="set_label_GUI" title="set_label_GUI"><br>
<img src="img/s_GUI_operation.png" alt="operation GUI" title="operation GUI"><br>
一通り終わったら, 顔画像が入っているディレクトリとGUIで顔パーツの情報を入力してJSONを作った出力先のディレクトリの2つを以下のようなディレクトリ構成でdata直下に入れる.
GUIの操作が時間がかかるため途中でも後からデータを追加できるので, そのときはコードをいじって!
```sh
anime_img
└ data
  └ dcgan_upload_directory
     ├ face_images 
     |    | hoge.png
     |    | fuga.png
     └ face_images_output
          | hoge.json
          └ fuga.json
```
このJSONをCSVファイルに統合する.
```sh
$ python union.py
```
次に, 学習データセットの作成を行う.
例えば金髪のロングヘアー, 緑目の女の子を生成したいと思ったら, 以下のように実行する.
引数--dataset_directoryは, data直下に今まで追加してきた画像について引数で指定した条件の女の子のみがコピーされる.
```sh
$ python crate_dataset.py --height_size=256 --width_size=256 --hair_color="gold" --hair_type="long" --eye_color="green" --dataset_directory dataset1
```
これを実行すると"data/dataset1"に以下のようなファイルが出力される.
<img src="img/gold_hair_green_eye.png" alt="gold_green" title="金髪ロング緑目"><br>






import os
import csv
import argparse
from tqdm import tqdm
from PIL import Image

args_hair_color_list = ["gold", "brown", "red", "orange", "pink", "black", "blue", "pirple", "green", "white", "silver"]
args_hair_type_list = ["long" , "short", "twinte", "drille", "ponite"]
args_eye_color_list = ["blue", "pirple", "red", "brown", "green", "yellow", "pink"]

def translate_color(color:str):
    """ GUIで設定したcolorとの対応のため, ここで変換する
    """
    if color=="light goldenrod":return "gold"
    elif color=="sienna1":return "brown"
    elif color=="red":return "red"
    elif color=="dark orange":return "orange"
    elif color=="Light Pink3":return "pink"
    elif color=="black":return "black"
    elif color=="blue":return "blue"
    elif color=="purple":return "purple"
    elif color=="white":return "white"
    elif color=="silver":return "silver"
    elif color=="green":return "green"
    elif color=="yellow":return "yellow"

if __name__ == "__main__":
    # 引数設定
    parser = argparse.ArgumentParser()
    parser.add_argument('--height_size', type=int, default=None)
    parser.add_argument('--width_size', type=int, default=None)
    parser.add_argument('--hair_color', type=str, default=None)
    parser.add_argument('--hair_type', type=str, default=None)
    parser.add_argument('--eye_color', type=str, default=None)
    parser.add_argument('--mouth_open', type=bool, default=False)
    parser.add_argument('--hat', type=bool, default=False)
    parser.add_argument('--glasses', type=bool, default=False)
    parser.add_argument('--dataset_directory', type=str, default=None)
    args = parser.parse_args()

    # データセット出力先のディレクトリ
    if not args.dataset_directory:
        print("please specify --dataset_directory")
        print("-- exit --")
        exit()
    else:
        path_dataset_directory = os.path.join("..","data","{}".format(args.dataset_directory))
        
    # サイズの設定
    if not args.height_size:
        print("please specify --height_size")
        print("-- exit --")
        exit()
    if not args.width_size:
        args.width_size = args.height_size

    # 顔パーツの設定
    if not args.hair_color or args.hair_color not in args_hair_color_list:
        print("please specify --hair_color from this list:", args_hair_color_list)
        print("-- exit --")
        exit()
    if not args.hair_type or args.hair_type not in args_hair_type_list:
        print("please specify --hair_type from this list:", args_hair_color_list)
        print("-- exit --")
        exit()
    if not args.eye_color or args.eye_color not in args_eye_color_list:
        print("please specify --eye_color from this list:", args_eye_color_list)
        exit()
    if type(args.mouth_open) != bool:
        print("pleaser specify --mouth_open in bool value: True or False")
        print("-- exit --")
        exit()
    if type(args.hat) != bool:
        print("pleaser specify --hat in bool value: True or False")
        print("-- exit --")
        exit()
    if type(args.glasses) != bool:
        print("pleaser specify --glasses in bool value: True or False")
        print("-- exit --")
        exit()

    # データ用のディレクトリ作成
    if os.path.exists(path_dataset_directory):
        print("please remove dataset or rename dataset directory")
        print("-- exit --")
        exit()
    if not os.path.exists(path_dataset_directory):
        print("mkdir {}".format(path_dataset_directory))
        os.system("mkdir {}".format(path_dataset_directory))

    # 学習データセット(csvと画像ディレクトリ)の作成
    path = "../data/dcgan_upload_directory"
    path_csv = os.path.join(path, "face_parts_info_00.csv")
    with open(path_csv, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        cnt = 0
        for info_img in tqdm(reader):
            # 髪色について
            name_file, directory, hair_color, hair_type, eye_color, flag_mouth, flag_hat, flag_glasses = info_img
            if translate_color(hair_color)==args.hair_color and hair_type==args.hair_type and translate_color(eye_color)==args.eye_color:
                print(cnt, info_img)
                cnt += 1
                
                path_img = os.path.join("../data/dcgan_upload_directory/{}/{}".format(directory, name_file))
                # Imageで読み込み
                img = Image.open(path_img)
                # リサイズ
                img_resized = img.resize((args.height_size, args.width_size))
                # データセットに追加
                path_dst_img = os.path.join(path_dataset_directory, name_file)
                img_resized.save(path_dst_img)





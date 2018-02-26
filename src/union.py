# 個々の画像に対するJSONを統合したCSVを作成する


import csv
import json
import os


if __name__ == "__main__":
    # csv を宣言する
    path_csv_dir = "..\\data\\dcgan_upload_directory"
    new_no = 0
    path_csv_file = os.path.join(path_csv_dir, "face_parts_info_%02d.csv"%new_no)
    header = ["name_img", "path_img", "hair_color", "hair_type", "eye_color", "opend_mouse", "flags_hat", "flags_grasses"]
    with open(path_csv_file, "w") as f:
        writer = csv.writer(f, lineterminator="\n")
        # header 書き込み
        writer.writerow(header)

        # json を読み込む
        no_dir = [1,5]
        paths_dir = ["..\\data\\dcgan_upload_directory\\image{}_face_output".format(no) for no in no_dir]
        for path_dir in paths_dir:
            for name_file in os.listdir(path_dir):
                # json読み込み
                path_json = os.path.join(path_dir, name_file)
                with open(path_json, "r") as jf:
                    json_dict = json.load(jf)
                    # 画像の名前
                    name_img_file = os.path.split(json_dict["file_img"])[1]
                    # 画像があるディレクトリの名前
                    name_directory = json_dict["file_img"].split("\\")[5]# ここは画像が保存されているディレクトリの名前になるようにする
                    # 画像の情報
                    img_info = list()
                    for key, val in json_dict.items():
                        img_info.append(val)
                    writer.writerow([name_img_file] + [name_directory] + img_info[1:])
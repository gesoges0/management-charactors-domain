import os
import numpy as np
import cv2
from tqdm import tqdm

class IMAGE():
    def __init__(self, path_img):
        # 画像の読み込み
        self.path_img = path_img
        self.img = cv2.imread(path_img)
        self.facerects = None        
        
    def set_croped_face(self):
        """ 顔画像をクロップする
        """
        # 顔画像認識
        img = self.img
        facerects = cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=2, minSize=(50, 50))
        self.facerects = facerects

    def get_croped_face(self):
        """ 顔画像の座標を返す
        """
        return self.facerects


if __name__ == "__main__":
    # カスケード PATH 設定
    path_cascade = ".\\lbpcascade_animeface.xml" #アニメ顔
    cascade = cv2.CascadeClassifier(path_cascade)

    path_src_dir = "..\\..\\pixiv_images\\image7" # 元画像のディレクトリ
    path_dst_dir = "..\\..\\pixiv_images\\image7_face" # 保存先のディレクトリ
    if not os.path.exists(path_dst_dir):
        os.mkdir(path_dst_dir)

    for name_file in os.listdir(path_src_dir):
        path_file = os.path.join(path_src_dir, name_file)
        print(path_file)
        # PNG or JPGでなければ
        ext = os.path.splitext(path_file)[1]
        if ext not in [".png", ".jpg"]:continue
        # 画像オブジェクトの宣言
        obj_img = IMAGE(path_file)
        # 顔画像の座標を取得
        faces_coodinates= obj_img.set_croped_face()
        faces_rect = obj_img.get_croped_face()
        if not len(faces_rect):continue
        # 各顔のオブジェクトを保存
        cnt = 0
        for i, rect in enumerate(faces_rect):
            x, y, width, height = rect
            dst_path_file = os.path.join(path_dst_dir, "{}_{}{}".format(name_file.replace(".png","").replace(".jpg",""), cnt, ext))
            # ".\\anime_img12\\{}\\{}_{}.png".format(year, name_file.replace(".png",""), cnt)
            cv2.imwrite(dst_path_file, obj_img.img[y:y+height, x:x+width])
        

        
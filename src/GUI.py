# -*- coding: utf8 -*-
import sys
import os
from PIL import Image, ImageTk
import tkinter 
import argparse


color_list = ["金", "茶", "赤", "橙", "桃", "黒", "青", "紫", "緑", "白", "銀", "黄"]
hair_color_list = ["金", "茶", "赤", "橙", "桃", "黒", "青", "紫", "緑", "白", "銀"]
hair_type_list = ["ロング", "ショート", "ツインテ", "ドリル", "ポニテ"]
eye_color_list = ["青", "紫", "赤", "茶", "緑", "黄", "桃", "黒"]
opend_mouse = ["true", "false"]
flags_hat = ["true", "false"]
flags_glasses = ["true", "false"]

def JapaneseColor2EnglshColor(string):
    """ 日本語から英語に変換するときの処理(色の名前の変換で用いる)
    """
    if string not in color_list:
        return None
    if string == color_list[0]:return "light goldenrod"
    elif string == color_list[1]:return "sienna1"
    elif string == color_list[2]:return "red"
    elif string == color_list[3]:return "dark orange"
    elif string == color_list[4]:return "Light Pink3"
    elif string == color_list[5]:return "black"
    elif string == color_list[6]:return "blue"
    elif string == color_list[7]:return "purple"
    elif string == color_list[8]:return "green"
    elif string == color_list[9]:return "white"# whiteではないことに注意
    elif string == color_list[10]:return "silver"
    elif string == color_list[11]:return "yellow"

def click_registration_button():
    """ RadioButtonがクリックされたときの処理
    """
    print("選択された髪の色:",hair_color_list[v100.get()])
    print("選択された髪型:", hair_type_list[v101.get()])
    print("選択された目の色:", eye_color_list[v102.get()])
    print("選択された開口:", opend_mouse[v103.get()])
    print("選択された帽子:", flags_hat[v104.get()])
    print("選択されたメガネ:", flags_glasses[v105.get()])
    print("=="*20)

    # JSON で出力
    output_dict = {}

class ImageFrame(tkinter.Frame):
    def __init__(self, master, path_img):
        # 画像を読み込む
        print("path_img:",path_img)
        self.obj_img = Image.open(path_img).resize((200, 200))
        self.image = ImageTk.PhotoImage(self.obj_img)
    def set_label(self, ImageFrameObject):
        #ラベルを宣言
        label_img_fig = tkinter.Label(ImageFrameObject, image=self.image)
        label_img_fig.pack(fill=tkinter.BOTH)


if __name__ == "__main__":
    # - * - * - * - * - * - * - * - * - * - * - * -
    # - * - * - * - * -  引数の設定 - * - * - * - * -
    # - * - * - * - * - * - * - * - * - * - * - * -
    parser = argparse.ArgumentParser()
    parser.add_argument('--src_dir', type=str, default=None)
    parser.add_argument('--dst_dir', type=str, default=None)
    args = parser.parse_args()
    print(args.src_dir)
    print(os.listdir(args.src_dir))

    if args.src_dir==None and args.dst_dir==None:
        print("please specify --src_dir and --dst_dir")
        exit()
    
    # src_dir からPNG画像のPATHを取得
    path_src_dir = args.src_dir
    path_src_png_imgs = [os.path.join(path_src_dir, name_file) for name_file in os.listdir(path_src_dir)]


    # - * - * - * - * - * - * - * - * - * - * - * - 
    # - * - * - * - * - GUIの設定 - * - * - * - * - 
    # - * - * - * - * - * - * - * - * - * - * - * -
    root = tkinter.Tk()
    # 第一層フレームの宣言
    f0 = tkinter.Frame(root)
    f1 = tkinter.Frame(root)
    # 第二層フレームの宣言
    f00 = tkinter.Frame(f0)
    #f01 = tkinter.Frame(f0)
    f01 = ImageFrame(f0, path_src_png_imgs[0])
    f01.set_label(f01)
    f02 = tkinter.Frame(f0)
    f10 = tkinter.LabelFrame(f1, text="属性選択")
    f11 = tkinter.Frame(f1)

    # フレームの配置
    # 第一層フレーム
    f0.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    f1.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
    # 第二層フレーム
    f00.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    f01.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    f02.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    f10.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    f11.pack(side=tkinter.TOP, fill=tkinter.BOTH)

    # f00にラベルを配置する
    label_img_name = tkinter.Label(f00, bg="green", text="src = 2007/hoge.png")
    label_img_name.pack(fill=tkinter.BOTH)
    
    # f01に画像を表示する
    # obj_img = Image.open("./sample/91913_0.png")
    # obj_img = obj_img.resize((200, 220))
    # image = ImageTk.PhotoImage(obj_img)
    # label_img_fig = tkinter.Label(f01, image=image)
    # label_img_fig.pack(fill=tkinter.BOTH)

    # f02に仮背景を設定
    label_kari_name = tkinter.Label(f02, bg="green", text="仮")
    label_kari_name.pack(fill=tkinter.BOTH)

    # - - - - - - f10の設定 - - - - - - 
    # 髪の色
    f100 = tkinter.LabelFrame(f10, text="髪の色", relief="sunken", bg="white")
    v100 = tkinter.IntVar()
    v100.set(0)
    for i, hair_color in enumerate(hair_color_list):
        tkinter.Radiobutton(f100, text=hair_color, fg=JapaneseColor2EnglshColor(hair_color), bg="white", activebackground="black",  value=i, variable=v100).pack(side=tkinter.LEFT, fill=tkinter.BOTH)   
    f100.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    # 髪型
    f101 = tkinter.LabelFrame(f10, text="髪型", relief="sunken")
    v101 = tkinter.IntVar()
    v101.set(0)
    for i, hair_type in enumerate(hair_type_list):
        tkinter.Radiobutton(f101, text=hair_type, activebackground="black", value=i, variable=v101).pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    f101.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    # 目の色
    v102 = tkinter.IntVar()
    v102.set(0)
    f102 = tkinter.LabelFrame(f10, text="目の色", relief="sunken")
    for i, eye_color in enumerate(eye_color_list):
        tkinter.Radiobutton(f102, text=eye_color, activebackground="black", fg=JapaneseColor2EnglshColor(eye_color), value=i , variable=v102).pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    f102.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    # 開口
    v103 = tkinter.IntVar()
    v103.set(0)
    f103 = tkinter.LabelFrame(f10, text="開口", relief="sunken")
    for i, flag_opend_mouse in enumerate(opend_mouse):
        tkinter.Radiobutton(f103, text=flag_opend_mouse, value=i , activebackground="black",  variable=v103).pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    f103.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    # 帽子
    v104 = tkinter.IntVar()
    v104.set(0)
    f104 = tkinter.LabelFrame(f10, text="帽子", relief="sunken")
    for i, flag_hat in enumerate(flags_hat):
        tkinter.Radiobutton(f104, text=flag_hat, value=i , activebackground="black", variable=v104).pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    f104.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    # メガネ
    v105 = tkinter.IntVar()
    v105.set(0)
    f105 = tkinter.LabelFrame(f10, text="メガネ", relief="sunken")
    for i, flag_glasses in enumerate(flags_glasses):
        tkinter.Radiobutton(f105, text=flag_glasses, value=i, activebackground="black", variable=v105).pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    f105.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    


    # - - - - - - f11の設定 - - - - - -
    button110 = tkinter.Button(f11, text="この内容で登録", command=click_registration_button)
    button110.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    button111 = tkinter.Button(f11, text="削除する")
    button111.pack(side=tkinter.TOP, fill=tkinter.BOTH)
    


    root.mainloop()

    
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



# class Application(tkinter.Frame):
#     def __init__(self, master=None):
#         # 継承, フレームを宣言
#         super().__init__(master)
#         # 継承したフレームを配置
#         self.pack()
        # 画像の指定
class Application():
    def __init__(self):
        self.root = tkinter.Tk()
        
        self.pointer = 0
        self.limit_pointer = len(path_src_png_imgs)
        self.path_img = None
        #self.obj_img = None # cv形式オブジェクト
        self.set_path_img()
        self.set_obj_img()
        print("path_img:", self.path_img)
        
        # ウィジェットの作成
        self.create_widgets()
    
        self.root.mainloop()

    def increment_pointer(self):
        """ self.pointer をインクリメントする
        """
        if self.pointer + 1 != self.limit_pointer:
            self.pointer += 1
        
    def set_path_img(self):
        """ self.path_img をセットする
            self.path_img は path_src_png_imgs におけるself.pointer の指すものである
        """
        self.path_img = path_src_png_imgs[self.pointer]
    
    def set_obj_img(self):
        """ self.obj_img をセットする
            self.obj_img は self.path_img を画像化したオブジェクトである
        """
        self.obj_img = Image.open(self.path_img).resize((300,320))
        self.image = ImageTk.PhotoImage(self.obj_img)

    def create_widgets(self):
        """ Applicationのウィジェットを作成する
        """
        # 左側フレーム ======================================================================
        self.frame_left = tkinter.LabelFrame(self.root, text="left frame")
        self.frame_left.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        # PATH表示フレーム
        self.frame_file_name = tkinter.Frame(self.frame_left)
        self.frame_file_name.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        self.label_file_name = tkinter.Label(self.frame_file_name, text="path = {}".format(self.path_img), bg="green")
        self.label_file_name.pack(fill=tkinter.BOTH)
        # IMG表示フレーム
        self.frame_img = tkinter.Frame(self.frame_left)
        self.label_img = tkinter.Label(self.frame_img, image=self.image, bg="blue")
        self.label_img.pack(fill=tkinter.BOTH)
        self.frame_img.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        # 仮フレーム
        self.frame_kari = tkinter.Frame(self.frame_left)
        self.frame_kari.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        self.label_kari = tkinter.Label(self.frame_kari, text="kari_label", bg="red")
        self.label_kari.pack(fill=tkinter.BOTH)
        # ===================================================================================
        
        # 右側フレーム =======================================================================
        self.frame_right = tkinter.Frame(self.root)
        self.frame_right.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
        # ラジオボタンフレーム
        self.frame_radio_button = tkinter.LabelFrame(self.frame_right, text="select face parts")
        self.frame_radio_button.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        # 髪の色
        self.f100 = tkinter.LabelFrame(self.frame_radio_button, text="髪の色", relief="sunken")
        self.v100 = tkinter.IntVar()
        self.v100.set(0)
        for i, hair_color in enumerate(hair_color_list):
            tkinter.Radiobutton(self.f100, text=hair_color, fg=JapaneseColor2EnglshColor(hair_color), activebackground="black",  value=i, variable=self.v100).pack(side=tkinter.LEFT, fill=tkinter.BOTH)   
        self.f100.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        # 髪型
        self.f101 = tkinter.LabelFrame(self.frame_radio_button, text="髪型", relief="sunken")
        self.v101 = tkinter.IntVar()
        self.v101.set(0)
        for i, hair_type in enumerate(hair_type_list):
            tkinter.Radiobutton(self.f101, text=hair_type, activebackground="black", value=i, variable=self.v101).pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.f101.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        # 目の色
        self.v102 = tkinter.IntVar()
        self.v102.set(0)
        self.f102 = tkinter.LabelFrame(self.frame_radio_button, text="目の色", relief="sunken")
        for i, eye_color in enumerate(eye_color_list):
            tkinter.Radiobutton(self.f102, text=eye_color, activebackground="black", fg=JapaneseColor2EnglshColor(eye_color), value=i , variable=self.v102).pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.f102.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        # 開口
        self.v103 = tkinter.IntVar()
        self.v103.set(0)
        self.f103 = tkinter.LabelFrame(self.frame_radio_button, text="開口", relief="sunken")
        for i, flag_opend_mouse in enumerate(opend_mouse):
            tkinter.Radiobutton(self.f103, text=flag_opend_mouse, value=i , activebackground="black",  variable=self.v103).pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.f103.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        # 帽子
        self.v104 = tkinter.IntVar()
        self.v104.set(0)
        self.f104 = tkinter.LabelFrame(self.frame_radio_button, text="帽子", relief="sunken")
        for i, flag_hat in enumerate(flags_hat):
            tkinter.Radiobutton(self.f104, text=flag_hat, value=i , activebackground="black", variable=self.v104).pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.f104.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        # メガネ
        self.v105 = tkinter.IntVar()
        self.v105.set(0)
        self.f105 = tkinter.LabelFrame(self.frame_radio_button, text="メガネ", relief="sunken")
        for i, flag_glasses in enumerate(flags_glasses):
            tkinter.Radiobutton(self.f105, text=flag_glasses, value=i, activebackground="black", variable=self.v105).pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.f105.pack(side=tkinter.TOP, fill=tkinter.BOTH)

        # 確認フレーム
        self.frame_confirmation = tkinter.LabelFrame(self.frame_right, text="confirmation")
        self.frame_confirmation.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)
        self.button1 = tkinter.Button(self.frame_confirmation, text="この内容で登録", command=self.clicked)
        self.button1.pack(fill=tkinter.BOTH)
        self.button2 = tkinter.Button(self.frame_confirmation, text="削除")
        self.button2.pack(fill=tkinter.BOTH)

        
        # ===================================================================================
    def clicked(self):
        # 値の更新
        print(self.path_img)
        print("選択された髪の色:",hair_color_list[self.v100.get()])
        print("選択された髪型:", hair_type_list[self.v101.get()])
        print("選択された目の色:", eye_color_list[self.v102.get()])
        print("選択された開口:", opend_mouse[self.v103.get()])
        print("選択された帽子:", flags_hat[self.v104.get()])
        print("選択されたメガネ:", flags_glasses[self.v105.get()])
        print("=="*20)
        self.label_file_name.configure(text="path = {}".format(self.path_img), bg="red")
        self.increment_pointer()
        self.set_path_img()
        self.set_obj_img()
        self.label_img.configure(image=self.image)
        
 

def check_png(name_file):
    """ src_dirの１ファイルに対して, 
        1. それがPNGか？
        2. そのファイルの解析結果(JSON)があるか？
        を調べる
        input: name_file, type(name_file) == str
        output: 
    """
    name, ext = os.path.splitext(name_file)
    if ext!=".png":return False
    return True
    

if __name__ == "__main__":
    # - * - * - * - * -  set argument - * - * - * - * -
    parser = argparse.ArgumentParser()
    parser.add_argument('--src_dir', type=str, default=None)
    parser.add_argument('--dst_dir', type=str, default=None)
    args = parser.parse_args()
    if args.src_dir==None and args.dst_dir==None:
        print("please specify --src_dir and --dst_dir")
        exit()
    
    # - * - * - get paths of images from src_dir - * - * -  
    path_src_dir = args.src_dir
    path_src_png_imgs = ["./{}/{}".format(path_src_dir,name_file) for name_file in os.listdir(path_src_dir) if check_png(name_file)]
    print(path_src_png_imgs)
    
    # - * - * - * - * - start application - * - * - * - * - 
    # app = Application()

    #root = tkinter.Tk()
    #app = Application(master = root)
    #app.mainloop()
    app = Application()
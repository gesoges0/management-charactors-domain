# -*- coding: utf8 -*-
import sys
from PIL import Image, ImageTk
import tkinter 

# class Frame(tk.Frame):
#     def __init__(self, master=None):
#         tk.Frame.__init__(self, master)
        
        
        # panedwindowを設定





        # 画像を開く
        #image = Image.open("./sample/47877_1.png")
        # 画像をインスタンス変数にセット
        #self.img = ImageTk.PhotoImage(image)


        # 画像をキャンバスにセット
        #il = tk.Label(self, image=self.img)
        #il.pack()


if __name__ == "__main__":
    
    root = tkinter.Tk()
    # 第一層フレームの宣言
    f0 = tkinter.Frame(root)
    f1 = tkinter.Frame(root)
    # 第二層フレームの宣言
    f00 = tkinter.Frame(f0)
    f01 = tkinter.Frame(f0)
    f02 = tkinter.Frame(f0, relief="flat", bg="red")
    f10 = tkinter.Frame(f1, relief="flat")
    f11 = tkinter.Frame(f1, relief="flat")

    # フレームの配置
    # 第一層フレーム
    f0.pack(side=tkinter.LEFT)
    f1.pack(side=tkinter.RIGHT)
    # 第二層フレーム
    f00.pack(side=tkinter.TOP)
    f01.pack(side=tkinter.TOP)
    f02.pack(side=tkinter.TOP)
    f10.pack(side=tkinter.TOP)
    f11.pack(side=tkinter.BOTTOM)

    # f00にラベルを配置する
    label_img_name = tkinter.Label(f00, bg="green", text="src = 2007/hoge.png")
    label_img_name.pack()
    
    # f01に画像を表示する
    obj_img = Image.open("./sample/91913_0.png")
    image = ImageTk.PhotoImage(obj_img)
    label_img_fig = tkinter.Label(f01, image=image)
    label_img_fig.pack()

    # f02に仮背景を設定
    label_kari_name = tkinter.Label(f02, bg="green", text="仮")
    label_kari_name.pack()

    # - - - - - - f10の設定 - - - - - - 
    # 髪の色
    f100 = tkinter.LabelFrame(f10, text="髪の色", relief="sunken")
    v100 = tkinter.IntVar()
    v100.set(0)
    hair_color_list = ["金", "茶", "赤", "橙", "桃", "黒", "青", "紫", "緑", "白", "銀"]
    for hair_color in hair_color_list:
        tkinter.Radiobutton(f100, text=hair_color, value="hari_"+hair_color, variable=v100).pack(side=tkinter.LEFT)   
    f100.pack(side=tkinter.TOP)
    # 髪型
    f101 = tkinter.LabelFrame(f10, text="髪型", relief="sunken")
    v101 = tkinter.IntVar()
    v101.set(0)
    hair_type_list = ["ロング", "ショート", "ツインテ", "ドリル", "ポニテ"]
    for hair_type in hair_type_list:
        tkinter.Radiobutton(f101, text=hair_type, value="hair_"+hair_type, variable=v101).pack(side=tkinter.LEFT)
    f101.pack(side=tkinter.TOP)
    # 目の色
    eye_color_list = ["青", "紫", "赤", "茶", "緑", "黄", "桃", "黒"]
    v102 = tkinter.IntVar()
    v102.set(0)
    f102 = tkinter.LabelFrame(f10, text="目の色", relief="sunken")
    for eye_color in eye_color_list:
        tkinter.Radiobutton(f102, text=eye_color, value="eye_"+eye_color, variable=v102).pack(side=tkinter.LEFT)
    f102.pack(side=tkinter.TOP)

    # - - - - - - f11の設定 - - - - - -
    button110 = tkinter.Button(f11, text="この内容で登録")
    button110.pack(side=tkinter.LEFT)
    button111 = tkinter.Button(f11, text="削除する")
    button111.pack(side=tkinter.LEFT)
    





    

    # tkinter.Frame(f0).pack(fill = tkinter.BOTH)
    # tkinter.Frame(f0).pack(fill = tkinter.BOTH)
    # tkinter.Frame(f0).pack(fill = tkinter.BOTH)
    
    # f1 にボタンを配置する
   # tkinter.Button(f1, text = 'button 10').pack(fill = tkinter.BOTH)
    #tkinter.Button(f1, text = 'button 11').pack(fill = tkinter.BOTH)
    #tkinter.Button(f1, text = 'button 12').pack(fill = tkinter.BOTH)
    
    #tkinter.Button(f3, text = 'button 00').pack(side = tkinter.LEFT)

    root.mainloop()
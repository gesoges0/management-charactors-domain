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
    f10 = tkinter.Frame(f1, relief="flat", width=60, height=60, bg="blue")
    f11 = tkinter.Frame(f1, relief="flat", width=60, height=60, bg="green")

    # フレームの配置
    # 第一層フレーム
    f0.pack(side=tkinter.LEFT)
    f1.pack(side=tkinter.RIGHT)
    # 第二層フレーム
    f00.pack(fill=tkinter.BOTH)
    f01.pack(fill=tkinter.BOTH)
    f02.pack(fill=tkinter.BOTH)
    f10.pack(fill=tkinter.BOTH)
    f11.pack(fill=tkinter.BOTH)

    # f00にラベルを配置する
    label_img_name = tkinter.Label(f00, bg="green", text="src = 2007/hoge.png")
    label_img_name.pack()
    
    # f01に画像を表示する
    obj_img = Image.open("./sample/47877_1.png")
    image = ImageTk.PhotoImage(obj_img)
    label_img_fig = tkinter.Label(f01, image=image)
    label_img_fig.pack()

    # f02に仮背景を設定
    label_kari_name = tkinter.Label(f02, bg="green", text="仮")
    
    



    

    # tkinter.Frame(f0).pack(fill = tkinter.BOTH)
    # tkinter.Frame(f0).pack(fill = tkinter.BOTH)
    # tkinter.Frame(f0).pack(fill = tkinter.BOTH)
    
    # f1 にボタンを配置する
   # tkinter.Button(f1, text = 'button 10').pack(fill = tkinter.BOTH)
    #tkinter.Button(f1, text = 'button 11').pack(fill = tkinter.BOTH)
    #tkinter.Button(f1, text = 'button 12').pack(fill = tkinter.BOTH)
    
    #tkinter.Button(f3, text = 'button 00').pack(side = tkinter.LEFT)

    root.mainloop()
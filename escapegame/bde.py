import tkinter as tk
from PIL import ImageTk, Image, ImageDraw

class Room:
    def __init__(self, master):
        self.master = master

        self.canvas = tk.Canvas(master,width=800,height=550)
        self.canvas.pack(side="bottom")
        # Toujours ajouter une référence au background pour éviter qu'elle soit détruite
        self.canvas.canva = self.canvas
        
        self.bgimg = ImageTk.PhotoImage(Image.open("bg_bde.jpg"))
        self.bgimg.img = self.bgimg
        self.canvas.create_image(0,30,image=self.bgimg,anchor="nw")

        self.btn_test = tk.Button(self.master, text="Test", command=self.test)
        self.buttontest_window = self.canvas.create_window(400,300,anchor="nw", window=self.btn_test)

    def test(self):
        print("success!")
    #def update_stream(self):
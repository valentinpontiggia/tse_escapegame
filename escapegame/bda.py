import tkinter as tk
from PIL import Image, ImageTk

class BDARiddle:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

        self.canvas = tk.Canvas(self.mainWindow, width=800, height=550)
        self.canvas.pack(side="bottom")
        # Toujours ajouter une référence au background pour éviter qu'elle soit détruite
        self.canvas.canva = self.canvas

        self.new_img = ImageTk.PhotoImage(Image.open("bda.jpg"))
        self.new_img.img = self.new_img
        self.canvas.create_image(0,20,image=self.new_img,anchor="nw")
        self.canvas.pack(fill="both", expand=True)

        

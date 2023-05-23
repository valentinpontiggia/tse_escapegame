import tkinter as tk
from PIL import Image, ImageTk

class InspireRiddle:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

        self.canvas = tk.Canvas(self.mainWindow, width=800, height=550)
        self.canvas.pack(side="bottom")
        # Toujours ajouter une référence au background pour éviter qu'elle soit détruite
        self.canvas.canva = self.canvas

        self.new_img = ImageTk.PhotoImage(Image.open("inspire.jpg"))
        self.new_img.img = self.new_img
        self.canvas.create_image(0,20,image=self.new_img,anchor="nw")
        self.canvas.pack(fill="both", expand=True)

        self.enter()

    def enter(self):
        keyboard.on_press_key("enter", lambda _:self.morse())

    def morse(self):
        self.morseWindow = tk.Toplevel(self.mainWindow)
        self.morseWindow.title("Code Morse")
        self.morseWindow.geometry("450x600")

        self.morsecanvas = tk.Canvas(self.morseWindow, width=450, height=600)
        self.morsecanvas.pack(side="bottom")
        # Toujours ajouter une référence au background pour éviter qu'elle soit détruite
        self.morsecanvas.canva = self.morsecanvas

        self.morse_img = ImageTk.PhotoImage(Image.open("morse.png"))
        self.morse_img.img = self.morse_img
        self.morsecanvas.create_image(0,20,image=self.morse_img,anchor="nw")
        self.morsecanvas.pack(fill="both", expand=True)
        

import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
#from tkmacosx import Button

class FATSE:
    def __init__(self, mainwindow):
        self.master = mainwindow

        self.canvas = tk.Canvas(mainwindow, width=800,height=550)
        self.canvas.pack(side="bottom")
        # Toujours ajouter une référence au background pour éviter qu'elle soit détruite
        self.canvas.canva = self.canvas

        self.bgimg = ImageTk.PhotoImage(Image.open("bg_images/bds.jpeg"))
        self.bgimg.img = self.bgimg
        self.canvas.create_image(0,-25,image=self.bgimg,anchor="nw")

        self.nerdle = tk.PhotoImage(file="bg_images/nerdle.png").subsample(8)
        self.play_button = tk.Button(self.master, image=self.nerdle, cursor="hand2", command = self.jouer)
        self.button4_window = self.canvas.create_window(295,240, anchor="nw", window=self.play_button)

    def jouer(self):
        print("en train de jouer...")
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.master,width=800,height=550)
        self.canvas.pack(side="bottom")
        # Toujours ajouter une référence au background pour éviter qu'elle soit détruite
        self.canvas.canva = self.canvas
        
        self.bgimg = ImageTk.PhotoImage(Image.open("bg_images/nerdle_ordi.jpg").resize((750,550), Image.ANTIALIAS))
        self.bgimg.img = self.bgimg
        self.canvas.create_image(25,0,image=self.bgimg,anchor="nw")
        
        self.gameRules = self.canvas.create_text(150,275, text="Nerdle : Placez les chiffres et les opérations \naux bons endroit pour que le calcul soit juste. \n\nEn rose le symbole est bon mais mal placé. \nEn vert le symbole est bon et bien placé.",anchor="nw",fill="black")
        
        self.first_symbol = tk.Entry(self.canvas, bg="#151803", fg="white", justify=tk.CENTER)
        self.first_symbol.place(x=142, y=175, width=50, height=50)
        self.second_symbol = tk.Entry(self.canvas, bg="#151803", fg="white", justify=tk.CENTER)
        self.second_symbol.place(x=207, y=175, width=50, height=50)
        self.third_symbol = tk.Entry(self.canvas, bg="#151803", fg="white", justify=tk.CENTER)
        self.third_symbol.place(x=272, y=175, width=50, height=50)
        self.fourth_symbol = tk.Entry(self.canvas, bg="#151803", fg="white", justify=tk.CENTER)
        self.fourth_symbol.place(x=337, y=175, width=50, height=50)
        self.fifth_symbol = tk.Entry(self.canvas, bg="#151803", fg="white", justify=tk.CENTER)
        self.fifth_symbol.place(x=402, y=175, width=50, height=50)
        self.sixth_symbol = tk.Entry(self.canvas, bg="#151803", fg="white", justify=tk.CENTER)
        self.sixth_symbol.place(x=467, y=175, width=50, height=50)
        self.seventh_symbol = tk.Entry(self.canvas, bg="#151803", fg="white", justify=tk.CENTER)
        self.seventh_symbol.place(x=532, y=175, width=50, height=50)
        self.eighth_symbol = tk.Entry(self.canvas, bg="#151803", fg="white", justify=tk.CENTER)
        self.eighth_symbol.place(x=597, y=175, width=50, height=50)
        
        self.btn_check = tk.Button(self.master, text="Vérifier", bg="#48FEFF", fg="black", command=self.check)
        self.buttoncheck_window = self.canvas.create_window(575,300,anchor="nw", window=self.btn_check)

    def check(self):
        self.nerdle = self.first_symbol.get() + self.second_symbol.get() + self.third_symbol.get() + self.fourth_symbol.get() + self.fifth_symbol.get() + self.sixth_symbol.get() + self.seventh_symbol.get() + self.eighth_symbol.get()
        #self.nerdle == "9*42=378"
        if self.nerdle == "9*42=378":
            self.canvas.destroy()

            self.canvas = tk.Canvas(self.master,width=800,height=550)
            self.canvas.pack(side="bottom")
            # Toujours ajouter une référence au background pour éviter qu'elle soit détruite
            self.canvas.canva = self.canvas

            self.bgimg = ImageTk.PhotoImage(Image.open("bg_images/nerdle_success.jpg").resize((750,550), Image.ANTIALIAS))
            self.bgimg.img = self.bgimg
            self.canvas.create_image(25,0,image=self.bgimg,anchor="nw")

            self.bravo = self.canvas.create_text(150,275, text="Bravo vous avez trouvé la réponse ! \n\nÀ quoi peut bien servir ce code ...?", font=("Arial", 16, "bold"), anchor="nw", fill="black")

            print("Bravo !!")
        else:
            self.canvas.create_text(550,250,text="Raté, essaye encore !")

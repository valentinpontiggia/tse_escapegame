import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
from tkinter import font
import pyglet, os
#from tkmacosx import Button

class FATSE:
    def __init__(self, mainwindow):
        self.master = mainwindow

        self.canvas = tk.Canvas(mainwindow, width=800,height=550)
        self.canvas.pack(side="bottom")
        # Toujours ajouter une référence au background pour éviter qu'elle soit détruite
        self.canvas.canva = self.canvas

        self.bgimg = ImageTk.PhotoImage(Image.open("bg_images/fatse.jpg").resize((800,550), Image.ANTIALIAS))
        self.bgimg.img = self.bgimg
        self.canvas.create_image(0,-25,image=self.bgimg,anchor="nw")

        self.nerdle = tk.PhotoImage(file="bg_images/safe_code.png").subsample(40)
        self.play_button = tk.Button(self.master, image=self.nerdle, cursor="hand2", command = self.jouer)
        self.button4_window = self.canvas.create_window(415,435, anchor="nw", window=self.play_button)

    def jouer(self):
        print("en train de jouer...")
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.master,width=800,height=550)
        self.canvas.pack(side="bottom")
        # Toujours ajouter une référence au background pour éviter qu'elle soit détruite
        self.canvas.canva = self.canvas
        
        self.bgimg = ImageTk.PhotoImage(Image.open("bg_images/code.png").resize((800,550), Image.ANTIALIAS))
        self.bgimg.img = self.bgimg
        self.canvas.create_image(0,0,image=self.bgimg,anchor="nw")
        
        pyglet.font.add_file('bg_images/DS-DIGIB.TTF')
        #custom_font = font.Font(family="DS-DIGIB", file="bg_images/DS-DIGIB.TTF")

        self.first_number_text = 0
        self.first_number = tk.Label(self.master, text = self.first_number_text, bg="#FFF390", fg="#653403", font=("DS-DIGIB", 30))
        self.first_number.place(x=326, y=310, width=40, height=40)

        self.second_number_text = 0
        self.second_number = tk.Label(self.master, text = self.second_number_text, bg="#FFF390", fg="#653403", font=("DS-DIGIB", 30))
        self.second_number.place(x=392, y=310, width=40, height=40)

        self.third_number_text = 0
        self.third_number = tk.Label(self.master, text = self.third_number_text, bg="#FFF390", fg="#653403", font=("DS-DIGIB", 30))
        self.third_number.place(x=458, y=310, width=40, height=40, anchor="nw")

        self.up_arrow = tk.PhotoImage(file="bg_images/up_arrow.png").subsample(10)
        self.down_arrow = tk.PhotoImage(file="bg_images/down_arrow.png").subsample(10)

        self.first_up_button = tk.Button(self.master, image=self.up_arrow, command=lambda: self.plus_one(1))
        self.first_up_button_window = self.canvas.create_window(320,192,anchor="nw", window=self.first_up_button)
        self.second_up_button = tk.Button(self.master, image=self.up_arrow, command=lambda: self.plus_one(2))
        self.second_up_button_window = self.canvas.create_window(386,192,anchor="nw", window=self.second_up_button)
        self.third_up_button = tk.Button(self.master, image=self.up_arrow, command=lambda: self.plus_one(3))
        self.third_up_button_window = self.canvas.create_window(452,192,anchor="nw", window=self.third_up_button)

        self.first_down_button = tk.Button(self.master, image=self.down_arrow, command=lambda: self.minus_one(1))
        self.first_down_button_window = self.canvas.create_window(320,327,anchor="nw", window=self.first_down_button)
        self.second_down_button = tk.Button(self.master, image=self.down_arrow, command=lambda: self.minus_one(2))
        self.second_down_button_window = self.canvas.create_window(386,327,anchor="nw", window=self.second_down_button)
        self.third_down_button = tk.Button(self.master, image=self.down_arrow, command=lambda: self.minus_one(3))
        self.third_down_button_window = self.canvas.create_window(452,327,anchor="nw", window=self.third_down_button)
        #self.btn_check = tk.Button(self.master, text="Vérifier", bg="#48FEFF", fg="black", command=self.check)
        #self.buttoncheck_window = self.canvas.create_window(575,300,anchor="nw", window=self.btn_check)

    def plus_one(self, case_number):
        if case_number == 1:
            self.first_number_text = self.first_number_text + 1
            self.first_number.config(text=self.first_number_text)
        elif case_number == 2:
            self.second_number_text = self.second_number_text + 1
            self.second_number.config(text=self.second_number_text)
        else:
            self.third_number_text = self.third_number_text + 1
            self.third_number.config(text=self.third_number_text)

    def minus_one(self, case_number):
        if case_number == 1:
            if self.first_number_text == 0:
                self.first_number_text = 0
            else:
                self.first_number_text = self.first_number_text - 1
                self.first_number.config(text=self.first_number_text)
        elif case_number == 2:
            if self.second_number_text == 0:
                self.second_number_text = 0
            else:
                self.second_number_text = self.second_number_text - 1
                self.second_number.config(text=self.second_number_text)
        else:
            if self.third_number_text == 0:
                self.third_number_text = 0
            else:
                self.third_number_text = self.third_number_text - 1
                self.third_number.config(text=self.third_number_text)
        
"""
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
"""
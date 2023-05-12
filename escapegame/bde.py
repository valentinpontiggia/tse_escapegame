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

        self.btn_test = tk.Button(self.master, text="Jouer",bg="black", fg='white', command=self.jouer)
        self.buttontest_window = self.canvas.create_window(617,145,anchor="nw", window=self.btn_test)

        self.printText()
        
    def jouer(self):
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.master,width=800,height=550)
        self.canvas.pack(side="bottom")
        # Toujours ajouter une référence au background pour éviter qu'elle soit détruite
        self.canvas.canva = self.canvas
        
        self.bgimg = ImageTk.PhotoImage(Image.open("Mastermind.jpg"))
        self.bgimg.img = self.bgimg
        self.canvas.create_image(50,30,image=self.bgimg,anchor="nw")
        
        self.gameRules = self.canvas.create_text(500,25, text='Jeu du Mastermind : placez les couleurs\naux bons endroits pour trouver le code \nsecret. Les points noirs correspondent \nà une bonne couleur bien placée, les\npoints blancs correspondent à une bon-\nne couleur mal placée.',anchor="nw",fill="black")
        
        self.btn_color1 = tk.Button(self.master, text="     ", bg="red", command=self.changeColor1)
        self.buttoncolor1_window = self.canvas.create_window(500,200,anchor="nw", window=self.btn_color1)
        self.btn_color2 = tk.Button(self.master, text="     ", bg="red", command=self.changeColor2)
        self.buttoncolor2_window = self.canvas.create_window(530,200,anchor="nw", window=self.btn_color2)
        self.btn_color3 = tk.Button(self.master, text="     ", bg="red", command=self.changeColor3)
        self.buttoncolor3_window = self.canvas.create_window(560,200,anchor="nw", window=self.btn_color3)
        self.btn_color4 = tk.Button(self.master, text="     ", bg="red", command=self.changeColor4)
        self.buttoncolor4_window = self.canvas.create_window(590,200,anchor="nw", window=self.btn_color4)

        self.btn_check = tk.Button(self.master, text="Check", command=self.check)
        self.buttoncheck_window = self.canvas.create_window(650,200,anchor="nw", window=self.btn_check)

    def changeColor1(self):
        if self.btn_color1.cget('bg')=="red":
            self.btn_color1.config(bg='green')
        elif self.btn_color1.cget('bg')=="green":
            self.btn_color1.config(bg='blue')
        elif self.btn_color1.cget('bg')=="blue":
            self.btn_color1.config(bg='yellow')
        elif self.btn_color1.cget('bg')=="yellow":
            self.btn_color1.config(bg='orange')
        elif self.btn_color1.cget('bg')=="orange":
            self.btn_color1.config(bg='purple')
        elif self.btn_color1.cget('bg')=="purple":
            self.btn_color1.config(bg='red')
            
    def changeColor2(self):
        if self.btn_color2.cget('bg')=="red":
            self.btn_color2.config(bg='green')
        elif self.btn_color2.cget('bg')=="green":
            self.btn_color2.config(bg='blue')
        elif self.btn_color2.cget('bg')=="blue":
            self.btn_color2.config(bg='yellow')
        elif self.btn_color2.cget('bg')=="yellow":
            self.btn_color2.config(bg='orange')
        elif self.btn_color2.cget('bg')=="orange":
            self.btn_color2.config(bg='purple')
        elif self.btn_color2.cget('bg')=="purple":
            self.btn_color2.config(bg='red')
            
    def changeColor3(self):
        if self.btn_color3.cget('bg')=="red":
            self.btn_color3.config(bg='green')
        elif self.btn_color3.cget('bg')=="green":
            self.btn_color3.config(bg='blue')
        elif self.btn_color3.cget('bg')=="blue":
            self.btn_color3.config(bg='yellow')
        elif self.btn_color3.cget('bg')=="yellow":
            self.btn_color3.config(bg='orange')
        elif self.btn_color3.cget('bg')=="orange":
            self.btn_color3.config(bg='purple')
        elif self.btn_color3.cget('bg')=="purple":
            self.btn_color3.config(bg='red')
            
    def changeColor4(self):
        if self.btn_color4.cget('bg')=="red":
            self.btn_color4.config(bg='green')
        elif self.btn_color4.cget('bg')=="green":
            self.btn_color4.config(bg='blue')
        elif self.btn_color4.cget('bg')=="blue":
            self.btn_color4.config(bg='yellow')
        elif self.btn_color4.cget('bg')=="yellow":
            self.btn_color4.config(bg='orange')
        elif self.btn_color4.cget('bg')=="orange":
            self.btn_color4.config(bg='purple')
        elif self.btn_color4.cget('bg')=="purple":
            self.btn_color4.config(bg='red')
            
    def check(self):
        if self.btn_color1.cget('bg')=="orange" and self.btn_color2.cget('bg')=="purple" and self.btn_color3.cget('bg')=="blue" and self.btn_color4.cget('bg')=="purple":
            self.canvas.destroy()
            print("ajouter photo de gaelle")
        else:
            self.canvas.create_text(550,250,text="Raté, essaye encore !")
        
    def printText(self):
        self.canvas_rulestext = self.canvas.create_text(50,50, text='',anchor="nw",fill="black")
        self.rulestext = "Un ordinateur abandonné se trouve \ndans le BDE, sur lequel est affiché\nun jeu étrange."
        self.delta = 30
        self.delay = 0
        for x in range(len(self.rulestext)+1):
            self.s = self.rulestext[:x]
            self.newtext = lambda s=self.s:self.canvas.itemconfigure(self.canvas_rulestext, text=s)
            self.canvas.after(self.delay,self.newtext)
            self.delay +=self.delta
    #def update_stream(self):
import tkinter as tk
from PIL import Image, ImageTk

class FATSEClue:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.canvas = tk.Canvas(self.mainWindow, width=800, height=550)
        self.canvas.pack(side="bottom")
        # Toujours ajouter une référence au background pour éviter qu'elle soit détruite
        self.canvas.canva = self.canvas

        #self.new_img = ImageTk.PhotoImage(Image.open("bda.jpg"))
        #self.new_img.img = self.new_img
        #self.canvas.create_image(0,20,image=self.new_img,anchor="nw")
        #self.canvas.pack(fill="both", expand=True)

        self.clue1_button = tk.Button(mainWindow, **self.button_style, text="Indice 1", command=self.clue1)
        self.clue1_button_window = self.canvas.create_window(80,50,anchor="nw", window=self.clue1_button)

        self.clue2_button = tk.Button(mainWindow, **self.button_style, text="Indice 2", command=self.clue2)
        self.clue2_button_window = self.canvas.create_window(80,300,anchor="nw", window=self.clue2_button)

    def clue1(self):
        self.clue1_button.destroy()
        self.canvas.create_text(400, 100, **self.text_style, text = "Un calcul compliqué permet d'obtenir un code à trois chiffres")

    def clue2(self):
        self.clue2_button.destroy()
        self.canvas.create_text(400, 350, **self.text_style, text = "Allez voir au BDS")



    button_style = {
        "fg": "#902038",     # Couleur du texte blanc
        "font": ("Verdana", 14, "bold"),   # Police en gras, taille 14
        "bd": 3,           # Largeur de la bordure de 3 pixels
        "relief": "ridge", # Type de bordure en relief
        "activebackground": "#2B91FF",    # Couleur de fond lors du survol de la souris
        "activeforeground": "white",      # Couleur du texte lors du survol de la souris
        "highlightcolor": "#F4FA58",      # Couleur de la bordure lors du survol de la souris
        "highlightbackground" : "darkgrey",
        "highlightthickness": 2,          # Epaisseur de la bordure lors du survol de la souris
        "cursor": "hand2",    # Curseur de souris en forme de main pour indiquer l'interactivité
        "height": 5,
        "width": 48,
    }

    text_style = {
        "font": ("Verdana", 14, "bold"),   # Police en gras, taille 14
    }

        

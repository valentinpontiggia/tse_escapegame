import tkinter as tk
#from ..controllers.controller import Controller

class Vue(tk.Tk):
    def __init__(self,controller):
        
        super().__init__()

        self.title("Escape Game")
        self.geometry("800x600")

        self.controller = controller
        
        self.question_label = tk.Label(self.master, text="Quel est l'objet sur cette image ?")
        self.question_label.pack()

        self.image_label = tk.Label(self.master, image=None)
        self.image_label.pack()

        self.reponse_label = tk.Label(self.master, text="")
        self.reponse_label.pack()

        self.bouton_capturer = tk.Button(self.master, text="Capturer", command=self.capturer_image)
        self.bouton_capturer.pack()

    def capturer_image(self):
        # Code pour capturer l'image depuis la webcam et la stocker dans une variable nommée image
        image = None
        self.afficher_image(image)

    def afficher_image(self, image):
        photo = tk.PhotoImage(file=image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def afficher_reponse(self, est_correcte):
        if est_correcte:
            self.reponse_label.configure(text="Bonne réponse!")
        else:
            self.reponse_label.configure(text="Mauvaise réponse :(")

import tkinter as tk

class Controller:
    def __init__(self):
        self.game = Game()
        self.vue = Vue(self)
        self.vue.bouton_capturer.config(state=tk.DISABLED)
        self.vue.question_label.configure(text="Escape Game")
        self.game.ajouter_enigme(Enigme("Chat", "cat"))
        self.vue.bouton_capturer.config(state=tk.NORMAL)

    def demarrer(self):
        self.vue.mainloop()

    def capturer_image(self):
        reponse = self.classifier_image()
        est_correcte = self.game.verifier_reponse(reponse)
        self.vue.afficher_reponse(est_correcte)

    def classifier_image(self):
        # Code pour classifier l'image capturée à l'aide d'un modèle de classification (par exemple, TensorFlow)
        return "chat"

class Enigme:
    def __init__(self, question, reponse):
        self.question = question
        self.reponse = reponse

class Game:
    def __init__(self):
        self.enigmes = []
        self.score = 0
        self.bonnes_reponses = []
        self.mauvaises_reponses = []

    def ajouter_enigme(self, enigme):
        self.enigmes.append(enigme)

    def verifier_reponse(self, reponse):
        for enigme in self.enigmes:
            if reponse == enigme.reponse:
                self.score += 1
                self.bonnes_reponses.append(reponse)
                return True
        self.mauvaises_reponses.append(reponse)
        return False

class Vue(tk.Tk):
    def __init__(self,controller):
        
        super().__init__()

        self.title("Escape Game")
        self.geometry("800x600")
        self.resizable(height=False,width=False)

        self.controller = controller
        
        self.question_label = tk.Label(self, text="Quel est l'objet sur cette image ?",font=("Verdana",20,"bold"),foreground="darkblue",bg="grey")
        self.question_label.pack()
        self.question_label.place(x='360',y='20')

        variable=""
        self.entree = tk.Entry(self,textvariable=variable)
        self.entree.pack()

        self.image_label = tk.Label(self, image=None)
        self.image_label.pack()

        self.reponse_label = tk.Label(self, text="")
        self.reponse_label.pack()

        self.bouton_capturer = tk.Button(self, text="Capturer", command=self.capturer_image, bg="darkblue", fg="white")
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

if __name__ == '__main__':
    game = Controller()
    game.demarrer()
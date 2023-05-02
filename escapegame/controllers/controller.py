from ..models.model import Game, Enigme
from ..views.view import Vue, tk

class Controller:
    def __init__(self):
        self.game = Game()
        self.vue = Vue()
        self.vue.bouton_capturer.config(state=tk.DISABLED)
        self.vue.question_label.configure(text="Quel est le nom de cet animal ?")
        self.game.ajouter_enigme(Enigme("Chat", "chat"))

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

if __name__ == '__main__':
    game = Controller()
    game.demarrer()
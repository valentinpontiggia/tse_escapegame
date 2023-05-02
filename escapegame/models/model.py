#from ..controllers.controller import Controller

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

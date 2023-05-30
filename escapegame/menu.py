import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
import pygame
import camera
import bde
import inspire
import bda
import bds
import fatse
import indiceBDA
import indiceFATSE
import indiceBDE
import indiceBDS

# Crée une nouvelle fenêtre décrivant le scénario
text2 = ("     Il semblerait que l'argent\n récolté lors du"
        +" Gala de l'école\n a été volé et les soupçons se\n portent sur l'une des assos de\n    l'école...")
text3 = ("            Je sais que tu as l'esprit vif,\n      c'est pourquoi je fais appel à toi.\n     J'ai besoin de quelqu'un en qui je\n      peux avoir"
        +" confiance pour m'aider\n          à mener l'enquête...")
text4 = ("     Je sais que c'est une tâche\n  difficile, mais je suis persuadé que\n    tu es capable de relever ce défi !")
text_index = 0
scenario_canvas = None
text_id = None
scenario_img = None
apropos_img = None
next_button = None
pause = False
timer_paused = False

def update_text():
        global next_button
        global text_index
        global text_id
        global scenario_canvas
        text_index += 1
        if text_index==1:
            scenario_canvas.itemconfigure(text_id, text=text2)
        if text_index==2:
            scenario_canvas.itemconfigure(text_id, text=text3)
        if text_index==3:
            scenario_canvas.itemconfigure(text_id, text=text4)
            next_button.destroy()
            text_index = 0
        if text_index==4:
            scenario_canvas.itemconfigure(text_id, text=text3)

def scenarioWindow():
    global next_button
    global scenario_canvas
    global text_id
    global scenario_img
    scenarioWin = tk.Toplevel(mainwindow)
    scenarioWin.title("Scénario")
    scenarioWin.geometry("600x600")
    scenario_canvas = tk.Canvas(scenarioWin, width=600, height=600)
    scenario_canvas.pack(fill="both",expand=True)
    scenario_img = ImageTk.PhotoImage(Image.open("bg_images/student.png"))
    scenario_canvas.create_image(0,0,image=scenario_img,anchor="nw")
    global text_id
    text_id = scenario_canvas.create_text(480,80,text=("     Salut ! Je suis confronté à\nune situation délicate et je me\n permets de solliciter ton"
        +" aide\n pour m'aider à résoudre cette\n     affaire !"))
    next_button = tk.Button(scenarioWin, text='>', command=update_text)
    next_button_window = scenario_canvas.create_window(530,108,anchor="nw", window=next_button)

def aProposWindow():
    global apropos_img
    aProposWin = tk.Toplevel(mainwindow)
    aProposWin.title("A propos")
    aProposWin.geometry("463x260")
    apropos_canvas = tk.Canvas(aProposWin, width=463, height=260)
    apropos_canvas.pack(fill="both",expand=True)
    apropos_img = ImageTk.PhotoImage(Image.open("bg_images/apropos.jpg"))
    apropos_canvas.create_image(0,0,image=apropos_img,anchor="nw")
    textapropos = tk.Label(aProposWin,text="Cette application a été créée dans le but du projet de classification d'images de FISE2 de Télécom Saint-Etienne.\n Contributeurs :\n - Lilou Tisserand\n - Gaëlle Quillaud\n - Chloé Davoine\n - Elie Cormier\n - Valentin Pontiggia \n\nMerci à Anne-Claire Legrand pour ses précieux conseils tout au long du projet",justify="left",wraplength=400, bg="#D4EAF8")
    textapropos.place(x=50,y=50)

new_img = None

# Change de canva au click du bouton start, active le chrono, et propose 4 assos pour commencer à enquêter

def startGame():
    global start_button, start_canvas
    # Remove the Start button and the Rules frame
    start_button.destroy()
    start_canvas.destroy()

    new_canvas = tk.Canvas(mainwindow,width=800,height=550)
    new_canvas.pack(side="bottom")
    # Toujours ajouter une référence au background pour éviter qu'elle soit détruite
    new_canvas.canva = new_canvas

    top_canvas = tk.Canvas(mainwindow,width=800,height=30,name="timer")
    top_canvas.pack(side="top")
    # Toujours ajouter une référence au background pour éviter qu'elle soit détruite
    top_canvas.canva = top_canvas


    new_img = ImageTk.PhotoImage(Image.open("bg_images/couloir.jpg"))
    new_img.img = new_img
    new_canvas.create_image(0,0,image=new_img,anchor="nw")
    
    timer_text = top_canvas.create_text(700,0, text='60:00',anchor="nw",fill="darkblue",font=("Helvetica",20, "bold"),tags=("timer"))
    
    play_music("musics/musicCouloir.mp3")
    

    def update_timer():
        global countdown_time, timer_paused
        if not timer_paused:
            minutes, seconds = divmod(countdown_time, 60)
            # Formate l'heure en MM:SS
            timer_hour = f"{minutes:02d}:{seconds:02d}"
            top_canvas.itemconfig(timer_text, text=timer_hour)
            if countdown_time > 0:
                # Rappelle la fonction au bout d'une seconde.
                countdown_time -= 1
                top_canvas.after(1000, update_timer)
            if countdown_time == 0:
                for widgets in mainwindow.winfo_children():
                    widgets.destroy()
                    loose_canvas = tk.Canvas(mainwindow,width=800,height=600)
                    loose_canvas.pack(fill="both", expand=True)
                    loose_canvas.canva = loose_canvas
                    loose_img = ImageTk.PhotoImage(Image.open("bg_images/thief.png"))
                    loose_img.img = loose_img
                    loose_canvas.create_image(80,0,image=loose_img,anchor="nw")
                    loose_canvas.create_text(400,360,text="Le voleur a réussi à s'enfuir... Il va pouvoir se la couler\ndouce pendant que les assos de TSE devront se\ndémener pour renflouer les caisses récemment vidées...",font=("Verdana",12, "bold"),fill="gold")
                    
    
    update_timer()
    new_canvas.create_text(412,455,text="Vous voici dans le couloir des\nassociations. Commencez à\nenquêter en choisissant dans \nquelle association vous sou-\nhaitez récolter des indices",fill="#902038",font=("Verdana",9))
    
    button1 = tk.Button(mainwindow, text="BDE", command = swapToBg1)
    button_style_doors(button1,10)
    button1_window = new_canvas.create_window(150,216,anchor="nw", window=button1)
    
    button2 = tk.Button(mainwindow, text="BDS", command = swapToBg2)
    button_style_doors(button2,6)
    button2_window = new_canvas.create_window(291,213,anchor="nw", window=button2)
    
    button3 = tk.Button(mainwindow, text="BDA", command = swapToBg3)
    button_style_doors(button3,5)
    button3_window = new_canvas.create_window(385,220,anchor="nw", window=button3)
    
    button4 = tk.Button(mainwindow, text="INSPIRE", command = swapToBg4)
    button_style_doors(button4,11)
    button4_window = new_canvas.create_window(687,215,anchor="nw", window=button4)

    button5 = tk.Button(mainwindow, text="FATSE", command = swapToBg5)
    button_style_doors(button5,6)
    button5_window = new_canvas.create_window(518,215,anchor="nw", window=button5)

    buttonEnd = tk.Button(mainwindow, text="Accuser", **button_style, command = startCamera)
    buttonEnd_window = new_canvas.create_window(350,350,anchor="nw", window=buttonEnd)
    
    def pause():
        global timer_paused
        if not timer_paused :
            timer_paused = True
        else : 
            timer_paused = False
            update_timer()
            
    buttonPause = tk.Button(mainwindow, text="⏯", fg= "#902038",   font = ("Verdana", 12),  bd= 3, relief= "ridge", command=pause)
    buttonPauseWindow = top_canvas.create_window(630,0,anchor="nw", window=buttonPause)

def play_music(musicFile):
    pygame.mixer.init()
    pygame.mixer.music.load("musics/porteSound.wav") # Ajoutez votre propre fichier de musique ici
    pygame.mixer.music.play()
    pygame.mixer.music.queue(musicFile)

def startCamera():
    camWindow = tk.Toplevel(mainwindow)
    camWindow.title("Caméra")
    camWindow.geometry("450x600")
    cam = camera.CameraApp(camWindow,mainwindow)
    
def swapToBg1():
    for widgets in mainwindow.winfo_children():
        if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
                play_music("musics/musicBDE.mp3")
                room = bde.Room(mainwindow)
                
def swapToBg2():
    for widgets in mainwindow.winfo_children():
      if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
                play_music("musics/musicBDS.mp3")
                room = bds.BDS(mainwindow)
def swapToBg3():
    for widgets in mainwindow.winfo_children():
      if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
                play_music("musics/musicBDA.mp3")
                room = bda.BDARiddle(mainwindow)
    
def swapToBg4():
    for widgets in mainwindow.winfo_children():
      if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
                play_music("musics/musicInspire.mp3")
                room = inspire.InspireRiddle(mainwindow)

def swapToBg5():
    for widgets in mainwindow.winfo_children():
      if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
                play_music("musics/musicFATSE.mp3")
                room = fatse.FATSE(mainwindow)

def swapToIndBDA():
    for widgets in mainwindow.winfo_children():
        if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
                room = indiceBDA.BDAClue(mainwindow)

def swapToIndFATSE():
    for widgets in mainwindow.winfo_children():
        if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
                room = indiceFATSE.FATSEClue(mainwindow)

def swapToIndBDS():
    for widgets in mainwindow.winfo_children():
        if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
                room = indiceBDS.BDSClue(mainwindow)
                
def swapToIndBDE():
    for widgets in mainwindow.winfo_children():
        if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
                room = indiceBDE.BDEClue(mainwindow)

def back():
    for widgets in mainwindow.winfo_children():
      if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
    startGame()

def pause_music():
    global pause
    if pause == False:
        pygame.mixer.music.pause()
        pause = True
    else:
        pygame.mixer.music.unpause()
        pause = False
    
# Programme principal : fenêtre d'accueil
mainwindow=tk.Tk()
mainwindow.title("Escape Game")
mainwindow.geometry("800x600")

start_canvas = tk.Canvas(mainwindow,width=800,height=600)
start_canvas.pack(fill="both", expand=True)

img = ImageTk.PhotoImage(Image.open("bg_images/bg.jpg"))
start_canvas.create_image(-150,-100,image=img,anchor="nw")


titre = start_canvas.create_text(400, 50, text="RACKE'TSE", font=("Verdana",20, "bold"),fill="darkblue")

canvas_rulestext = start_canvas.create_text(100,140, text='',anchor="nw",fill="white")
rulestext = "Bienvenue dans Racke'tse, un jeu \nd'enquête où se mêlent réflexion et \nsuspense...\nLa trésorerie du gala a disparu ! Sauras-tu\n retrouver quelle association est la \n coupable ?"
delta = 30
delay = 0
for x in range(len(rulestext)+1):
    s = rulestext[:x]
    newtext = lambda s=s:start_canvas.itemconfigure(canvas_rulestext, text=s)
    start_canvas.after(delay,newtext)
    delay +=delta


# Style des boutons
button_style = {
    "fg": "#902038",     # Couleur du texte
    "font": ("Verdana", 14, "bold"),   # Police en gras, taille 14
    "bd": 3,           # Largeur de la bordure de 3 pixels
    "relief": "ridge", # Type de bordure en relief
    "activebackground": "#2B91FF",    # Couleur de fond lors du survol de la souris
    "activeforeground": "white",      # Couleur du texte lors du survol de la souris
    "highlightcolor": "#F4FA58",      # Couleur de la bordure lors du survol de la souris
    "highlightbackground" : "darkgrey",
    "highlightthickness": 2,          # Epaisseur de la bordure lors du survol de la souris
    "cursor": "hand2"    # Curseur de souris en forme de main pour indiquer l'interactivité
}

# Style des boutons des portes
def button_style_doors(button,font_size):
    style = {
        "fg": "#902038",     # Couleur du texte blanc
        "font": ("Verdana", font_size, "bold"),   # Police en gras, taille 14
        "bd": 2,           # Largeur de la bordure de 3 pixels
        "relief": "ridge", # Type de bordure en relief
        "activebackground": "#2B91FF",    # Couleur de fond lors du survol de la souris
        "activeforeground": "white",      # Couleur du texte lors du survol de la souris
        "highlightcolor": "#F4FA58",      # Couleur de la bordure lors du survol de la souris
        "highlightbackground" : "darkgrey",
        "highlightthickness": 2,          # Epaisseur de la bordure lors du survol de la souris
        "cursor": "hand2"    # Curseur de souris en forme de main pour indiquer l'interactivité
    }
    button.config(**style)

# Création du bouton Start
start_button = tk.Button(mainwindow, text="START", **button_style, command=startGame)
start_button_window = start_canvas.create_window(540,140,anchor="nw", window=start_button)

timer_text = start_canvas.create_text(700,20, text='30:00',anchor="nw",fill="white",font=("Helvetica",20, "bold"))
countdown_time = 1800

def createMenu():
    menu=tk.Menu(mainwindow)
    about=tk.Menu(menu,tearoff=0)
    about.add_command(label="Scénario",command=scenarioWindow,activebackground="grey")
    about.add_command(label="A propos",command=aProposWindow,activebackground="grey")
    menu.add_cascade(label="Contexte", menu=about)

    indices=tk.Menu(menu,tearoff=0)
    indices.add_command(label="Enigme BDA", command=swapToIndBDA)
    indices.add_command(label="Enigme FATSE", command=swapToIndFATSE)
    indices.add_command(label="Enigme BDS", command=swapToIndBDS)
    indices.add_command(label="Enigme BDE", command=swapToIndBDE)
    menu.add_cascade(label="Indice",menu=indices)

    options=tk.Menu(menu,tearoff=0)
    options.add_command(label="Chrono",command=None)
    options.add_command(label="Musique On/Off",command=pause_music)
    menu.add_cascade(label="Options",menu=options)

    close=tk.Menu(menu,tearoff=0)
    menu.add_cascade(label="Fermer",command=mainwindow.quit)
    mainwindow.config(menu=menu)
createMenu()

mainwindow.mainloop()
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
import camera
import bde
import inspire
import bda
import bds
import fatse
import indiceBDA

# Crée une nouvelle fenêtre décrivant le scénario
def scenarioWindow():
    scenarioWin = tk.Toplevel(mainwindow)
    scenarioWin.title("Scénario")
    scenarioWin.geometry("450x600")
    scenarioLabel = tk.Label(scenarioWin, text="Salut ! Je suis confronté(e) à une situation \n"
                                            +" délicate et je me permets de solliciter ton \n"
                                            +" aide pour m'aider à résoudre cette affaire.\n"
                                            +" Il semblerait que l'argent récolté lors du\n"
                                            +" Gala de l'école a été volé et les soupçons se \n"
                                            +"portent sur l'une des associations de l'école.\n"
                                            +" Je sais que tu as l'esprit analytique et la\n"
                                            +" capacité de résoudre les mystères, c'est \n"
                                            +"pourquoi je fais appel à toi. J'ai besoin \n"
                                            +"de quelqu'un en qui je peux avoir \n"
                                            +"confiance pour m'aider à mener l'enquête et \n"
                                            +"identifier les responsables de ce vol. Je \n"
                                            +"sais que c'est une tâche difficile, mais je suis \n"
                                            +"persuadé(e) que tu es capable de relever ce défi.",font=("Verdana",12))
    scenarioLabel.pack()

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


    new_img = ImageTk.PhotoImage(Image.open("couloir.jpg"))
    new_img.img = new_img
    new_canvas.create_image(0,0,image=new_img,anchor="nw")
    
    timer_text = top_canvas.create_text(700,0, text='60:00',anchor="nw",fill="darkblue",font=("Helvetica",20, "bold"),tags=("timer"))
    

    def update_timer():
        global countdown_time
        minutes, seconds = divmod(countdown_time, 60)
        # Format the time as MM:SS
        timer_hour = f"{minutes:02d}:{seconds:02d}"
        top_canvas.itemconfig(timer_text, text=timer_hour)
        if countdown_time > 0:
            # Schedule the function to be called again after 1 second
            countdown_time -= 1
            top_canvas.after(1000, update_timer)
    
    update_timer()
    new_canvas.create_text(400,460,text="Vous voici dans le couloir\n des associations. Commencez à\n enquêter en choisissant dans \nquelle association vous souhaitez\n récolter des indices")
    
    button1 = tk.Button(mainwindow, text="BDE", **button_style, command = swapToBg1)
    button1_window = new_canvas.create_window(540,90,anchor="nw", window=button1)
    
    button2 = tk.Button(mainwindow, text="BDS", **button_style, command = swapToBg2)
    button2_window = new_canvas.create_window(540,200,anchor="nw", window=button2)
    
    button3 = tk.Button(mainwindow, text="BDA", **button_style, command = swapToBg3)
    button3_window = new_canvas.create_window(540,310,anchor="nw", window=button3)
    
    button4 = tk.Button(mainwindow, text="INSPIRE", **button_style, command = swapToBg4)
    button4_window = new_canvas.create_window(540,420,anchor="nw", window=button4)

    button4 = tk.Button(mainwindow, text="FATSE", **button_style, command = swapToBg5)
    button4_window = new_canvas.create_window(540,530,anchor="nw", window=button4)

    buttonEnd = tk.Button(mainwindow, text="Accuser", **button_style, command = startCamera)
    buttonEnd_window = new_canvas.create_window(350,100,anchor="nw", window=buttonEnd)

def startCamera():
    camWindow = tk.Toplevel(mainwindow)
    camWindow.title("Caméra")
    camWindow.geometry("450x600")
    cam = camera.CameraApp(camWindow)
    
def swapToBg1():
    for widgets in mainwindow.winfo_children():
        if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
                room = bde.Room(mainwindow)
                
def swapToBg2():
    for widgets in mainwindow.winfo_children():
      if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
                room = bds.BDS(mainwindow)
def swapToBg3():
    for widgets in mainwindow.winfo_children():
      if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
                room = bda.BDARiddle(mainwindow)
    
def swapToBg4():
    for widgets in mainwindow.winfo_children():
      if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
                room = inspire.InspireRiddle(mainwindow)

def swapToBg5():
    for widgets in mainwindow.winfo_children():
      if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
            else :
                buttonBack = tk.Button(mainwindow, text="Back", **button_style, command = back)
                button4_window = widgets.create_window(40,0,anchor="nw", window=buttonBack)
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

def back():
    for widgets in mainwindow.winfo_children():
      if isinstance(widgets, tk.Canvas):
            if widgets.winfo_name() != "timer":
                widgets.destroy()
    startGame()
    
# Programme principal : fenêtre d'accueil
mainwindow=tk.Tk()
mainwindow.title("Escape Game")
mainwindow.geometry("800x600")

start_canvas = tk.Canvas(mainwindow,width=800,height=600)
start_canvas.pack(fill="both", expand=True)

img = ImageTk.PhotoImage(Image.open("bg.jpg"))
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
    "fg": "#902038",     # Couleur du texte blanc
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

# Création du bouton Start
start_button = tk.Button(mainwindow, text="START", **button_style, command=startGame)
start_button_window = start_canvas.create_window(540,140,anchor="nw", window=start_button)

timer_text = start_canvas.create_text(700,20, text='60:00',anchor="nw",fill="white",font=("Helvetica",20, "bold"))
countdown_time = 3600

def createMenu():
    menu=tk.Menu(mainwindow)
    about=tk.Menu(menu,tearoff=0)
    about.add_command(label="Scénario",command=scenarioWindow,activebackground="grey")
    about.add_command(label="A propos",command=scenarioWindow,activebackground="grey")
    menu.add_cascade(label="Contexte", menu=about)

    indices=tk.Menu(menu,tearoff=0)
    indices.add_command(label="Enigme BDA", command=swapToIndBDA)
    indices.add_command(label="Enigme 2", command=None)
    indices.add_command(label="Enigme 3", command=None)
    menu.add_cascade(label="Indice",menu=indices)

    options=tk.Menu(menu,tearoff=0)
    options.add_command(label="Chrono",command=None)
    options.add_command(label="Musique",command=None)
    menu.add_cascade(label="Options",menu=options)

    close=tk.Menu(menu,tearoff=0)
    menu.add_cascade(label="Fermer",command=mainwindow.quit)
    mainwindow.config(menu=menu)
createMenu()

mainwindow.mainloop()
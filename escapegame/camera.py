import cv2
import tkinter as tk
from PIL import Image, ImageTk
from classification import ImageClassifier
class CameraApp:
    def __init__(self, master,master2):
        self.master = master
        self.master2 = master2
        self.camera = cv2.VideoCapture(0)

        self.canvas = tk.Canvas(self.master, width=640, height=480)
        self.canvas.pack()

        self.btn_capture = tk.Button(self.master, text="Capture", command=self.capture())
        self.btn_capture.pack()

        self.update_stream()

    def update_stream(self):
        _, frame = self.camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        self.canvas.create_image(0, 0, anchor="nw", image=imgtk)
        self.canvas.imgtk = imgtk
        self.master.after(10, self.update_stream)

    def capture(self):
        self.btn_classify = tk.Button(self.master, text="Classifier", command=self.classify)
        self.btn_classify.pack()    
        _, frame = self.camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img.save("reponse.jpg")
        
    def classify(self):
        image_classifier = ImageClassifier()
        classe = image_classifier.predict_single_image("reponse.jpg")
        for widgets in self.master2.winfo_children():
            if isinstance(widgets, tk.Canvas):
                widgets.destroy()
        self.success_canvas = tk.Canvas(self.master2, width=463, height=260)            
        self.success_canvas.pack(fill="both",expand=True)
        if classe == "BDA" :
            self.success_img = ImageTk.PhotoImage(Image.open("bg_images/victoire.jpg"))
            self.success_img.img = self.success_img
            self.success_canvas.create_image(0,0,image=self.success_img,anchor="nw")
            self.success_label = tk.Label(text="Victoire !\nVous avez réussi à trouver le voleur ! C'était bien le BDA qui était à l'origine du crime. Grâce à toi, les couloirs de TSE sont plus sûrs, désormais !",font=("Verdana",10, "bold"),fg="darkblue",wraplength=250, justify="left")
            self.success_label.place(x=555, y=50)
        else :
            self.success_img = ImageTk.PhotoImage(Image.open("bg_images/thief.png"))
            self.success_img.img = self.success_img
            self.success_canvas.create_image(80,0,image=self.success_img,anchor="nw")
            self.success_canvas.create_text(400,360,text="Le voleur a réussi à s'enfuir... Il va pouvoir se la couler\ndouce pendant que les assos de TSE devront se\ndémener pour renflouer les caisses récemment vidées...",font=("Verdana",12, "bold"),fill="gold")

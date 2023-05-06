import cv2
import tkinter as tk
from PIL import Image
class CameraApp:
    def __init__(self, master):
        self.master = master
        self.camera = cv2.VideoCapture(0)

        self.canvas = tk.Canvas(self.master, width=640, height=480)
        self.canvas.pack()

        self.btn_capture = tk.Button(self.master, text="Capture", command=self.capture)
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
        _, frame = self.camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img.save("Test.jpg")

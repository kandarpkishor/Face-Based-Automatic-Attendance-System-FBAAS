#import modules
import cv2
import numpy as nm
import tkinter as tk 
from tkinter import *
import tkinter.ttk as ttk
import os
import  tkinter.messagebox as messagebox
from PIL import Image
# import ttkthemes 
import time as tm
global sample_screen
sample_screen = Tk()
    #photo = PhotoImage(file = "bg.gif")
sample_screen.geometry("1100x640")
sample_screen.title("Face Based Attendane System")
# background_image =PhotoImage(file = 'bg.gif')
# bg_home_frame = PhotoImage(file = 'images/bg_home_frame.gif')
    # Label widget is used to display text or image on screen
# background_labe =Label(sample_screen, image = background_image)
    #background_label.image = background_image
# background_labe.place(x = 0, y = 0, relwidth = 1, relheight = 1)
collect_btn=Button(sample_screen, text="Collect Sample", width="18",  fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6").place(x=300, y=220)
# PanelA=Tk.Panel(sample_screen, text="Collect Sample", width="180",  fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6").place(x=300, y=250)

cap = cv2.VideoCapture(2)
while True:
    succ, img=cap.read()
    photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img))
    
    canvas = Canvas(sample_screen, width = 400, height = 400, bg="#008000")
    img_gui=canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)


    canvas.place(x=300, y=250)
    canvas.create_image("image", img)
    key=cv2.waitKey(1)
    if key==13:
        break
cap.release();
cv2.destroyAllWindows()

sample_screen.mainloop()


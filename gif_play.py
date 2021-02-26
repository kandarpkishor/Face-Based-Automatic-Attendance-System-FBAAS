from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
import os
from tkinter import messagebox
import face_recognition
from database import connection as cn
# import attendance as att
import tkinter as tk
from tkcalendar import Calendar, DateEntry
# import pillow as pw
from PIL import Image
import datetime
import time as tm
import tkinter.ttk as ttk 
import pickle

path = "Images"
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
root=Tk()
root.geometry("1100x640")
# lbl=Label(root)
x_ax=20
label=[{"one"},{"two"},{"three"}, {"four"}, {"five"}, {"six"}, {"seven"}, {"eight"}, {"nine"}, {"ten"}]
def display_img(img,x_axis, y_axis):
    lbl=Label(root, image=pic).place(x=x_axis, y=y_axis)
    # root.update()
# label_list=[]
label = list(range(len(images)))
print(label)
for img, lbl, i in zip(myList, label, range(18)):
    print(img)
    x_ax+=100
    y_ax=20
    path="Images/"+img
    # label[i]=Frame(root, height=200, width=300).place(x=x_ax, y=80)
    pic=ImageTk.PhotoImage(Image.open(path))
    display_img(pic,x_ax, 80)
    root.update()



root.mainloop()
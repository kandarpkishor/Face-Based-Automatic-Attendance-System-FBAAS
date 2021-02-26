import cv2
import numpy as np
import face_recognition
import tqdm
import os
from tqdm import tqdm 
from tkinter import *
from datetime import datetime
import pickle
from PIL import ImageTk
from PIL import Image
import cv2
import face_recognition
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
root=Tk()
root.geometry("1100x640")
lbl_img=Label(root)
lbl_img.pack()
imgSneha = face_recognition.load_image_file('Images/frame.jpg')
imgSneha = cv2.cvtColor(imgSneha,cv2.COLOR_BGR2RGB)

faces = face_classifier.detectMultiScale(imgSneha,1.5,5)
print(faces)
faceLoc = face_recognition.face_locations(imgSneha)[0]

print(faceLoc)
cv2.rectangle(imgSneha,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2) # top, right, bottom, left
# cv2.rectangle(imgSneha,(faces[0][0],faces[0][2]),(faces[0][1],faces[0][2]),(255,0,255),2) # top, right, bottom, left

x,h,w,y=faceLoc
# (x,y,w,h)=faces
# print(x-w)
# print(h)
# print(w)
# print(y-h)
# img = imgSneha.crop([ left, , right, lower])
cv2.line(imgSneha, (y,x), (y,0),  (255,255,255), 5)
# img=imgSneha[y:y+200, x:x+200]
# for(x,y,w,h) in faces:
# 	img = imgSneha[y:y+h, x:x+w]

# cv2.imshow('Training Image',imgSneha)
# cv2.waitKey(0)
# imgSneha=cv2.cvtColor(imgSneha, COLOR_BGR2RGB)
frame= Image.fromarray(imgSneha)
frame=ImageTk.PhotoImage(frame)
lbl_img.configure(image=frame)
lbl_img.image=frame


root.mainloop()
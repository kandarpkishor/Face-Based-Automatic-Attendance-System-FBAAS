import cv2
import numpy as np
import face_recognition
import tqdm
import os
from tkinter.ttk import *
from tqdm import tqdm 
from tkinter import *
from datetime import datetime
import time
import pickle

# from PIL import ImageGrab

root=Tk()
root.title("progress")
root.geometry("1100x640")

    
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
progressbar=Progressbar(root, mode="determinate", length="500")
progressbar.place(x=10, y=80)
lbl_pr=Label(root)
lbl_pr.place(x=520, y=50)
# progressbar['value'] =10
def findEncodings(images):
    p_val=0
    encodeList = {}
    encode={}
    for img_name, img in zip(classNames, images):
        # # progressbar.start()
        p_val+=(100/len(classNames))
        progressbar['value'] =p_val
        print(p_val)
        lbl_pr.text=p_val
        # lbl_pr.after(2,update_idletasks)
        root.update_idletasks() 
        time.sleep(1)  

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        encode[img_name] = face_recognition.face_encodings(img)[0]
    with open('dataset_faces.dat', 'wb') as f:
        pickle.dump(encode, f)
    # progressbar.stop()
    print('Encoding Complete')

Button(root,text="Train System", command=lambda:findEncodings(images)).place(x=10, y=50)
# findEncodings(images)
root.mainloop()



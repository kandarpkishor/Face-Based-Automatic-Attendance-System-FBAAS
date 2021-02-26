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

root=Tk()
root.title("Face Based Attendance System")
root.geometry("1100x640")
nocam=PhotoImage(file="images/nocam1.png")
lbl_cam_img=Label(root, image=nocam, width="719", height="540")
lbl_cam_img.place(x=170,y=80)

def attendance():
	cap=cv2.VideoCapture(0)
	def open_cam():
		if cap.isOpened():
			ret, img=cap.read()
			
			img=cv2.resize(img, (719,540))

			with open('dataset_faces.dat', 'rb') as f:
			    all_face_encodings = pickle.load(f)
			name = list(all_face_encodings.keys())
			encodeListKnown = np.array(list(all_face_encodings.values()))
			
			 
			# while True:
			#img = captureScreen()
			imgS = cv2.resize(img,(0,0),None,0.25,0.25)
			imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
			
			facesCurFrame = face_recognition.face_locations(imgS)
			encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
			
			for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
			    matches = face_recognition.compare_faces(encodeListKnown,encodeFace, 0.4)
			    faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
			    matchIndex = np.argmin(faceDis)
			    print(matchIndex)
			    if matches[matchIndex]:
			        # name = classNames[0][matchIndex].upper()
			        print(name[matchIndex])
			        y1,x2,y2,x1 = faceLoc
			        y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
			        cv2.rectangle(img,(x1-50,y1-90),(x2+50,y2+50),(0,255,0),2)
			        # cv2.rectangle(img,(x1,y2+35),(x2,y2),(0,255,0),cv2.FILLED)
			        cv2.line(img,(x2,y1),(x2+50,y1+20),(0,255,0), 2)
			        cv2.rectangle(img,(x2+50,y1+20),(x2+300,y1+100),(0,255,0),cv2.FILLED)

			        cv2.putText(img,"Name :"+name[matchIndex] ,(x2+55,y1+45),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
			        cv2.putText(img,"Roll : 180309",(x2+55,y1+65),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
			        cv2.putText(img,"Dept. : MCA",(x2+55,y1+85),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
			img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			return(ret, img)



	def show_img():
		if cap.isOpened():
			ret, frame = open_cam()
			frame= Image.fromarray(frame)
			frame=ImageTk.PhotoImage(frame)
			lbl_cam_img.configure(image=frame)
			lbl_cam_img.image=frame
			lbl_cam_img.after(1,show_img)
	show_img()
	def close_cam():
		cap.release()
		lbl_cam_img.configure(image=nocam)
		lbl_cam_img.image=nocam
		root.update()
	btn_close_cam=Button(root, text="Close Camera", width=50, command=close_cam)
	btn_close_cam.place(x=600, y=30)



btn_open_cam=Button(root, text="Open Camera", width=50, command=attendance)
btn_open_cam.place(x=20, y=30)


root.mainloop()
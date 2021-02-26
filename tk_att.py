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
root.title("OpenCv with Tkinter")
root.geometry("1100x640")
# root.overrideredirect(1)
root.resizable(0,0)
lbl_img=Label(root, width="719", height="540")
lbl_img.place(x=100, y=80)

# canvas = Canvas(root, width =800, height =600)
# canvas.place(x=60, y=80)


cap=cv2.VideoCapture(0)
def camera_img():
    ret=False
    if cap.isOpened():

        ret, frame = cap.read()
        if cap.isOpened():
            # Return a boolean success flag and the current frame converted to BGR
            with open('dataset_faces.dat', 'rb') as f:
                all_face_encodings = pickle.load(f)
            name = list(all_face_encodings.keys())
            encodeListKnown = np.array(list(all_face_encodings.values()))
          
             
            # while True:


            success, img = cap.read()
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
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                    # cv2.rectangle(img,(x1,y2+35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.line(img,(x2,y1),(x2+50,y1+20),(0,255,0), 2)
                    cv2.rectangle(img,(x2+50,y1+20),(x2+300,y1+100),(0,255,0),cv2.FILLED)

                    cv2.putText(img,"Name :"+name[matchIndex] ,(x2+55,y1+45),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
                    cv2.putText(img,"Roll : 180309",(x2+55,y1+65),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
                    cv2.putText(img,"Dept. : MCA",(x2+55,y1+85),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
                    # markAttendance(name)

            return (ret, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        else:
            return (ret, None)
    else:
        return (ret, None)
def video_img():
    ret, frame=camera_img()
    if ret==True:
        frame= Image.fromarray(frame)
        frame=ImageTk.PhotoImage(frame)
        lbl_img.configure(image=frame)
        lbl_img.image=frame
        # canvas.create_image(0,0, image =frame)
        # root.update_idletasks() 
        # canvas.after(1,video_img)
        # lbl_img.after(1,video_img)
def snapshot():
    # Get a frame from the video source
    count=0
    face_id="180309"
    ret, frame =camera_img()
    if ret:
        cv2.imwrite("frame.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
def close_cam():
    if cap.isOpened():
        cap.release()
        ret=False
        def nocam():
            frame1=PhotoImage(file="images/nocam1.png")
            lbl_img.configure(image=frame1)
            lbl_img.image=frame1
            # lbl_img.after(1, nocam)
            # canvas.create_image(0, 0, image =frame1)
            # root.update_idletasks() 
            lbl_img.update()
            root.mainloop()
        nocam()
    else:
        print("Camera not Open")


video_img()
# btn_snapshot.configure()
# btn_snapshot.command=snapshot
btn_snapshot=Button(root, text="Close Camera", width=50, command=close_cam)
btn_snapshot.place(x=600, y=30)
frame1=PhotoImage(file="images/nocam.png")
# lbl2=Label(root, image=frame1).place(x=500,y=80)
# btn_snapshot=Button(root, text="Open Camera", width=50, command=)
# btn_snapshot.place(x=20, y=30)
print("Executation Complete")
# Button(root, text="Open Camera", width=28, command=camera_img).place(x=10, y=10)
# camera_img()
root.mainloop()
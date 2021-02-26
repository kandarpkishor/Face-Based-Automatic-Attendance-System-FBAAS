import cv2
import numpy as np
import face_recognition
import tqdm
import os
from tqdm import tqdm 
from tkinter import *
from datetime import datetime
import pickle

# from PIL import ImageGrab

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
 
def findEncodings(images):
    encodeList = {}
    encode={}
    for img_name, img, i in zip(classNames, images, tqdm(range (len(images)))):
    # for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        encode[img_name] = face_recognition.face_encodings(img)[0]
        # print(encode.keys())
        # print(np.array(list(encode.values())))

        # encodeList.append(encode)
    with open('dataset_faces.dat', 'wb') as f:
        pickle.dump(encode, f)
    print('Encoding Complete')

root=Tk()
root.title("progress")
root.geometry("1000x600")
# for i in tqdm(findEncodings(images), deac="Training...."):
#     # pass
# for i in tqdm(range (1), desc="Loading..."): 
# findEncodings(images)
root.mainloop()

# def markAttendance(name):
#     with open('Attendance.csv','r+') as f:
#         myDataList = f.readlines()
#         nameList = []
#         for line in myDataList:
#             entry = line.split(',')
#             nameList.append(entry[0])
#         if name not in nameList:
#             now = datetime.now()
#             current_date=now.strftime("%d %b %Y")
#             dtString = now.strftime('%H:%M:%S')
#             f.writelines(f'\n{name},{current_date},{dtString}')
 
#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr

# encodeListKnown = findEncodings(images)
# with open('dataset_faces.dat', 'wb') as f:
#     pickle.dump(encodeListKnown, f)
# print('Encoding Complete')



def face_rec():
    with open('dataset_faces.dat', 'rb') as f:
        all_face_encodings = pickle.load(f)
    name = list(all_face_encodings.keys())
    encodeListKnown = np.array(list(all_face_encodings.values()))
    cap = cv2.VideoCapture(0)
     
    while True:
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
        # frameSize= cv2.resize(img, (1000, 600), fx=0.75, fy=0.75)
        
        cv2.imshow('Attendance Window',img)
        key=cv2.waitKey(1)
        if key==13:
            break
    cap.release()
    cv2.destroyAllWindows()
face_rec()
   
    
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from PIL import Image, ImageDraw
# from PIL import ImageGrab

cap = cv2.VideoCapture(0)
count=0
while True:
    success, img = cap.read()
    count+=1
    # file_name_path = "Images/User."+str(count)+".jpg"
    # cv2.imwrite(file_name_path,img)
    face_landmarks_list = face_recognition.face_landmarks(img)
    # pil_image = Image.fromarray(img)
    # d = ImageDraw.Draw(pil_image)
    key=0
    for face_landmarks in face_landmarks_list:

        # Print the location of each facial feature in this image
        for facial_feature in face_landmarks.keys():
            print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

        # Let's trace out each facial feature in the image with a line!
        for facial_feature in face_landmarks.keys():
            for i in range((len(face_landmarks[facial_feature]))-1):
                start=face_landmarks[facial_feature][i]
                end_point=face_landmarks[facial_feature][i+1]
                # print (face_landmarks[facial_feature][i+1])
            # x1, y1 ,x2, y2 = face_landmarks[facial_feature]
                cv2.line(img, start, end_point,  (255,255,255), 1)
            # d.line(face_landmarks[facial_feature], width=5)
                cv2.imshow('Webcam',img)
                key=cv2.waitKey(1)
                if key==13:
                    break
            i=0
            if key==13:
                break
        if key==13:
                break
    if key==13:
                break
    # Show the picture
    # pil_image.show()
    
cap.release()
cv2.destroyAllWindows()
   
    
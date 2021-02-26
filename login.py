
import cv2
import face_recognition

imgSneha = face_recognition.load_image_file('Images/sk.jpg')
imgSneha = cv2.cvtColor(imgSneha,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Images/sk.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
print(imgSneha)
faceLoc = face_recognition.face_locations(imgSneha)[0]
encodeSneha = face_recognition.face_encodings(imgSneha)[0]
cv2.rectangle(imgSneha,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2) # top, right, bottom, left
print("Sneha Enoding\n")
print(encodeSneha)


faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

print("Test Enoding\n")
print(encodeTest)

results = face_recognition.compare_faces([encodeSneha],encodeTest,0.25)
faceDis = face_recognition.face_distance([encodeSneha],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


#cv2.imshow('Training Image',imgSneha)
cv2.imshow('Test Image',imgTest)
cv2.waitKey(0)
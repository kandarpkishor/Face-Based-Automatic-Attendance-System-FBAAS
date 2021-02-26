from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk

root=Tk()
root.title("OpenCv with Tkinter")
root.geometry("1000x600")
lbl_img=Label(root)
lbl_img.place(x=100, y=80)
cap=cv2.VideoCapture(0)

def camera_img():
	
	succ, frame= cap.read()
	frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	frame= Image.fromarray(frame)
	frame=ImageTk.PhotoImage(frame)
	lbl_img.configure(image=frame)
	lbl_img.image=frame
	lbl_img.after(1,camera_img)
print("Executation Complete")
Button(root, text="Open Camera", width=28, command=camera_img).place(x=10, y=10)
# camera_img()
root.mainloop()




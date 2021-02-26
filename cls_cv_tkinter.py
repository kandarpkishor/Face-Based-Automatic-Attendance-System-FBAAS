from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk

class videoStream:
	lbl_img=None
	root=None
	cap=None
	def __init__(self):
		self.root=Tk()
		self.root.title("OpenCv with Tkinter")
		self.root.geometry("1000x600")
		self.lbl_img=Label(self.root, height="400", width="500", bg="black")
		self.lbl_img.pack()
		self.cap=cv2.VideoCapture(0)
		self.camera_img()
		self.root.mainloop()

	def camera_img(self):
		_,frame= self.cap.read()
		frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		frame= Image.fromarray(frame)
		frame=ImageTk.PhotoImage(frame)
		self.lbl_img.configure(image=frame)
		self.lbl_img.image=frame
		self.lbl_img.after(1,self.camera_img)

if __name__ == '__main__':
	objVideo= videoStream()
	print("Executation Complete")




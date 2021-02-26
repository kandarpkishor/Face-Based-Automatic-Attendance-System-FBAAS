from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk

root=Tk()
root.title("OpenCv with Tkinter")
root.geometry("1000x600")
lbl_img=Label(root)
lbl_img.place(x=100, y=80)
canvas = Canvas(root, width =400, height =200)
canvas.place(x=600, y=80)


cap=cv2.VideoCapture(0)
def camera_img():
	if cap.isOpened():
	    ret, frame = cap.read()
	    if ret:
	        # Return a boolean success flag and the current frame converted to BGR
	        return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
	    else:
	        return (ret, None)
	else:
	    return (ret, None)
def video_img():
	ret, frame=camera_img()
	frame= Image.fromarray(frame)
	frame=ImageTk.PhotoImage(frame)
	lbl_img.configure(image=frame)
	lbl_img.image=frame
	canvas.create_image(0, 0, image =frame)
	lbl_img.after(1,video_img)
def snapshot():
    # Get a frame from the video source
    count=0
    face_id="180309"
    ret, frame =camera_img()
    if ret:
        cv2.imwrite("frame.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
   


video_img()
# btn_snapshot.configure()
# btn_snapshot.command=snapshot
btn_snapshot=Button(root, text="Snapshot", width=50, command=snapshot)
btn_snapshot.place(x=600, y=20)
print("Executation Complete")
# Button(root, text="Open Camera", width=28, command=camera_img).place(x=10, y=10)
# camera_img()
root.mainloop()




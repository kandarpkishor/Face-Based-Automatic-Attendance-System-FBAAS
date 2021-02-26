from tkinter import *
import cv2
import numpy as np
from PIL import Image
from PIL import ImageTk
import os
from tkinter import messagebox
import face_recognition
from database import connection as cn
import tkinter as tk
from tkcalendar import Calendar, DateEntry
from PIL import Image
import datetime
import time as tm
import tkinter.ttk as ttk 
import pickle


def login():
	# username = username_verify.get()
	# password = password_verify.get()
	username = "kkjha"
	password = "kkjha"
	
	if username=="":
		msg=messagebox.showwarning(title="Alert", message=" Enter Username")
	else:
		if password=="":
			msg=messagebox.showwarning(title="Alert", message=" Enter Password")
		else:
			print(username)
			print(password)
			# fetching data from database
			conn=cn.create_connection("database/attendance_db.SQLite")
			val=(username,password)
			cursor = conn.cursor()
			cursor.execute('SELECT *FROM users WHERE username=? AND password=?', val)
			row=cursor.fetchone()
			user_name=row[1]
			if username==row[3] and password==row[4]:
				# msg=messagebox.showinfo(title="Message", message="Login Successfull")
				home_screen()
				conn.close()
				# add_account_screen()
			else:
				msg=messagebox.showwarning(title="Message", message="Enter valid username and password")
			# user_entry.delete(0, END)
			# pass_entry.delete(0, END)
			conn.close()
# print(user_name)
global root 
root = Tk()
root.resizable(0,0)
root.title("Face Based Automatic Attendance System")
background_image =PhotoImage(file = 'images/bg2.png')
# Label widget is used to display text or image on screen
background_label =Label(root, image = background_image)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
root.geometry("1100x640")

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list
# Home page GUI

def home_screen():
	widget_list = all_children(root)
	for item in widget_list:
		item.destroy()

	background_image =PhotoImage(file = 'images/home_bg.png')
	# Label widget is used to display text or image on screen
	

	global home_frame
	header_frame= Frame(root,width=780, height=55, bd="2", highlightbackground="black", highlightthickness="1").place(x=20, y=20)
	date_frame= Frame(root,width=265, height=55, bd="2", highlightbackground="black", highlightthickness="1").place(x=805, y=20)
	add_people = PhotoImage(file = 'images/add_people.gif')
	home_frame=Frame(root,width=1050,height=540, bd="2", highlightbackground="black", highlightthickness="1" )
	home_frame.place(x=20, y=80)
	# Button(home_frame, text="Login", width=40, height=1, fg="white", command=att.face_rec, bg="#008000", font=('calibri', 13, 'bold'),activebackground="#006600",activeforeground="#e6ffe6").place(x=20, y=175)
	
	background_label =Label(home_frame, image = background_image)
	background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	root.geometry("1100x640")

	collect_sample = PhotoImage(file = 'images/collect_sample.gif')
	train_system = PhotoImage(file = 'images/train_system.gif')
	mark_attendance=PhotoImage(file= 'images/mark_attendance.gif')
	attendance_report= PhotoImage(file = 'images/attendance_report.gif')
	view_sample = PhotoImage(file = 'images/sample1.gif')
	setting = PhotoImage(file = 'images/settings.png')
	exit_image = PhotoImage(file='images/exit.png')

	
	

	sample_button=Button(home_frame, text="Add People", command=add_account_screen, image= add_people, height="160", width="160", font=("calibri",13)).place(x=10, y=10)
	attendance_button=Button(home_frame, text="Mark Attendance", command=attendance_screen, image=mark_attendance, height="160", width="160", font=("calibri",13)).place(x=190, y=10)
	report_button=Button(home_frame,text="Attendance Report", command=report_screen, image=attendance_report, height="160", width="160", font=("calibri",13)).place(x=380, y=10)
	sample_button=Button(home_frame, text="Collect Sample", command=collect_sample_screen, image=collect_sample,height="160", width="160", font=("calibri",13)).place(x=10, y=185)
	train_button=Button(home_frame, text= "Train Model", command=train_system_screen, image=train_system,height="160", width="160", font=("calibri",13)).place(x=190, y=185)
	
	view_sample_button=Button(home_frame, text="View Sample", image=view_sample, height="160", width="160", font=("calibri",13)).place(x=380, y=185)
	setting_button=Button(home_frame, text="Settings", image=setting, height="160", width="160", font=("calibri",13)).place(x=10, y=360)
	exit_button=Button(home_frame, text="Exit", image=exit_image, command=exit, height="160", width="160", font=("calibri",13)).place(x=190, y=360) 
	#Button(home_frame, text="Login", width=50, height=1, fg="white", bg="#008000", font=('calibri', 13, 'bold'),activebackground="#006600",activeforeground="#e6ffe6").place(x=20, y=175)    
	current_date = datetime.datetime.now()
	current_date=current_date.strftime("%A, %d %b %Y")
	background_label =Label(root, image = sample_button)
	# user_label = Label(root, text="user_name", font=("Helvetica", 15)).place(x=810, y=10)
	date=Label(date_frame,text=current_date, font=("Helvetica", 14))
	date.place(x=810, y=30)
	head=Label(header_frame, text="Face Based Automatic Attendance System",font=("Helvetica",20)).place(x=160,y=35)

	def showtime():
	    current_time=tm.strftime('%H:%M:%S')
	    time=Label(date_frame,text=current_time, font=("Helvetica", 14), )
	    time.place(x=810, y=50)
	    #print(current_time)
	    time.after(200,showtime)
	showtime()
	root.mainloop()
# home_screen()
def exit():
	widget_list = all_children(root)
	for item in widget_list:
		item.destroy()
	root.destroy()

# Add Student
def add_student():
    nm_val=nm.get()
    fnm_val=fnm.get()
    gender_val=gender.get()
    roll_val=role.get()
    sem_val=sem.get()
    mobile_val=mob.get()
    email_val= email.get()
    select_class_val=select_class_var.get()
    current_date = datetime.datetime.now()
    date=current_date.strftime("%d %b %Y")
    
    # nm_val="Keshav Kishor Jha"
    # fnm_val="Dinesh Kunar Jha"
    # gender_val="Male"
    # roll_val="180309"
    # sem_val="4th"
    # mobile_val="8877972243"
    # email_val= "kishor.keshav.jha@gmail.com"
    # select_class_val="MCA"
    # date ='2020-07-20'
    conn=cn.create_connection("database/attendance_db.SQLite")

    
    if (not nm_val) or (not fnm_val) or (not roll_val) or (not sem_val) or (not nm_val) or (not mobile_val) or (not email_val) or (select_class_val=="--Select Department--"):
        msg=messagebox.showwarning(title="Warning", message="Please fill all details")
    else:
    	value=(nm_val, fnm_val, gender_val, roll_val, sem_val, select_class_val, email_val, mobile_val,date)
    	cursor = conn.cursor()
    	cursor.execute("INSERT INTO STUDENT (ID, NAME, F_NAME, GENDER, ROLL_NO, SEMESTER, DEPARTMENT, EMAIL_ID, MOBILE, ENROLLMENT_DATE) VALUES(NULL,?,?,?, ?, ?, ?, ?, ?,?)", value)
    	if cursor.execute :
    	    msg=messagebox.showinfo(title="Message", message="Student Added Successfully")
    	    conn.commit()
    	    add_account_screen()
    conn.close()
# Get Profile
        

# add people GUI
def add_account_screen():

	widget_list = all_children(root)
	for item in widget_list:
		item.destroy()
	ackground_image =PhotoImage(file = 'images/bg2.png')
	# Label widget is used to display text or image on screen
	background_label =Label(root, image = background_image)
	background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	global add_people_frame
	add_people_frame=Frame(root,width=380,height=540, bd="2", highlightbackground="black", highlightthickness="1" )
	add_people_frame.place(x=20, y=80)
	global nm
	nm = StringVar()
	global fnm
	fnm = StringVar()
	global gender
	gender=StringVar()
	global dob
	dob =StringVar()
	global role

	role = StringVar()
	global sem
	sem = StringVar()
	global mob
	mob = StringVar()
	global email
	email = StringVar()
	global select_class
	global select_class_var

	home_btn=Button(root, text="Back", command=home_screen, width="26", fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6").place(x=20, y=30)
	cls_lbl=Label(add_people_frame, text="Select Department ").place(x=5,y=65)

	options = ('--Select Department--','MCA', 'MBA', 'B.Tech (CE)', 'B.Tech(EE)', 'B.Tech(CSE)', 'B.Tech(PPT)', 'M.Com', 'M.Sc (Physics)', 'M.Sc (Che)', 'M.Sc (Math)')
	select_class_var = StringVar(add_people_frame)
	#select_class_var = 'MCA'
	select_class_var.set(options[0])
	select_class=OptionMenu(add_people_frame, select_class_var, *options)
	select_class.config(width="20")
	# labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
	# labelTest.pack(side="top")
	# def callback(*args):
	#     labelTest.configure(text="The selected item is {}".format(select_class_var.get()))
	# select_class_var.trace("w", callback)
	select_class.place(x=150, y=60)

	#background_add_fram_label=Label(add_people_frame, bg="#80d4ff", height="35", width="150").pack()
	head_lbl=Label(add_people_frame, text="Student Registration Form ", font=("calibri",13)).place(x=80,y=20)
	nm_lbl=Label(add_people_frame, text="Name ").place(x=5,y=100)
	nm_entry=Entry(add_people_frame, textvariable=nm, width="26").place(x=150,y=100)
	fnm_lbl=Label(add_people_frame, text="Fathers Name ").place(x=5,y=130)
	fnm_entry=Entry(add_people_frame, textvariable=fnm, width="26").place(x=150,y=130)

	dob_lbl=Label(add_people_frame, text="Date of Brth ").place(x=5,y=160)
	dob_entry=DateEntry(add_people_frame, textvariable=dob, width="25").place(x=150,y=160)

	gender_lbl=Label(add_people_frame, text="Gender ").place(x=5,y=190)
	gender_entry=Entry(add_people_frame, textvariable=gender, width="26").place(x=150,y=190)

	role_lbl=Label(add_people_frame, text="Roll No. ").place(x=5,y=220)
	role_entry=Entry(add_people_frame, textvariable=role, width="26").place(x=150,y=220)
	sem_lbl=Label(add_people_frame, text="Semester ").place(x=5,y=250)
	sem_entry=Entry(add_people_frame, textvariable=sem, width="26").place(x=150,y=250)
	#dob_lbl=Label(add_people_frame, text="Date of Birth ").place(x=5,y=180)
	#dob_date=Entry(add_people_frame, textvariable="dob").place(x=150,y=180)
	mob_lbl=Label(add_people_frame, text="Mobile No. ").place(x=5,y=280)
	mob_entry=Entry(add_people_frame, textvariable=mob, width="26").place(x=150,y=280)
	email_lbl=Label(add_people_frame, text="Email Id ").place(x=5,y=310)
	email_entry=Entry(add_people_frame, textvariable=email, width="26").place(x=150,y=310)
	add_btn=Button(add_people_frame, command=add_student, text="Add Student", width="26", fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6").place(x=70, y=340)



	# Manage Department GUI
	global manage_dept_frame
	def get_profile(s_id):
		manage_dpt_frame=Frame(root,width=660,height=230, bd="2", highlightbackground="black", highlightthickness="1" )
		manage_dpt_frame.place(x=410, y=390)
		val=(s_id,)
		conn=cn.create_connection("database/attendance_db.SQLite")
		cursor = conn.cursor()
		cursor.execute('SELECT  *FROM student WHERE ROLL_NO like ?',val)
		row=cursor.fetchone()
		if len(row)>0:
			global face_id
			Label(manage_dpt_frame, text="Name :").place(x=10,y=20)
			Label(manage_dpt_frame,text=row[2]).place(x=140, y=20)
			Label(manage_dpt_frame, text="Fathers Name :").place(x=10,y=45)
			Label(manage_dpt_frame,text=row[3]).place(x=140, y=45)
			Label(manage_dpt_frame, text="Gender :").place(x=10,y=70)
			Label(manage_dpt_frame,text=row[4]).place(x=140, y=70)
			Label(manage_dpt_frame, text="Date of Birth :").place(x=250,y=70)
			Label(manage_dpt_frame,text=row[5]).place(x=350, y=70)

			Label(manage_dpt_frame, text="Roll No. :").place(x=10,y=95)
			Label(manage_dpt_frame,text=row[6]).place(x=140, y=95)

			Label(manage_dpt_frame, text="Semester :").place(x=250,y=95)
			Label(manage_dpt_frame,text=row[7]).place(x=350, y=95)

			Label(manage_dpt_frame, text="Department :").place(x=10,y=120)
			Label(manage_dpt_frame,text=row[8]).place(x=140, y=120)
			print(row[1])
			# 
			# 
			image = Image.open("face_sample/"+row[6]+"_1.jpg")

			image = image.resize((140, 160), Image.ANTIALIAS) ## The (250, 250) is (height, width)
			image.save("profile/"+row[6]+".png", "png")
			profile_pic=PhotoImage(file="profile/"+row[6]+".png")
			if profile_pic:

			# profile_pic = PhotoImage(image)
			# 
			# global img 
			# img.destroy()
				img=Label(manage_dpt_frame, image=profile_pic,  height=160, width=140, highlightbackground="black", highlightthickness=2).place(x=450, y=25)


			Label(manage_dpt_frame, text="Mobile :").place(x=10,y=145)
			Label(manage_dpt_frame,text=row[10]).place(x=140, y=145)
			Label(manage_dpt_frame, text="Email Id :").place(x=10,y=170)
			Label(manage_dpt_frame,text=row[9]).place(x=140, y=170)
			root.mainloop()
		conn.close()


	#view Student frame
	global view_frame
	view_frame=Frame(root,width=660,height=300, bd="2", highlightbackground="black", highlightthickness="1" )
	view_frame.place(x=410, y=80)
	Label(view_frame,text="Enrolled Student", bg="blue", fg="white", width=65, font=("Helvetica", 13)).place(x=0, y=0)
	tree=ttk.Treeview(view_frame, height=12)

	vsb = ttk.Scrollbar(view_frame, orient="vertical", command=tree.yview)
	vsb.place(x=30+605+2, y=25, height=240+20)
	tree.configure(yscrollcommand=vsb.set)



	tree["columns"]=("sl", "one","two","three", "four","five", "six")
	tree.column("#0", width=0, minwidth=0, stretch=tk.NO)
	tree.column("sl", width=35, minwidth=0, stretch=tk.NO)

	tree.column("one", width=160, minwidth=270,  stretch=tk.NO)
	# tree.column("one", width=50, minwidth=100, stretch=tk.NO)
	tree.column("two", width=70, minwidth=50, anchor="center",)
	tree.column("three", width=90, minwidth=80, stretch=tk.NO)
	tree.column("four", width=100, minwidth=40,stretch=tk.NO)
	tree.column("five", width=100, minwidth=40,stretch=tk.NO)
	tree.column("six", width=75, minwidth=150,stretch=tk.NO)
	tree.heading("#0",text="",anchor=tk.W)
	tree.heading("sl",text="Sl",anchor=tk.W)
	tree.heading("one",text="Name",anchor=tk.W)
	# tree.heading("one", text="Face Id",anchor=tk.W)
	tree.heading("two", text="Roll No",anchor=tk.W)
	tree.heading("three", text="Semester",anchor=tk.W)
	tree.heading("four", text="Department",anchor=tk.W)
	tree.heading("five", text="Mobile",anchor=tk.W)
	tree.heading("six", text="Acton",anchor=tk.W)
	def fetchdetail():
		conn=cn.create_connection("database/attendance_db.SQLite")
		cursor = conn.cursor()
		cursor.execute("SELECT *FROM STUDENT")
		row=cursor.fetchall()
		cpt=10
		y_ax= 43
		sl_no=1;
		if len(row)>0:
			for column in row:
				# print("Data Fetched from database")
				tree.insert("", "end", values=(sl_no, column[2],column[6],column[7],column[8],column[10]))
				view_btn=Button(view_frame,text="View", command=lambda s_id=column[6]:get_profile(s_id), height= 0,font=("Helvetica", 10)).place(x=565, y=y_ax)
				y_ax +=20

				# cpt+=10
				sl_no +=1
		conn.close()
		
	
	tree.place(x=5,y=23)
	fetchdetail()

	root.mainloop()


# Report GUI
def report_screen():
	widget_list = all_children(root)
	for item in widget_list:
		item.destroy()
	ackground_image =PhotoImage(file = 'images/bg2.png')
	# Label widget is used to display text or image on screen
	background_label =Label(root, image = background_image)
	background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	#view Student frame
	home_btn=Button(root, text="Back", command=home_screen, width="26", fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6").place(x=20, y=30)
	
	report_nav=Frame(root,width=150,height=540, bd="2", highlightbackground="black", highlightthickness="1" )
	report_nav.place(x=20, y=80)
	btn_yr=Button(report_nav,text="Yearly Report", width="13", fg="white", bg="#008000", activebackground="#006600", activeforeground="#e6ffe6").place(x=5, y=60)
	btn_mn=Button(report_nav,text="Monthly Report", width="13", fg="white", bg="#008000", activebackground="#006600", activeforeground="#e6ffe6").place(x=5, y=100)

	global report_frame
	current_date = datetime.datetime.now()
	current_date=current_date.strftime("%A, %d %b %Y")
	report_frame=Frame(root,width=900,height=540, bd="2", highlightbackground="black", highlightthickness="1" )
	report_frame.place(x=170, y=80)
	Label(report_frame, text="Attendance : "+str(current_date), font=("calibri",15,"bold"), fg="Green").place(x=200, y=7)
	tree=ttk.Treeview(report_frame, height=20)

	vsb = ttk.Scrollbar(report_frame, orient="vertical", command=tree.yview)
	vsb.place(x=30+836+2, y=40, height=400+20)
	tree.configure(yscrollcommand=vsb.set)

	tree["columns"]=("on","one","two","three", "four")
	tree.column("#0", width=0, minwidth=0, stretch=tk.NO)
	tree.column("on", width=250, minwidth=270, stretch=tk.NO)
	tree.column("one", width=140, minwidth=100, stretch=tk.NO, anchor=tk.CENTER)
	tree.column("two", width=170, minwidth=80, stretch=tk.NO, anchor=tk.CENTER)
	tree.column("three", width=150, minwidth=80, stretch=tk.NO, anchor=tk.CENTER)
	tree.column("four", width=160, minwidth=80, stretch=tk.NO, anchor=tk.CENTER)
	tree.heading("on",text="Name",anchor=tk.CENTER)
	tree.heading("one", text="Roll No.",anchor=tk.CENTER)
	tree.heading("two", text="Date",anchor=tk.CENTER)
	tree.heading("three", text="Log In Time",anchor=tk.CENTER)
	tree.heading("four", text="Log Out Time",anchor=tk.CENTER)
	value=(current_date);
	def fetchdetail():
	    conn = cn.create_connection("database/attendance_db.SQLite")
	    cursor = conn.cursor()
	    cursor.execute("SELECT DISTINCT ROLL_ID, NAME, DOA, TOA FROM ATTENDANCE")# WHERE DOA LIKE ?",value[0])
	    rows=cursor.fetchall()
	    cpt=0
	    if len(rows)>0:
	        for row in rows :
	            print("Data Fetched from database")
	            print(row)
	            tree.insert("", "end", values=(row[1],row[0],row[2],row[3]))
	            cpt+=1
	
	tree.place(x=10,y=40)
	fetchdetail()






#Collect Sample Screen 

def collect_sample(face_id):
    cap=cv2.VideoCapture(0)
    lbl_img=Label(root,  highlightbackground="black", highlightthickness=2)
    lbl_img.place(x=530, y=80)
    lbl_img_count=Label(root)
    lbl_img_count.place(x=540, y=90)
    def camera_img():
    	if cap.isOpened():
    	    ret, frame = cap.read()
    	    if ret:
    	        # Return a boolean success flag and the current frame converted to BGR
    	        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    	        frame=cv2.resize(frame, (500,500))
    	        return (ret, frame)
    	    else:
    	        return (ret, None)
    	# else:
    	    # return (ret, None)
    def video_img():
    	ret, frame=camera_img()
    	# frame=frame.resize(400,400)
    	frame= Image.fromarray(frame)
    	frame=ImageTk.PhotoImage(frame)
    	lbl_img.configure(image=frame)
    	lbl_img.image=frame
    	lbl_img.after(1,video_img)
    def snapshot(img_name):
        # Get a frame from the video source
        count=0
        
        ret, frame =camera_img()
        # frame=cv2.
        if ret:
            cv2.imwrite("face_sample/"+img_name+".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    def take_img():
    	img_count=0
    	#face_id="180309"
    	#face_id=face_id;
    	print(face_id)
    	for i in range(5):
    		lbl_img_count.configure(text=str(i+1))
    		lbl_img_count.text=str(i+1)
    		snapshot(face_id+"_"+str(i+1))
    		lbl_img_count.update()
    		lbl_img.update()
    		tm.sleep(1)
    	conn=cn.create_connection("database/attendance_db.SQLite")
    	value=(face_id, face_id)
    	cursor = conn.cursor()
    	cursor.execute("UPDATE STUDENT SET FACE_ID = ? WHERE ROLL_NO LIKE ?" , (value))
    	if cursor.execute :
    		msg=messagebox.showinfo(title="Message", message="Colleting Samples Complete!!!")
    		print("hi")
    		conn.close()
    		cap.release()

    video_img()
    btn_snapshot=Button(root, text="Take Picture", command=take_img, width="60", fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6")
    btn_snapshot.place(x=530, y=30)
    # cap.release()
    # cv2.destroyAllWindows()
    









def find_student():
	select_class_val=select_class_var.get()
	print(select_class_val)
	if select_class_val=="" or select_class_val=="No Student Left":
		msg=messagebox.showwarning("Alert", "Please Select Roll Number")
		
	else:
		print(select_class_val)
		val=(select_class_val,)
		conn=cn.create_connection("database/attendance_db.SQLite")
		cursor = conn.cursor()
		cursor.execute('SELECT  *FROM STUDENT WHERE ROLL_NO like ?',val)
		row=cursor.fetchone()
		global face_id
		face_id=row[1]
		Label(collect_sample_frame, text="Student Information", font=("Helvetica",13), width="48", bg="blue", fg="white" ,highlightbackground="black", highlightthickness="2" ).place(x=3, y=0)
		Label(collect_sample_frame, text="Name :").place(x=10,y=50)
		Label(collect_sample_frame,text=row[2]).place(x=140, y=50)
		Label(collect_sample_frame, text="Fathers Name :").place(x=10,y=75)
		Label(collect_sample_frame,text=row[3]).place(x=140, y=75)
		Label(collect_sample_frame, text="Gender :").place(x=10,y=100)
		Label(collect_sample_frame,text=row[4]).place(x=140, y=100)
		Label(collect_sample_frame, text="Date of Birth :").place(x=250,y=100)
		Label(collect_sample_frame,text=row[5]).place(x=350, y=100)
		Label(collect_sample_frame, text="Roll No. :").place(x=10,y=125)
		Label(collect_sample_frame,text=row[6]).place(x=140, y=125)
		Label(collect_sample_frame, text="Semester :").place(x=250,y=125)
		Label(collect_sample_frame,text=row[7]).place(x=350, y=125)
		Label(collect_sample_frame, text="Department :").place(x=10,y=150)
		Label(collect_sample_frame,text=row[8]).place(x=140, y=150)
		Label(collect_sample_frame, text="Mobile :").place(x=10,y=175)
		Label(collect_sample_frame,text=row[10]).place(x=140, y=175)
		Label(collect_sample_frame, text="Email Id :").place(x=10,y=200)
		Label(collect_sample_frame,text=row[9]).place(x=140, y=200)
			# 
		collect_btn=Button(collect_sample_frame, text="Collect Sample", width="18", command=lambda:collect_sample(row[6]), fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6").place(x=150, y=250)
		print("row: ")
		print(row[6]) 
    
    






def collect_sample_screen():
	widget_list = all_children(root)
	for item in widget_list:
		item.destroy()
	ackground_image =PhotoImage(file = 'images/bg2.png')
	# Label widget is used to display text or image on screen
	background_label =Label(root, image = background_image)
	background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	#view Student frame
	home_btn=Button(root, text="Back", command=home_screen, width="26", fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6").place(x=20, y=30)
	
	global collect_sample_frame
	collect_sample_frame=Frame(root,width=500,height=400, bd="2", highlightbackground="black", highlightthickness="1" )
	collect_sample_frame.place(x=20, y=190)
	global select_frame
	select_frame=Frame(root,width=500,height=100, bd="2", highlightbackground="black", highlightthickness="1" )
	select_frame.place(x=20, y=80)
	global select_class
	global select_class_var
	cls_lbl=Label(select_frame, text="Select Student ", font=("Helvetica",13)).place(x=20,y=35)
	conn=cn.create_connection("database/attendance_db.SQLite")
	cursor = conn.cursor()
	cursor.execute("SELECT *FROM STUDENT where coalesce(FACE_ID, '') = ''")
	row=cursor.fetchall()
	i=0
	global options
	options=[]
	if len(row)>0:
	    for coloumn in row:
	    	options.append(coloumn[6])
	    	i+=1
	else:
	    options=('No Student Left','')
	conn.close()
	select_class_var = StringVar(collect_sample_frame)
	#select_class_var = 'MCA'
	select_class_var.set(options[0])
	select_class=OptionMenu(select_frame, select_class_var, *options)
	select_class.config(width="20")
	select_class.place(x=150, y=30)
	add_btn=Button(select_frame, text="Find Student", width="11", command=find_student, fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6").place(x=360, y=30)
	root.mainloop()




def train_system_screen():
	widget_list = all_children(root)
	for item in widget_list:
		item.destroy()
	background_image =PhotoImage(file = 'images/bg2.png')
	background_label =Label(root, image = background_image)
	background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

	home_btn=Button(root, text="Back", command=home_screen, width="26", fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6").place(x=20, y=30)
	train_frame=Frame(root,width=1060,height=545, bd="2", bg="black", highlightbackground="black", highlightthickness="1" )
	train_frame.place(x=20, y=80)

	btn_train=Button(train_frame,text="Train System", command=lambda:findEncodings(images), width="26", fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6")
	btn_train.place(x=150, y=260)
	# Training Code    
	path = "face_sample"
	images = []
	classNames = []
	myList = os.listdir(path)
	print(myList)
	for cl in myList:
	    curImg = cv2.imread(f'{path}/{cl}')
	    images.append(curImg)
	    classNames.append(os.path.splitext(cl)[0])
	print(classNames)
	# progressbar['value'] =10
	def findEncodings(images):
	    p_val=0
	    
	    progressbar=ttk.Progressbar(train_frame, mode="determinate", length="430")
	    progressbar.place(x=535, y=510)
	    lbl_pr=Label(train_frame, bg="black", fg="white")
	    lbl_pr.place(x=960, y=510)
	    encodeList = {}
	    encode={}
	    for img_name, img in zip(classNames, images):
	        p_val+=(100/len(classNames))
	        progressbar['value'] =p_val
	        lbl_pr.configure(text=str(round(p_val,2))+"%")
	        lbl_pr.text=p_val
	        root.update_idletasks() 
	        # progressbar.update() 
	        # tm.sleep(1)
	        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
	        encode[img_name] = face_recognition.face_encodings(img)[0]
	    with open('dataset_faces.dat', 'wb') as f:
	        pickle.dump(encode, f)
	    # progressbar.stop()
	    print('Encoding Complete')
	from script import gif
	# train_bg=PhotoImage(file = 'images/train.gif', format="gif -index 1")
	lbl_total_sample=Label(train_frame, text="Total Sample: "+str(len(images)), bg="black", fg="white").place(x=150, y=230)
	train_bb_label =gif.AnimatedGIF(train_frame, "images/faceman1.gif")
	train_bb_label.place(x=530,y=0)
	# btn_train.command=lambda:findEncodings(images)
	root.update()
	# findEncodings(images)
	root.mainloop()

# train_system() end


# Attendance code begin


def attendance_screen():
	widget_list = all_children(root)
	for item in widget_list:
		item.destroy()
	background_image =PhotoImage(file = 'images/bg2.png')
	background_label =Label(root, image = background_image)
	background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	home_btn=Button(root, text="Back", command=home_screen, width="26", fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6").place(x=20, y=30)
	attendance_frame=Frame(root,width=1060,height=545, bd="2", bg="black", highlightbackground="black", highlightthickness="1" )
	attendance_frame.place(x=20, y=80)
	frame_background_label =Label(attendance_frame, image = background_image).place(x = 0, y = 0, relwidth = 1, relheight = 1)
	nocam=PhotoImage(file="images/nocam1.png")
	lbl_cam_img=Label(attendance_frame, image=nocam, width="719", height="540")
	lbl_cam_img.place(x=335,y=0)
	btn_open_cam=Button(attendance_frame, text="Open Camera", width="26", fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6")
	btn_open_cam.place(x=50, y=245)
	def profile_detail(student_id):
		val=(student_id,)
		conn=cn.create_connection("database/attendance_db.SQLite")
		cursor = conn.cursor()
		cursor.execute('SELECT  *FROM student WHERE ROLL_NO like ?',val)
		row=cursor.fetchone()
		if (len(row)>0):
			return(row[6], row[2], row[8])
		conn.close()


	def attendance():
		def check_attendance(roll_no, date):
			conn=cn.create_connection("database/attendance_db.SQLite")
			cursor = conn.cursor()
			val=(roll_no, date)
			cursor.execute('SELECT  *FROM attendance WHERE ROLL_ID like ? AND DOA like ?',(val))
			row=cursor.fetchall()
			if (len(row))>0:
				return True
			conn.close()
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
				    # matchIndex1=(matchIndex,1);
				    # print("Match Index")
				    # print(matchIndex)
				    if matches[matchIndex]:
				        # name = classNames[0][matchIndex].upper()
				        fc_no=name[matchIndex]
				        # face_no=fc_no[:-1]
				        face_no=fc_no.rsplit('_',1)[0]
				        # print(name[matchIndex])
				        # print(face_no)
				        y1,x2,y2,x1 = faceLoc
				        y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
				        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
				        # cv2.rectangle(img,(x1,y2+35),(x2,y2),(0,255,0),cv2.FILLED)
				        cv2.line(img,(x2,y1),(x2+50,y1+20),(0,255,0), 2)
				        cv2.rectangle(img,(x2+50,y1+20),(x2+300,y1+100),(0,255,0),cv2.FILLED)
				        student_detail= profile_detail(face_no)
				        print(name[matchIndex])
				        cv2.putText(img,"Name :"+student_detail[1] ,(x2+55,y1+45),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
				        cv2.putText(img,"Roll :" +student_detail[0] ,(x2+55,y1+65),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
				        cv2.putText(img,"Dept. :"+student_detail[2] ,(x2+55,y1+85),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
				        # tm.sleep(2)
				        time=tm.strftime('%H:%M:%S')
				        current_date = datetime.datetime.now()
				        date=current_date.strftime("%d %b %Y")
				        check=check_attendance(student_detail[0], date)
				        if(check==True):
				        	cv2.putText(img,"Attendance Already Marked " ,(x2+55,y1+10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
				        else:
					        conn=cn.create_connection("database/attendance_db.SQLite")
					        value=(student_detail[0], student_detail[1], date, time, student_detail[2])
					        cursor = conn.cursor()
					        cursor.execute("INSERT INTO ATTENDANCE (ID, ROLL_ID, NAME, DOA, TOA, DEPARTMENT) VALUES(NULL,?,?, ?, ?, ?)", value)
					        
					        if cursor.execute :
					        	msg=messagebox.showinfo(title="Message", message="Attendance Marked Successfully")
					        	conn.commit()
					        	conn.close()
				    else:
				    	y1,x2,y2,x1 = faceLoc
				    	y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
				    	cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
				    	# cv2.rectangle(img,(x1,y2+35),(x2,y2),(0,255,0),cv2.FILLED)
				    	cv2.line(img,(x2,y1),(x2+50,y1+20),(0,255,0), 2)
				    	cv2.rectangle(img,(x2+50,y1+20),(x2+300,y1+100),(0,255,0),cv2.FILLED)
				    	cv2.putText(img,"Student Record Not Found",(x2+55,y1+45),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
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
		# btn_close_cam=Button(attendance_frame, text="Close Camera", width="26", fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6")
		# btn_close_cam.place(x=50, y=270)
		def close_cam():
			cap.release()
			lbl_cam_img.configure(image=nocam)
			lbl_cam_img.image=nocam
			btn_open_cam.configure(command=attendance, text="Open Camera")
			btn_open_cam.command=attendance
			# btn_close_cam.destroy()
			root.update()
		# btn_close_cam=Button(attendance_frame, text="Close Camera", command=close_cam, width="26", fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6")
		btn_open_cam.configure(command=close_cam, text="Close Camera")
		btn_open_cam.command=close_cam

	btn_open_cam.configure(command=attendance, text="Open Camera")
	btn_open_cam.command=attendance


	


	root.mainloop()



















# Login Page GUI



global main_frame    
global username_verify
global password_verify
username_verify=StringVar()
password_verify=StringVar()
main_frame=Frame(root,width=550,height=250, bd="2", highlightbackground="black", highlightthickness="1" )
main_frame.place(x=80, y=210)
Label(main_frame,text="Login to Continue", bg="blue",  width=49,height=2, font=("Helvetica", 15)).place(x=0, y=0)
global user_entry
global pass_entry
Label(main_frame, text="Username :", font=("calibri",13)).place(x=0, y=70)
user_entry=Entry(main_frame, textvariable=username_verify, width=38, selectborderwidth=4,bd=3,font=("calibri",13))
user_entry.place(x=110, y=72)
Label(main_frame, text="Password :",font=("calibri",13)).place(x=0, y=120)
pass_entry=Entry(main_frame, textvariable=password_verify, show="*",width=38, selectborderwidth=4,bd=3,font=("calibri",13))
pass_entry.place(x=110, y=122)
Button(main_frame, text="Login", width=40, height=1, fg="white", command=login, bg="#008000", font=('calibri', 13, 'bold'),activebackground="#006600",activeforeground="#e6ffe6").place(x=20, y=175)
Label(root,text="Developed By: K.K. Jha",  width="53",height="2", font=("Helvetica", 13)).place(x=330, y=600)


root.mainloop()




from tkinter import *
from tkinter import messagebox
from database import connection as cn
import tkinter.ttk as ttk 
import tkinter as tk
import attendance as att
import datetime
import time as tm

def add_account_screen():
    global add_screen
    add_screen= Tk()
    #add_screen = Tk()

    #photo = PhotoImage(file = "bg.gif")
    
    add_screen.geometry("1100x640")
    add_screen.title("")
    # background_image1 =PhotoImage(file = 'bg.gif')
    # bg_home_frame = PhotoImage(file = 'images/bg_home_frame.gif')
    # # Label widget is used to display text or image on screen
    # background_label =Label(add_screen, image = background_image1)
    #background_label.image = background_image
    # background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        
    global add_people_frame
    add_people_frame=Frame(add_screen,width=380,height=510, bd="2", highlightbackground="black", highlightthickness="1" )
    add_people_frame.place(x=10, y=90)
    global nm
    nm = StringVar()
    global fnm
    fnm = StringVar()
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
    role_lbl=Label(add_people_frame, text="Roll No. ").place(x=5,y=160)
    role_entry=Entry(add_people_frame, textvariable=role, width="26").place(x=150,y=160)
    sem_lbl=Label(add_people_frame, text="Semester ").place(x=5,y=190)
    sem_entry=Entry(add_people_frame, textvariable=sem, width="26").place(x=150,y=190)
    #dob_lbl=Label(add_people_frame, text="Date of Birth ").place(x=5,y=180)
    #dob_date=Entry(add_people_frame, textvariable="dob").place(x=150,y=180)
    mob_lbl=Label(add_people_frame, text="Mobile No. ").place(x=5,y=220)
    mob_entry=Entry(add_people_frame, textvariable=mob, width="26").place(x=150,y=220)
    email_lbl=Label(add_people_frame, text="Email Id ").place(x=5,y=250)
    email_entry=Entry(add_people_frame, textvariable=email, width="26").place(x=150,y=250)
    add_btn=Button(add_people_frame, text="Add Student", width="26", fg="white", bg="#008000",activebackground="#006600",activeforeground="#e6ffe6").place(x=70, y=280)

    #view Student frame
    global view_frame
    view_frame=Frame(add_screen,width=690,height=300, bd="2", highlightbackground="black", highlightthickness="1" )
    view_frame.place(x=400, y=90)
    Label(view_frame, text="Inrolled Students").place(x=300, y=0)
    tree=ttk.Treeview(view_frame, height=12)

    vsb = ttk.Scrollbar(view_frame, orient="vertical", command=tree.yview)
    vsb.place(x=30+630+2, y=22, height=240+20)
    tree.configure(yscrollcommand=vsb.set)



    tree["columns"]=("on","one","two","three", "four", "five", "six")
    tree.column("#0", width=0, minwidth=0, stretch=tk.NO)
    tree.column("on", width=150, minwidth=270,  stretch=tk.NO)
    tree.column("one", width=50, minwidth=100, stretch=tk.NO)
    tree.column("two", width=50, minwidth=50, anchor="center",)
    tree.column("three", width=100, minwidth=80, stretch=tk.NO)
    tree.column("four", width=60, minwidth=40,stretch=tk.NO)
    tree.column("five", width=70, minwidth=40,stretch=tk.NO)
    tree.column("six", width=178, minwidth=150,stretch=tk.NO)
    #tree.heading("#0",text="Name",anchor=tk.W)
    tree.heading("on",text="Name",anchor=tk.W)
    tree.heading("one", text="Face Id",anchor=tk.W)
    tree.heading("two", text="Roll No",anchor=tk.W)
    tree.heading("three", text="Department",anchor=tk.W)
    tree.heading("four", text="Semester",anchor=tk.W)
    tree.heading("five", text="Mobile",anchor=tk.W)
    tree.heading("six", text="Email",anchor=tk.W)

    global manage_dept_frame
    manage_dpt_frame=Frame(add_screen,width=690,height=200, bd="2", highlightbackground="black", highlightthickness="1" )
    manage_dpt_frame.place(x=400, y=400)



    add_screen.mainloop()
add_account_screen()
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
ws=Tk()
ws.geometry('1350x680+0+0')
ws.title('R E P O R T')
ws.resizable(0,0)
ws.configure(bg='white')

#label title
l1=Label(ws,text='ATTENDANCE REPORT',bg='black',fg='gold')
l=('consols',22)  #font,textsize
l1.config(font=l)
l1.place(x=0,y=125,width=1350,height=35)

image1=Image.open("Tittles.jpg")
image1=image1.resize((1350,120),Image.ANTIALIAS)
image2=ImageTk.PhotoImage(image1)
label1=Label(image=image2,border=0,justify=CENTER)
label1.place(x=0,y=0)


#left frame
left_frame=LabelFrame(ws,width=550,height=490,bg='white',fg="black",text="ATTENDANCE REPORT",relief=RIDGE).place(x=10,y=180)

imageemp=Image.open("title.jpg")
image3=imageemp.resize((800,100),Image.ANTIALIAS)
image3=ImageTk.PhotoImage(imageemp)
label2=Label(left_frame,image=image3,border=0,justify=CENTER)
label2.place(x=60,y=200)

l2=Label(left_frame,text='Employee ID',bg='white',)
l=('consols',9)  #font,textsiz
l2.config(font=l)
l2.place(x=30,y=340)

e1=Entry(left_frame,width=30,border=2)
e1.config(font=l)
e1.place(x=150,y=340)


l3=Label(left_frame,text='Employee Name',bg='white',)
l=('consols',9)  #font,textsiz
l3.config(font=l)
l3.place(x=30,y=370)

e2=Entry(left_frame,width=30,border=2)
e2.config(font=l)
e2.place(x=150,y=370)


l4=Label(left_frame,text='Department',bg='white',)
l=('consols',9)  #font,textsiz
l4.config(font=l)
l4.place(x=30,y=400)

e3=Entry(left_frame,width=30,border=2)
e3.config(font=l)
e3.place(x=150,y=400)


l5=Label(left_frame,text='Destination',bg='white',)
l=('consols',9)  #font,textsiz
l5.config(font=l)
l5.place(x=30,y=430)

e4=Entry(left_frame,width=30,border=2)
e4.config(font=l)
e4.place(x=150,y=430)

l6=Label(left_frame,text='Time',bg='white',)
l=('consols',9)  #font,textsiz
l6.config(font=l)
l6.place(x=30,y=460)

e5=Entry(left_frame,width=30,border=2)
e5.config(font=l)
e5.place(x=150,y=460)

l7=Label(left_frame,text='Date',bg='white',)
l=('consols',9)  #font,textsiz
l7.config(font=l)
l7.place(x=30,y=490)

e6=Entry(left_frame,width=30,border=2)
e6.config(font=l)
e6.place(x=150,y=490)



l6=Label(left_frame,text='Status',bg='white')
l=('consols',9)  #font,textsiz
l6.config(font=l)
l6.place(x=30,y=520)

dep_combo=ttk.Combobox(left_frame,font=("times new roman",12,"bold"),width=17)
dep_combo['values']=("Status","Present","Absent")
dep_combo.current(0)
dep_combo.grid(row=0,column=1,padx=150,pady=520)

def back():
    ws.destroy()
    import main


#--------------------------------

right_frame=LabelFrame(ws,width=770,height=490,bg='white',fg="black",text="ATTENDANCE VIEW",relief=RIDGE).place(x=570,y=180)


table_frame=Frame(ws,bd=2,bg="white",relief=RIDGE)
table_frame.place(width=750,height=450,x=580,y=210)

scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

ws.student_table=ttk.Treeview(table_frame,column=("id","dep","dest","name","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=ws.student_table.xview)
scroll_y.config(command=ws.student_table.yview)

############
ws.student_table.column("id",width=100,minwidth=100)
ws.student_table.column("dep",width=100,minwidth=100)
ws.student_table.column("dest",width=100,minwidth=100)
ws.student_table.column("name",width=150,minwidth=150)
ws.student_table.column("time",width=100,minwidth=100)
ws.student_table.column("date",width=100,minwidth=100)
ws.student_table.column("attendance",width=100,minwidth=100)

#############



ws.student_table.heading("id",text='Emp Id')
ws.student_table.heading("dep",text="Department")
ws.student_table.heading("dest",text="Destination")
ws.student_table.heading("name",text="Emp Name")
ws.student_table.heading("time",text="Time")
ws.student_table.heading("date",text="Date")
ws.student_table.heading("attendance",text="Attendance")
ws.student_table["show"]="headings"

ws.student_table.pack(fill=BOTH,expand=1)
ws.student_table.bind("<ButtonRelease>")

#---------------fetch data-----------------------------

def fetch_data(rows):
    ws.student_table.delete(*ws.student_table.get_children())
    for i in rows:
        ws.student_table.insert("",END,values=i)

def importcsv():
    global mydata
    fln=filedialog.askopenfilename(initialdir="C:\\Users\\Sabari\\Desktop\\Face reg Emp system\\Attendance")

    file=open(fln,'r')

    file.close()



#------------------------------------------------------
Button(left_frame,width=10,height=1,fg="white",bg="grey",border=0,text="Import CSV",command=importcsv).place(x=40,y=610)

Button(left_frame,width=10,height=1,fg="white",bg="grey",border=0,text="Export CSV").place(x=130,y=610)

Button(left_frame,width=10,height=1,fg="white",bg="grey",border=0,text="Update").place(x=230,y=610)

Button(left_frame,width=10,height=1,fg="white",bg="grey",border=0,text="Delete",command=back).place(x=320,y=610)



ws.mainloop()
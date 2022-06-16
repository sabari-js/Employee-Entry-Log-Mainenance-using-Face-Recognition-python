from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
import cv2

class Registration:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x680+0+0')
        self.root.title('R E G I S T R A T I O N')
        self.root.resizable(0,0)
        self.root.configure(bg='white')

        ############################################################
        #=========variable=============

        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_address=StringVar()
        self.var_dept=StringVar()
        self.var_dest=StringVar()
        self.var_doj=StringVar()
        self.var_contact=StringVar()
        self.var_salary=StringVar()

      #-------------------------Database---------------------------------
        conn=sqlite3.connect("faceRegemp.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS emptbl (id varchar PRIMARY KEY,name varchar,age varchar,address varchar,dept varchar,dest varchar,doj varchar,contact varchar,salary varchar)")
        conn.commit()
        conn.close

      #------------------------Fetch Data---------------------------------
        def fetch_data():
            conn=sqlite3.connect("faceRegemp.db")
            cur=conn.cursor()
            cur.execute("select * from emptbl")
            data=cur.fetchall()

            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()  

     #------------------------Add data---------------------------------------
        def add_data():
            if self.var_id.get()=="" or  self.var_name.get()=="" or  self.var_age.get()=="" or  self.var_address.get()=="" or  self.var_dept.get()=="" or  self.var_dest.get()=="" or  self.var_doj.get()=="" or  self.var_contact.get()=="" or  self.var_salary.get()=="":
                messagebox.showerror("Error","all fields are required")
            else:
                
                conn=sqlite3.connect("faceRegemp.db")
                cur=conn.cursor()
                cur.execute("insert into emptbl values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(self.var_id.get(),self.var_name.get(),self.var_age.get(),self.var_address.get(),self.var_dept.get(),self.var_dest.get(),self.var_doj.get(),self.var_contact.get(),self.var_salary.get()))
                

                
                conn.commit()
                lstid=cur.lastrowid + 1
                
                
                cur.close()
                fetch_data()
                messagebox.showinfo("SUCCESS","DATA INSERTED SUCCESSFULLY")
                reset_data()
                
                self.var_id.set(lstid)
            
                
                conn.close()
     #-----------------------------Get Cursor--------------------------------
        def get_cursor(event=""):
            cursor_focus=self.student_table.focus()
            content=self.student_table.item(cursor_focus)
            data=content["values"]

            self.var_id.set(data[0]),
            self.var_name.set(data[1]),
            self.var_age.set(data[2]),
            self.var_address.set(data[3]),
            self.var_dept.set(data[4]),
            self.var_dest.set(data[5]),
            self.var_doj.set(data[6]),
            self.var_contact.set(data[7]),
            self.var_salary.set(data[8])
     #------------------------------- UPDATE -----------------------------------
        def update_data():
            if self.var_id.get()=="" or  self.var_name.get()=="" or  self.var_age.get()=="" or  self.var_address.get()=="" or  self.var_dept.get()=="" or  self.var_dest.get()=="" or  self.var_doj.get()=="" or  self.var_contact.get()=="" or  self.var_salary.get()=="":
                messagebox.showerror("Error","all fields are required")
            else:
                try:
                    Update=messagebox.askyesno("update","do you want to update this details")
                    if Update>0:
                        conn=sqlite3.connect("faceRegemp.db")
                        cur=conn.cursor()
                        cur.execute("update emptbl set name=?,age=?,address=?,dept=?,dest=?,doj=?,contact=?,salary=? where id=?",(

                                                                                                                self.var_name.get(),
                                                                                                                self.var_age.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_dept.get(),
                                                                                                                self.var_dest.get(),
                                                                                                                self.var_doj.get(),
                                                                                                                self.var_contact.get(),
                                                                                                                self.var_salary.get(),
                                                                                                                self.var_id.get()
                                                                                                                ))
                                                                                                                
                    else:
                        if not Update:
                            return
                    messagebox.showinfo("success","data updated")        
                    cur.close()
                    conn.commit()
                    fetch_data()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("error",f"due to:{str(es)}") 
     #----------------------------
        def delete_data():
            if self.var_id.get()=="":
                messagebox.showerror("Error","Employee Id must be Required")
            else: 
                
                    delete=messagebox.askyesno("Delete page","Do you want to delete this Employee")
                    if delete>0:
                        conn=sqlite3.connect("faceRegemp.db")
                        cur=conn.cursor()
                        cur.execute("delete from emptbl where id=?",(self.var_id.get()))
                        
                        
                    else:
                        if not delete:
                            return
                    cur.close()
                    conn.commit()
                    fetch_data()
                    conn.close()        
                    messagebox.showinfo("Delete","successfilly deleted")

    #---------------------------Reset---------------------------------------

        def reset_data():
            self.var_id.set("")
            self.var_name.set("") 
            self.var_age.set("") 
            self.var_address.set("") 
            self.var_dept.set("") 
            self.var_dest.set("")
            self.var_doj.set("")
            self.var_contact.set("")  
            self.var_salary.set("")
    #-----------------------------------------------------------------------------
        
            


            



    #---------------------------------
        def generate_dataset():
            if self.var_id.get()=="" or  self.var_name.get()=="" or  self.var_age.get()=="" or  self.var_address.get()=="" or  self.var_dept.get()=="" or  self.var_dest.get()=="" or  self.var_doj.get()=="" or  self.var_contact.get()=="" or  self.var_salary.get()=="":
                messagebox.showerror("Error","all fields are required")
            else:
                try:
                    conn=sqlite3.connect("faceRegemp.db")
                    cur=conn.cursor()
                    cur.execute("select * from emptbl")
                    myresult=cur.fetchall()
                    id=0
                    for x in myresult:
                        id+=1
                    cur.execute("update emptbl set name=?,age=?,address=?,dept=?,dest=?,doj=?,contact=?,salary=? where id=?",(

                                                                                                                self.var_name.get(),
                                                                                                                self.var_age.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_dept.get(),
                                                                                                                self.var_dest.get(),
                                                                                                                self.var_doj.get(),
                                                                                                                self.var_contact.get(),
                                                                                                                self.var_salary.get(),
                                                                                                                self.var_id.get()
                                                                                                                )) 
                    conn.commit()
                    fetch_data()
                    reset_data()
                    conn.close()
                # =================    load predefined data on face frontals=============

                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1
                        #minimum neighbour=5

                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped

                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("cropped face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==50:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generated data sets completed") 
                except Exception as es:
                    messagebox.showerror("error",f"due to:{str(es)}")


    #---------------------------------        

        #Title & Background

        image1=Image.open("Tittles.jpg")
        image1=image1.resize((1350,120),Image.ANTIALIAS)
        self.image2=ImageTk.PhotoImage(image1)
        label1=Label(self.root,image=self.image2,border=0,justify=CENTER)
        label1.place(x=0,y=0) 
        
        

        l1=Label(self.root,text='EMPLOYEE REGISTERATION',bg='black',fg='gold')
        l=('consols',22)  #font,textsize
        l1.config(font=l)
        l1.place(x=0,y=125,width=1350,height=35)

        #left frame design

        left_frame=LabelFrame(self.root,width=550,height=490,bg='white',fg="black",text="EMPLOYEE DETAILS",relief=RIDGE).place(x=10,y=180)

        imageemp=Image.open("title.jpg")
        image3=imageemp.resize((800,100),Image.ANTIALIAS)
        self.image3=ImageTk.PhotoImage(imageemp)
        label2=Label(self.root,left_frame,image=self.image3,border=0,justify=CENTER)
        label2.place(x=60,y=200)
        
        l2=Label(self.root,left_frame,text='Employee ID',bg='white',)
        l=('consols',9)  #font,textsiz
        l2.config(font=l)
        l2.place(x=30,y=340)

        e1=Entry(self.root,left_frame,width=40,border=2,textvariable=self.var_id)
        e1.config(font=l)
        e1.place(x=150,y=340)
##############
        l3=Label(self.root,left_frame,text='Employee Name',bg='white')
        l=('consols',9)  #font,textsiz
        l3.config(font=l)
        l3.place(x=30,y=370)

        e2=Entry(self.root,left_frame,width=40,border=2,textvariable=self.var_name)
        e2.config(font=l)
        e2.place(x=150,y=370)
###############
        l4=Label(self.root,left_frame,text='Age',bg='white')
        l=('consols',9)  #font,textsiz
        l4.config(font=l)
        l4.place(x=30,y=410)

        e3=Entry(self.root,left_frame,width=40,border=2,textvariable=self.var_age)
        e3.config(font=l)
        e3.place(x=150,y=410)
################
        l5=Label(self.root,left_frame,text='Address',bg='white')
        l=('consols',9)  #font,textsiz
        l5.config(font=l)
        l5.place(x=30,y=450)

        e4=Entry(self.root,left_frame,width=40,border=2,textvariable=self.var_address)
        e4.config(font=l)
        e4.place(x=150,y=450)
##############
        l6=Label(self.root,left_frame,text='Department',bg='white')
        l=('consols',9)  #font,textsiz
        l6.config(font=l)
        l6.place(x=30,y=480)

        dep_combo=ttk.Combobox(self.root,font=("times new roman",12,"bold"),width=17,textvariable=self.var_dept)
        dep_combo['values']=("Select Department","Administration","Product","Sales","Packing")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=150,pady=480)
###############
        l7=Label(self.root,left_frame,text='Designation',bg='white')
        l=('consols',9)  #font,textsiz
        l7.config(font=l)
        l7.place(x=30,y=510)

        e5=Entry(self.root,left_frame,width=40,border=2,textvariable=self.var_dest)
        e5.config(font=l)
        e5.place(x=150,y=510)
#################
        l8=Label(self.root,left_frame,text='DOJ',bg='white')
        l=('consols',9)  #font,textsiz
        l8.config(font=l)
        l8.place(x=30,y=540)

        e6=Entry(self.root,left_frame,width=40,border=2,textvariable=self.var_doj)
        e6.config(font=l)
        e6.place(x=150,y=540)
##################
        l9=Label(self.root,left_frame,text='Contact',bg='white')
        l=('consols',9)  #font,textsiz
        l9.config(font=l)
        l9.place(x=30,y=570)

        e7=Entry(self.root,left_frame,width=40,border=2,textvariable=self.var_contact)
        e7.config(font=l)
        e7.place(x=150,y=570)
##################
        l10=Label(self.root,left_frame,text='Salary / Month',bg='white')
        l=('consols',9)  #font,textsiz
        l10.config(font=l)
        l10.place(x=30,y=600)

        e8=Entry(self.root,left_frame,width=40,border=2,textvariable=self.var_salary)
        e8.config(font=l)
        e8.place(x=150,y=600)

#=====================Button================================

        Button(self.root,left_frame,width=10,height=1,fg="white",bg="grey",border=0,text="Save",command=add_data).place(x=20,y=640)

        Button(self.root,left_frame,width=10,height=1,fg="white",bg="grey",border=0,text="Update",command=update_data).place(x=110,y=640)

        Button(self.root,left_frame,width=10,height=1,fg="white",bg="grey",border=0,text="Delete",command=delete_data).place(x=200,y=640)

        Button(self.root,left_frame,width=10,height=1,fg="white",bg="grey",border=0,text="Reset",command=reset_data).place(x=290,y=640)

        Button(self.root,left_frame,width=18,height=1,fg="white",bg="grey",border=0,text="Take Sample Photo",command=generate_dataset).place(x=380,y=640)

        
        
#right frame

        #right_frame=LabelFrame(self.root,width=770,height=490,bg='white',fg="black",text="Over All Details",relief=RIDGE).place(x=570,y=180)

        table_frame=Frame(self.root,bd=2,bg="white",relief=RIDGE)
        table_frame.place(width=770,height=480,x=570,y=190)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("id","name","age","address","dep","dest","contact","doj","salary"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
############
        self.student_table.column("id",width=100,minwidth=100)
        self.student_table.column("name",width=150,minwidth=150)
        self.student_table.column("age",width=80,minwidth=80)
        self.student_table.column("address",width=150,minwidth=150)
        self.student_table.column("dep",width=100,minwidth=100)
        self.student_table.column("dest",width=100,minwidth=100)
        self.student_table.column("doj",width=100,minwidth=100)
        self.student_table.column("contact",width=100,minwidth=100)
        self.student_table.column("salary",width=100,minwidth=100)
#############



        self.student_table.heading("id",text='Emp Id')
        self.student_table.heading("name",text="Emp Name")
        self.student_table.heading("age",text="Age")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("dest",text="Designation")
        self.student_table.heading("doj",text="Dateofjoin")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("salary",text="Salary")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",get_cursor)
        fetch_data()

    

    





if __name__ == "__main__":
    root=Tk()
    obj=Registration(root)
    root.mainloop()
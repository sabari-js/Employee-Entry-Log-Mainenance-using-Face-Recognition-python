import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
import cv2
import numpy as np
from time import strftime
from datetime import datetime
import csv

class Recog:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x680+0+0')
        self.root.title('M E N U')
        self.root.resizable(0,0)


        #label title
        l1=Label(self.root,text='Face Regognition ',bg='black',fg='gold')
        l=('consols',22)  #font,textsize
        l1.config(font=l)
        l1.place(x=0,y=120,width=1350,height=36)

        image1=Image.open("Tittles.jpg")
        image1=image1.resize((1350,120),Image.ANTIALIAS)
        self.image2=ImageTk.PhotoImage(image1)
        label1=Label(self.root,image=self.image2,border=0,justify=CENTER)
        label1.place(x=0,y=0)

        imagebgs=Image.open("frsimg.jpg")
        imagebgs=imagebgs.resize((1350,525),Image.ANTIALIAS)
        self.image3=ImageTk.PhotoImage(imagebgs)
        label2=Label(self.root,image=self.image3,border=0,justify=CENTER)
        label2.place(x=0,y=155)

        #============mark attendance=====================
        def mark_attendance(i,r,n,d):
            dt_now=datetime.today()
            f_name=dt_now.strftime("%b-%d-%Y")
            open('Attendance/'+f_name+'.csv','a+')
            with open('Attendance/'+f_name+'.csv',"r+",newline="\n") as f:
                myDataList=f.readlines()
                name_list=[]
                for line in myDataList:
                    entry=line.split((","))
                    name_list.append(entry[0])
                if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ):
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

        #==========face recognition======================

        def face_recog():
            def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

                coord=[]

                for (x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))
                    
                    conn=sqlite3.connect("faceRegemp.db")
                    cur=conn.cursor()

                    cur.execute("select name from emptbl where id="+str(id))
                    n=cur.fetchone()
                    n="+".join(n)

                    cur.execute("select dept from emptbl where id="+str(id))
                    r=cur.fetchone()
                    r="+".join(r)

                    cur.execute("select dest from emptbl where id="+str(id))
                    d=cur.fetchone()
                    d="+".join(d)

                    cur.execute("select id from emptbl where id="+str(id))
                    i=cur.fetchone()
                    i="+".join(i)




                    if confidence>70:
                        cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Destination:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        mark_attendance(i,r,d,n)
                        
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,f"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    coord=[x,y,w,y]
                
                return coord        
            
            def recognize(img,clf,faceCasecade):
                coord=draw_boundry(img,faceCasecade,1.1,10,(255,25,255),"Face",clf)
                return img


            faceCasecade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")


            video_cap=cv2.VideoCapture(0)


            while True:
                ret,img=video_cap.read()
                img=recognize(img,clf,faceCasecade)
                cv2.imshow("Welcome to face recognition",img)


                if cv2.waitKey(1)==13:
                    break
            video_cap.release()
            cv2.destroyAllWindows()

        
        #================================================
        Button(self.root,width=14,height=1,fg="white",bg="green",border=2,text="RECOGNIZE DATA",justify=CENTER,command=face_recog).place(x=610,y=620)



if __name__ == "__main__":
    root=Tk()
    obj=Recog(root)
    root.mainloop()
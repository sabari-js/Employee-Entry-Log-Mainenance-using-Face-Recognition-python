from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import os
from register import Registration
from train import Train_Dataset
from face_recognition import Recog

class Face_Recog_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x680+0+0')
        self.root.title('M E N U')
        self.root.resizable(0,0)
        


#label title
        l1=Label(self.root,text='EMPLOYEE ENTRY LOG MAINTANANCE',bg='black',fg='gold')
        l=('consols',22)  #font,textsize
        l1.config(font=l)
        l1.place(x=0,y=125,width=1350,height=35)

        image1=Image.open("Tittles.jpg")
        image1=image1.resize((1350,120),Image.ANTIALIAS)
        self.image2=ImageTk.PhotoImage(image1)

        label1=Label(image=self.image2,border=0,justify=CENTER)
        label1.place(x=0,y=0)
#
        l2=Label(self.root,text='MENU',bg='black',fg='gold')
        l=('consols',22)  #font,textsize
        l2.config(font=l)
        l2.place(x=0,y=165,width=260,height=70)

##
        imagebg=Image.open("BGS.jpg")
        imagebg=imagebg.resize((1090,515),Image.ANTIALIAS)
        self.imagebg=ImageTk.PhotoImage(imagebg)
        
        label1=Label(image=self.imagebg,border=0,justify=CENTER)
        label1.place(x=260,y=165)

    
    


        regbut=Button(self.root,width=36,height=5,fg="white",bg="black",border=0,text="REGISTRATION",command=self.reg).place(x=0,y=240)

        shout=Button(self.root,width=36,height=5,fg="white",bg="black",border=0,text="SHOW DATASET",command=self.show_pic).place(x=0,y=330)

        trainbut=Button(self.root,width=36,height=5,fg="white",bg="black",border=0,text="TRAIN DATA",command=self.train).place(x=0,y=420)

        facebut=Button(self.root,width=36,height=5,fg="white",bg="black",border=0,text="FACE REGONIZATION",command=self.fc_recog).place(x=0,y=510)
        
        exbut=Button(self.root,width=36,height=5,fg="white",bg="black",border=0,text="EXIT",command=self.exit).place(x=0,y=605)  

    


    
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Registration(self.new_window)

    def show_pic(self):
           os.startfile("data")        
    
    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_Dataset(self.new_window)
    
    def fc_recog(self):
        self.new_window=Toplevel(self.root)
        self.app=Recog(self.new_window)
    
    def exit(self):
        root.destroy()        


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recog_System(root)
    root.mainloop()





import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
import cv2
import numpy as np

class Train_Dataset:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x680+0+0')
        self.root.title('M E N U')
        self.root.resizable(0,0)


#label title
        l1=Label(self.root,text='TRAIN DATA',bg='black',fg='gold')
        l=('consols',22)  #font,textsize
        l1.config(font=l)
        l1.place(x=0,y=125,width=1350,height=35)

        image1=Image.open("Tittles.jpg")
        image1=image1.resize((1350,120),Image.ANTIALIAS)
        self.image2=ImageTk.PhotoImage(image1)
        label1=Label(self.root,image=self.image2,border=0,justify=CENTER)
        label1.place(x=0,y=0)

        imagebgs=Image.open("TRAINBACK.jpg")
        imagebgs=imagebgs.resize((1350,510),Image.ANTIALIAS)
        self.image3=ImageTk.PhotoImage(imagebgs)
        label2=Label(self.root,image=self.image3,border=0,justify=CENTER)
        label2.place(x=0,y=165)

        ####### function ##########
        def train_classifier():
            data_dir=("data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

            faces=[]
            ids=[]

            for image in path:
                img=Image.open(image).convert('L') # gray scale image
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)

        #==============train the classifier and save==============

            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training datasets completed")

        ###########################



        Button(self.root,width=15,height=3,fg="gold",bg="black",border=2,text="TRAIN",command=train_classifier).place(x=600,y=610)





if __name__ == "__main__":
    root=Tk()
    obj=Train_Dataset(root)
    root.mainloop()

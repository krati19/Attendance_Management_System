from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
import cv2
import numpy as np
from tkinter import messagebox

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")
        
        # header image  
        img=Image.open(r"images\header.jpg")
        img=img.resize((1530,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as label
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1535,height=130)

        # background image 
        bg1=Image.open(r"images\bg4.jpg")
        bg1=bg1.resize((1530,790),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1530,height=790)

        #title section
        title_lb1 = Label(bg_img,text="Train Your Dataset",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        # Training button 
        std_img_btn=Image.open(r"images\train.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=660,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="navyblue",fg="white")
        std_b1_1.place(x=660,y=350,width=180,height=45)

        #Back Button
        def prevPage():
            self.root.destroy()
            import main
        back_button= Button( bg_img, text="Home Page", font=("verdana",12,"bold"),command=prevPage,fg="navyblue",bg="white",bd=5)
        back_button.place(x=10,y=60,width=150,height=60)

# ==================Creating Function of Training===================
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # convert to grey scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)

# main class object
if __name__ == "__main__":
    root = Tk()
    obj =  Train(root)
    root.mainloop()



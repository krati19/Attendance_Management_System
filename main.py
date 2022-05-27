from tkinter import *
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
#from PIL import ImageFont,ImageDraw
from student import Student
import os
from train import Train
from recognition import Recognition
from attendance import Attendance

class Face_Recognition_System:
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
        
        # title section
        title_lb1 = Label(bg_img,text="Attendance Managment System",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        # Student Pannel button 
        std_img_btn=Image.open(r"images\student.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=420,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student Pannel",cursor="hand2",font=("tahoma",15,"bold"),bg="navyblue",fg="white")
        std_b1_1.place(x=420,y=280,width=180,height=45)

       # Face Detection button 
        det_img_btn=Image.open(r"images\detect.png")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=643,y=100,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="navyblue",fg="white")
        det_b1_1.place(x=643,y=280,width=180,height=45)

        # Attendance Pannel button 
        att_img_btn=Image.open(r"images\att.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=867,y=100,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="navyblue",fg="white")
        att_b1_1.place(x=867,y=280,width=180,height=45)

        # Train button 
        tra_img_btn=Image.open(r"images\train.jpg")
        tra_img_btn=tra_img_btn.resize((180,180),Image.ANTIALIAS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=420,y=350,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Train Data",cursor="hand2",font=("tahoma",15,"bold"),bg="navyblue",fg="white")
        tra_b1_1.place(x=420,y=530,width=180,height=45)

        # Photos button 
        pho_img_btn=Image.open(r"images\dataset.jpg")
        pho_img_btn=pho_img_btn.resize((180,180),Image.ANTIALIAS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,image=self.pho_img1,cursor="hand2",command=self.open_img)
        pho_b1.place(x=645,y=350,width=180,height=180)

        pho_b1_1 = Button(bg_img,text="Pictures",command=self.open_img,cursor="hand2",font=("tahoma",15,"bold"),bg="navyblue",fg="white")
        pho_b1_1.place(x=645,y=530,width=180,height=45)

        # Exit button 
        exi_img_btn=Image.open(r"images\exit.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,image=self.exi_img1,cursor="hand2",command=self.exit)
        exi_b1.place(x=870,y=350,width=180,height=180)

        exi_b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("tahoma",15,"bold"),bg="navyblue",fg="white")
        exi_b1_1.place(x=870,y=530,width=180,height=45)

    # ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data")
        
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Attendance System","Are you sure",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return

    # ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Recognition(self.new_window)
        
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def Close(self):
        root.destroy()

# main class object
if __name__ == "__main__":
    root = Tk()
    obj =  Face_Recognition_System(root)
    root.mainloop()


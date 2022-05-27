import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

#Global variable for importCsv Function 
mydata=[]

class Attendance:
    
    def __init__(self,root):
        self.root=root
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
        title_lb1 = Label(bg_img,text="Attendance Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        #Label Frame 
        #main_frame = LabelFrame(bg_img,bd=5,bg="white",relief=RIDGE,text="Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        #main_frame.place(x=400,y=90,width=780,height=500)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=430,y=80,width=700,height=560)

        # Inside main frame
        table_frame = LabelFrame(main_frame,bd=5,bg="white",text="Attendance Details",font=("verdana",12,"bold"),relief=RIDGE,fg="navyblue")
        table_frame.place(x=10,y=10,width=675,height=530)

        #Scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #Creating table 
        self.attendanceReport_left = ttk.Treeview(table_frame,column=("ID","Roll_No","Name","Time","Date","Attendance-Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport_left.xview)
        scroll_y.config(command=self.attendanceReport_left.yview)

        self.attendanceReport_left.heading("ID",text="Student-ID")
        self.attendanceReport_left.heading("Roll_No",text="Roll_No")
        self.attendanceReport_left.heading("Name",text="Student-Name")
        self.attendanceReport_left.heading("Time",text="Time")
        self.attendanceReport_left.heading("Date",text="Date")
        self.attendanceReport_left.heading("Attendance-Status",text="Attendance-Status")
        self.attendanceReport_left["show"]="headings"

         # Set Width of Columns 
        self.attendanceReport_left.column("ID",width=150)
        self.attendanceReport_left.column("Roll_No",width=150)
        self.attendanceReport_left.column("Name",width=150)
        self.attendanceReport_left.column("Time",width=150)
        self.attendanceReport_left.column("Date",width=150)
        self.attendanceReport_left.column("Attendance-Status",width=150)
        
        self.attendanceReport_left.pack(fill=BOTH,expand=1)

        #Button Frame
        btn_frame = Frame(table_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=170,y=420,width=315,height=55)

        #Import button
        save_btn=Button(btn_frame,command=self.importCsv,text="Import CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Export button
        update_btn=Button(btn_frame,command=self.exportCsv,text="Export CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

    # =========================Fetch Data Import data ===============
    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            print(i)
        
    #==================Import CSV=============
    def importCsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
            
#==================Export CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

# main class object
if __name__ == "__main__":
    root = Tk()
    obj =  Attendance(root)
    root.mainloop()


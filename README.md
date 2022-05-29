
# Attendance Management System Using Face Recognition

An attendance management system using state-of-the-art face 
detection and recognition algorithms. This system of attendance 
tracking helps alleviate major grievances in the present system 
such as unnecessary time consumption and proxies.

This project is made on Visual Studio Code using Python version 3.10.4

TECHNOLIGIES USED:

Tkinter for whole GUI

OpenCV for taking images and face recognition (cv2.face.LBPHFaceRecognizer_create())

CSV, Numpy, Pandas, datetime etc. for other purposes.

mysqlite for database

FEATURES:

1.)Easy to use with interactive GUI support.

2.)Creates/Updates database for details of students on registration.

3.)Recognises faces and marks attendance automatically.

4.)Shows name,id,date,time,attendance status after marking attendance.

RUN LOCALLY:

Make sure you have dlib, cmake and mysqlite database installed.

1.) Clone the repository 
    git clone https://github.com/krati19/Attendance_Management_System.git
    
2.) type pip install -r requirements.txt in command prompt
    (this will install required package for project)
    
3.) Create a 'data' folder in a project folder.

4.) Run main.py file

PROJECT FLOW AND EXPLAINATION:

1.) On running main.py the home page opens,which has six photo buttons.
    ![Screenshot (5)](https://user-images.githubusercontent.com/92323422/170815872-122fbbd6-4db9-439b-a33d-2dce7f7301e2.png)
2.) Clicking on the Student Pannel button, we go to the registration window where students can register themselves.
    ![Screenshot (7)](https://user-images.githubusercontent.com/92323422/170815876-a92fba60-2343-470d-9860-9b7a1ab48d55.png)
3.) Then we go to the train dataset button, where we train the pictures taken during the registration period.
    ![Screenshot (11)](https://user-images.githubusercontent.com/92323422/170815905-69d9dd7c-03a7-4160-a57c-810084810dd5.png)
4.) There is also a photos button which shows the picture dataset that has been created.

5.) Then we click on the face recogniton button, where clicking on the button the webcam opens and recognises the student's face and automatically marks the attendance.The webcam closes by clicking 'q' on the keyboard.
    ![Screenshot (13)](https://user-images.githubusercontent.com/92323422/170815915-acb11163-d1a9-4526-b8e3-68ced66cd5bf.png)
6.) Then there is the attendance button where we can see the attendance details and also import and export the CSV files that have been created to store the details.
    ![Screenshot (15)](https://user-images.githubusercontent.com/92323422/170815920-ece90e94-9a1b-4bcd-924e-2a7f0bbb38f6.png)
7.) Lastly there is the exit button, which helps us to exit the system.

This is how the mysqlite database of this project looks like:
    ![Screenshot (9)](https://user-images.githubusercontent.com/92323422/170815926-fabb73cf-b504-472d-8655-ef9a86c5ebe7.png)

AUTHOR:
KRATI SHARMA

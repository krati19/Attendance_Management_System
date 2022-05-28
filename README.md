
# Attendance Management System Using Face Recognition

An attendance management system using state-of-the-art face 
detection and recognition algorithms. This system of attendance 
tracking helps alleviate major grievances in the present system 
such as unnecessary time consumption and proxies.

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
3.) Create a data folder in a project folder.
4.) Run main.py file

PROJECT FLOW AND EXPLAINATION:

1.) On running main.py the home page opens,which has six photo buttons.
    Screenshot (5).png
2.) Clicking on the Student Pannel button, we go to the registration window where students can register themselves.
    Screenshot (7).png
3.) Then we go to the train dataset button, where we train the pictures taken during the registration period.
    Screenshot (11).png
4.) There is also a photos button which shows the picture dataset that has been created.
5.) Then we click on the face recogniton button, where clicking on the button the webcam opens and recognises the student's face and automatically marks the attendance.The webcam closes by clicking 'q' on the keyboard.
    Screenshot (13).png
6.) Then there is the attendance button where we can see the attendance details and also import and export the CSV files that have been created to store the details.
    Screenshot (15).png
7.) Lastly there is the exit button, which helps us to exit the system.

SCREENSHOTS:

This is how the mysqlite database of this project looks like:
    Screenshot (9).png

AUTHOR:
KRATI SHARMA
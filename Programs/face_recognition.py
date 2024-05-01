from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION")
        self.root.wm_iconbitmap(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\face_detector.ico")

        
        self.var_teacher=StringVar()
        self.var_course=StringVar()
        
        title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="light green",fg="red")
        title_lbl.place(x=0,y=0,width=1550,height=45)
        
        # Left side with combo boxes
        left_frame = Frame(self.root, bg="white")
        left_frame.place(x=0, y=50, width=773, height=700)

        teacher_label = Label(left_frame, text="Teacher Name:", font=("times new roman", 20), bg="white")
        teacher_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        teacher_combo = ttk.Combobox(left_frame,textvariable=self.var_teacher, font=("times new roman", 15), state="readonly")
        teacher_combo["values"] = ["Select Teacher Name","Teacher 1", "Teacher 2", "Teacher 3"]
        teacher_combo.current(0)
        teacher_combo.grid(row=0, column=1, padx=20, pady=10)

        course_label = Label(left_frame, text="Course Name:", font=("times new roman", 20), bg="white")
        course_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        course_combo = ttk.Combobox(left_frame,textvariable=self.var_course, font=("times new roman", 15), state="readonly")
        course_combo["values"] = ["Select Course","Course 1", "Course 2", "Course 3"]
        course_combo.current(0)
        course_combo.grid(row=1, column=1, padx=20, pady=10)
        
        # Right side with the DETECT button and background image
        right_frame = Frame(self.root)
        right_frame.place(x=775, y=50, width=773, height=700)

        right_bg_img = Image.open(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\face_recog_bg2.jpg")
        right_bg_img = right_bg_img.resize((700, 750))
        self.right_bg_img = ImageTk.PhotoImage(right_bg_img)

        right_bg_lbl = Label(right_frame, image=self.right_bg_img)
        right_bg_lbl.pack(fill="both", expand=True)

        recognition_btn = Button(right_frame, command=self.recognition,text="DETECT", font=("times new roman", 25, "bold"), bg="green", fg="white", cursor="hand2")
        recognition_btn.place(relx=0.5, rely=0.85, anchor="center")
        
        
        
    # ==============Attendance=================

    def mark_attendance(self, r, n, b):
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        file_path = f"D:\\PROJECT\\FACE RECOGNITION ATTENDANCE SYSTEM\\College-Project\\Programs\\attendance_{date_str}.csv"
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="\n") as f:
                f.write("Roll Number,Name,Branch,Teacher,Course,Time,Date,Status\n")

        # Check if the student's data is already present in the file for the current teacher
        with open(file_path, "r", newline="\n") as f:
            myDataList = f.readlines()
            for line in myDataList:
                entry = line.split(",")
                if entry[0] == r and entry[1] == n and entry[2] == b and entry[3] == self.var_teacher.get():
                    # Student's data is already present for the current teacher, do not add a new attendance record
                    return

        # Write to the CSV file
        with open(file_path, "a", newline="\n") as f:
            f.write(f"{r},{n},{b},{self.var_teacher.get()},{self.var_course.get()},{now.strftime('%H:%M:%S')},{now.strftime('%d/%m/%Y')},present\n")


                
        
    
    
    # ===========Face recognition===========
    def recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbour)
            
            coord = []
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_img[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict / 300))
                
                conn = mysql.connector.connect(host="localhost", username="root", password="Rakesh@347", database="face_recognition")
                my_cursor = conn.cursor()
                
                my_cursor.execute("SELECT s_name FROM student WHERE roll_no = " + f"\'{str(id)}\'")
                n_row = my_cursor.fetchone()
                if n_row:
                    n = "+".join(n_row)
                else:
                    n = "Unknown"
                
                my_cursor.execute("SELECT roll_no FROM student WHERE roll_no = " + f"\'{str(id)}\'")
                r_row = my_cursor.fetchone()
                if r_row:
                    r = "+".join(r_row)
                else:
                    r = "Unknown"
                
                my_cursor.execute("SELECT branch FROM student WHERE roll_no = " + f"\'{str(id)}\'")
                b_row = my_cursor.fetchone()
                if b_row:
                    b = "+".join(b_row)
                else:
                    b = "Unknown"
                
                if confidence > 87:
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Branch: {b}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(r,n,b)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    
                coord = [x, y, w, h]
                
            return coord

        
        def recog(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\Programs\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\Programs\classifier.xml")
        
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recog(img,clf,faceCascade)
            cv2.imshow("Welcome To face recognition",img)
            
            if cv2.waitKey(1)==13 or cv2.getWindowProperty("Welcome To face recognition", cv2.WND_PROP_VISIBLE) < 1:
                break
        video_cap.release()
        cv2.destroyAllWindows()
            
        

        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
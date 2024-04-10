from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION")
        
        
        title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="light green",fg="red")
        title_lbl.place(x=0,y=0,width=1550,height=45)
        
        
        #bg image1
        img1=Image.open(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\face_recog_bg2.jpg")
        img1=img1.resize((1550,800))
        self.bg_img1=ImageTk.PhotoImage(img1)
        
        bg_img_lbl1=Label(self.root,image=self.bg_img1)
        bg_img_lbl1.place(x=0,y=45,width=515,height=800)
        
        
        #bg image2
        img2=Image.open(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\face_recog_bg2.jpg")
        img2=img2.resize((1550,800))
        self.bg_img2=ImageTk.PhotoImage(img2)
        
        bg_img_lbl2=Label(self.root,image=self.bg_img2)
        bg_img_lbl2.place(x=515,y=45,width=515,height=800)
        
        #bg image3
        img3=Image.open(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\face_recog_bg2.jpg")
        img3=img3.resize((1550,800))
        self.bg_img3=ImageTk.PhotoImage(img3)
        
        bg_img_lbl3=Label(self.root,image=self.bg_img3)
        bg_img_lbl3.place(x=1030,y=45,width=520,height=800)
        
        
        recognition_btn=Button(bg_img_lbl2,command=self.recognition,text="DETECT",cursor="hand2",font=("times new roman",25,"bold"),bg="green",fg="white")
        recognition_btn.place(x=64,y=625,width=387,height=60)
        
    
    
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
                
                my_cursor.execute("SELECT s_name FROM student WHERE s_id = " + f"\'{str(id)}\'")
                n_row = my_cursor.fetchone()
                if n_row:
                    n = "+".join(n_row)
                else:
                    n = "Unknown"
                
                my_cursor.execute("SELECT roll_no FROM student WHERE s_id = " + f"\'{str(id)}\'")
                r_row = my_cursor.fetchone()
                if r_row:
                    r = "+".join(r_row)
                else:
                    r = "Unknown"
                
                my_cursor.execute("SELECT branch FROM student WHERE s_id = " + f"\'{str(id)}\'")
                b_row = my_cursor.fetchone()
                if b_row:
                    b = "+".join(b_row)
                else:
                    b = "Unknown"
                
                if confidence > 80:
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Branch: {b}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
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
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
            
        

        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
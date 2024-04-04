from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")
        
        
        #College name photo
        img1=Image.open(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\College name.png")
        img1=img1.resize((1550,130))
        self.Clg_img=ImageTk.PhotoImage(img1)
        
        lbl1=Label(self.root,image=self.Clg_img)
        lbl1.place(x=0,y=0,width=1550,height=130)
        
        
        #bg image
        img2=Image.open(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\student_bg.jpg")
        img2=img2.resize((1550,715))
        self.bg_img=ImageTk.PhotoImage(img2)
        
        bg_img_lbl=Label(self.root,image=self.bg_img)
        bg_img_lbl.place(x=0,y=130,width=1550,height=715)
        
        title_btn=Button(bg_img_lbl,command=self.train_classifier,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="light green",fg="blue")
        title_btn.place(x=0,y=0,width=1550,height=45)
        
        
    def train_classifier(self):
        data_dir=(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\Student pictures")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')
            img_arr=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(img_arr)
            ids.append(id)
            cv2.imshow("Training",img_arr)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        # ==================Train the Classifier and Save=====================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed")
        
if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
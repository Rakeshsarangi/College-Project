from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")
        self.root.configure(bg="blue")
        
        
        #College name photo
        img1=Image.open(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\College name.png")
        img1=img1.resize((1550,200))
        self.Clg_img=ImageTk.PhotoImage(img1)
        
        lbl1=Label(self.root,image=self.Clg_img)
        lbl1.place(x=0,y=0,width=1550,height=200)
        
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="light green",fg="red")
        title_lbl.place(x=0,y=200,width=1550,height=45)
        
        # Help Desk Button
        img6=Image.open(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\help_desk.jpeg")
        img6=img6.resize((220,220))
        self.help_desk_img=ImageTk.PhotoImage(img6)
        
        b4=Button(self.root,image=self.help_desk_img,cursor="hand2")
        b4.place(x=650,y=300,width=230,height=220)
        
        b4_1=Button(self.root,text="Email : demoemail@gmail.com",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b4_1.place(x=560,y=530,width=400,height=40)
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
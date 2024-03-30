from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")
        
        
        
        #College name photo
        img1=Image.open("D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\College name.png")
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
        
        title_lbl=Label(bg_img_lbl,text="STUDENT DETAILS",font=("times new roman",35,"bold"),bg="light green",fg="blue")
        title_lbl.place(x=0,y=0,width=1550,height=45)
        
        # Draw vertical line in the middle of bg_img_lbl
        canvas = tk.Canvas(bg_img_lbl, width=2, height=715, bg='Black', highlightthickness=1)
        canvas.create_line(775, 0, 775, 715, fill='black')
        canvas.place(x=774, y=45)
        
        
        curr_course_lbl=Label(bg_img_lbl,text="CURRENT COURSE INFORMATION",font=("times new roman",15,"bold"),bg="yellow",fg="blue")
        curr_course_lbl.place(x=0,y=45,width=775,height=40)
        
        
        #Branch selector
        branch_lbl=Label(bg_img_lbl,text="Branch : ",font=("times new roman",20,"bold"),fg="black",)
        branch_lbl.place(x=0,y=100,width=150,height=40)
        
        
        branch_combo= ttk.Combobox(bg_img_lbl,font=("times new roman",15),width=17,state="readonly")
        branch_combo["values"]=("Select Branch","MCA","CSc")
        branch_combo.current(0)
        branch_combo.place(x=150,y=100,width=150,height=40)
        
        
        #Year selector
        year_lbl=Label(bg_img_lbl,text="year : ",font=("times new roman",20,"bold"),fg="black",)
        year_lbl.place(x=0,y=170,width=150,height=40)
        
        
        year_combo= ttk.Combobox(bg_img_lbl,font=("times new roman",15),width=17,state="readonly")
        year_combo["values"]=("Select Year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.place(x=150,y=170,width=150,height=40)
        
        
        #Course selector
        course_lbl=Label(bg_img_lbl,text="Course : ",font=("times new roman",20,"bold"),fg="black",)
        course_lbl.place(x=350,y=100,width=150,height=40)
        
        
        course_combo= ttk.Combobox(bg_img_lbl,font=("times new roman",15),width=17,state="readonly")
        course_combo["values"]=("Select Course","C","C++","java","python")
        course_combo.current(0)
        course_combo.place(x=500,y=100,width=150,height=40)
        
        
        #Semester selector
        semester_lbl=Label(bg_img_lbl,text="Semester : ",font=("times new roman",20,"bold"),fg="black",)
        semester_lbl.place(x=350,y=170,width=150,height=40)
        
        
        semester_combo= ttk.Combobox(bg_img_lbl,font=("times new roman",15),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        semester_combo.current(0)
        semester_combo.place(x=500,y=170,width=150,height=40)
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
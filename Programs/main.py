from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")
        
        
        #College name photo
        img1=Image.open("D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\College name.png")
        img1=img1.resize((1530,130))
        self.Clg_img=ImageTk.PhotoImage(img1)
        
        lbl1=Label(self.root,image=self.Clg_img)
        lbl1.place(x=0,y=0,width=1530,height=130)
        
        
        #bg image
        img2=Image.open(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\fr_system.jpg")
        img2=img2.resize((1530,710))
        self.bg_img=ImageTk.PhotoImage(img2)
        
        bg_img_lbl=Label(self.root,image=self.bg_img)
        bg_img_lbl.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        
        # Student Details Button
        img3=Image.open("D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\students.jpg")
        img3=img3.resize((220,220))
        self.student_img=ImageTk.PhotoImage(img3)
        
        b1=Button(bg_img_lbl,image=self.student_img,cursor="hand2")
        b1.place(x=250,y=100,width=220,height=220)
        
        b1_1=Button(bg_img_lbl,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=250,y=320,width=220,height=40)
        
        
        
        # Face Detector Button
        img4=Image.open(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\face_detector.jpeg")
        img4=img4.resize((220,220))
        self.face_detector_img=ImageTk.PhotoImage(img4)
        
        b2=Button(bg_img_lbl,image=self.face_detector_img,cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)
        
        b2_1=Button(bg_img_lbl,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=320,width=220,height=40)
        
        
        
        # Attendance Button
        img5=Image.open(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\attendance.png")
        img5=img5.resize((220,220))
        self.attendance_img=ImageTk.PhotoImage(img5)
        
        b3=Button(bg_img_lbl,image=self.attendance_img,cursor="hand2")
        b3.place(x=750,y=100,width=220,height=220)
        
        b3_1=Button(bg_img_lbl,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=750,y=320,width=220,height=40)
        
        
        
        # Help Desk Button
        img6=Image.open("D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\help_desk.jpeg")
        img6=img6.resize((220,220))
        self.help_desk_img=ImageTk.PhotoImage(img6)
        
        b4=Button(bg_img_lbl,image=self.help_desk_img,cursor="hand2")
        b4.place(x=1000,y=100,width=220,height=220)
        
        b4_1=Button(bg_img_lbl,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1000,y=320,width=220,height=40)
        
        
        
        # Train data Button
        img7=Image.open(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\train data.png")
        img7=img7.resize((220,220))
        self.train_data_img=ImageTk.PhotoImage(img7)
        
        b5=Button(bg_img_lbl,image=self.train_data_img,cursor="hand2")
        b5.place(x=250,y=430,width=220,height=220)
        
        b5_1=Button(bg_img_lbl,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=250,y=650,width=220,height=40)
        
        
        
        # Photos Button
        img8=Image.open("D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\photos.jpeg")
        img8=img8.resize((220,220))
        self.photos_img=ImageTk.PhotoImage(img8)
        
        b6=Button(bg_img_lbl,image=self.photos_img,cursor="hand2")
        b6.place(x=500,y=430,width=220,height=220)
        
        b6_1=Button(bg_img_lbl,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=500,y=650,width=220,height=40)
        
        
        
        # Developer Button
        img9=Image.open("D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\developer.jpeg")
        img9=img9.resize((220,220))
        self.developer_img=ImageTk.PhotoImage(img3)
        
        b7=Button(bg_img_lbl,image=self.developer_img,cursor="hand2")
        b7.place(x=750,y=430,width=220,height=220)
        
        b7_1=Button(bg_img_lbl,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=750,y=650,width=220,height=40)
        
        
        
        # Exit Button
        img10=Image.open("D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\exit.jpeg")
        img10=img10.resize((220,220))
        self.exit_img=ImageTk.PhotoImage(img10)
        
        b8=Button(bg_img_lbl,image=self.exit_img,cursor="hand2")
        b8.place(x=1000,y=430,width=220,height=220)
        
        b8_1=Button(bg_img_lbl,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=1000,y=650,width=220,height=40)
        
        



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
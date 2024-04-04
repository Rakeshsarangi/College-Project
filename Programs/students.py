from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")
        
        
        
        # ===============Variables=============
        self.var_br=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_course=StringVar()
        self.var_regd=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_city=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()
        self.var_photo=StringVar()
        
        
        
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
        branch_lbl.place(x=0,y=110,width=150,height=40)
        
        
        branch_combo= ttk.Combobox(bg_img_lbl,textvariable=self.var_br,font=("times new roman",15),width=17,state="readonly")
        branch_combo["values"]=("Select Branch","MCA","CSc")
        branch_combo.current(0)
        branch_combo.place(x=150,y=110,width=150,height=40)
        
        
        #Year selector
        year_lbl=Label(bg_img_lbl,text="Year : ",font=("times new roman",20,"bold"),fg="black",)
        year_lbl.place(x=0,y=160,width=150,height=40)
        
        
        year_combo= ttk.Combobox(bg_img_lbl,textvariable=self.var_year,font=("times new roman",15),width=17,state="readonly")
        year_combo["values"]=("Select Year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.place(x=150,y=160,width=150,height=40)
        
        
        #Course selector
        course_lbl=Label(bg_img_lbl,text="Course : ",font=("times new roman",20,"bold"),fg="black",)
        course_lbl.place(x=350,y=110,width=150,height=40)
        
        
        course_combo= ttk.Combobox(bg_img_lbl,textvariable=self.var_course,font=("times new roman",15),width=17,state="readonly")
        course_combo["values"]=("Select Course","C","C++","java","python")
        course_combo.current(0)
        course_combo.place(x=500,y=110,width=150,height=40)
        
        
        #Semester selector
        semester_lbl=Label(bg_img_lbl,text="Semester : ",font=("times new roman",20,"bold"),fg="black",)
        semester_lbl.place(x=350,y=160,width=150,height=40)
        
        
        semester_combo= ttk.Combobox(bg_img_lbl,textvariable=self.var_sem,font=("times new roman",15),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        semester_combo.current(0)
        semester_combo.place(x=500,y=160,width=150,height=40)
        
        
        
        curr_course_lbl=Label(bg_img_lbl,text="STUDENT INFORMATION",font=("times new roman",15,"bold"),bg="yellow",fg="blue")
        curr_course_lbl.place(x=0,y=220,width=775,height=40)
        
        #Registration no. entry
        regd_lbl=Label(bg_img_lbl,text="Regd No. : ",font=("times new roman",15,"bold"),fg="black",)
        regd_lbl.place(x=0,y=280,width=175,height=30)
        
        
        regd_entry= ttk.Entry(bg_img_lbl,textvariable=self.var_regd,font=("times new roman",15),width=17)
        regd_entry.place(x=175,y=280,width=200,height=30)
        
        
        #Roll no. entry
        roll_lbl=Label(bg_img_lbl,text="Roll No. : ",font=("times new roman",15,"bold"),fg="black",)
        roll_lbl.place(x=400,y=280,width=175,height=30)
        
        
        roll_entry= ttk.Entry(bg_img_lbl,textvariable=self.var_roll,font=("times new roman",15),width=17)
        roll_entry.place(x=575,y=280,width=200,height=30)
        
        
        #Name entry
        name_lbl=Label(bg_img_lbl,text="Name : ",font=("times new roman",15,"bold"),fg="black",)
        name_lbl.place(x=0,y=320,width=175,height=30)
        
        
        name_entry= ttk.Entry(bg_img_lbl,textvariable=self.var_name,font=("times new roman",15),width=17)
        name_entry.place(x=175,y=320,width=200,height=30)
        
        
        #Gender entry
        gender_lbl=Label(bg_img_lbl,text="Gender : ",font=("times new roman",15,"bold"),fg="black",)
        gender_lbl.place(x=400,y=320,width=175,height=30)
        
        gender_combo= ttk.Combobox(bg_img_lbl,textvariable=self.var_gender,font=("times new roman",15),width=17,state="readonly")
        gender_combo["values"]=("Select Gender","M","F","O")
        gender_combo.current(0)
        gender_combo.place(x=575,y=320,width=200,height=30)
        
        
        #DOB entry
        DOB_lbl=Label(bg_img_lbl,text="DOB : ",font=("times new roman",15,"bold"),fg="black",)
        DOB_lbl.place(x=0,y=360,width=175,height=30)
        
        
        DOB_entry= ttk.Entry(bg_img_lbl,textvariable=self.var_dob,font=("times new roman",15),width=17)
        DOB_entry.place(x=175,y=360,width=200,height=30)
        
        
        # City entry
        city_lbl=Label(bg_img_lbl,text="City : ",font=("times new roman",15,"bold"),fg="black",)
        city_lbl.place(x=400,y=360,width=175,height=30)
        
        
        city_entry= ttk.Entry(bg_img_lbl,textvariable=self.var_city,font=("times new roman",15),width=17)
        city_entry.place(x=575,y=360,width=200,height=30)
        
        
        #Phone no. entry
        phone_lbl=Label(bg_img_lbl,text="Phone No. : ",font=("times new roman",15,"bold"),fg="black",)
        phone_lbl.place(x=0,y=400,width=175,height=30)
        
        
        phone_entry= ttk.Entry(bg_img_lbl,textvariable=self.var_phone,font=("times new roman",15),width=17)
        phone_entry.place(x=175,y=400,width=200,height=30)
        
        
        #Email entry
        email_lbl=Label(bg_img_lbl,text="Email : ",font=("times new roman",15,"bold"),fg="black",)
        email_lbl.place(x=400,y=400,width=175,height=30)
        
        
        email_entry= ttk.Entry(bg_img_lbl,textvariable=self.var_email,font=("times new roman",15),width=17)
        email_entry.place(x=575,y=400,width=200,height=30)
        
        # Radio buttons
        self.var_rbtn1=StringVar()
        radiobtn1=ttk.Radiobutton(bg_img_lbl,variable=self.var_rbtn1,text="Take Photo Sample",value="Yes")
        radiobtn1.place(x=20,y=435,width=150,height=40)
        
        self.var_rbtn2=StringVar()
        radiobtn2=ttk.Radiobutton(bg_img_lbl,variable=self.var_rbtn1,text="No Photo Sample",value="No")
        radiobtn2.place(x=200,y=435,width=150,height=40)
        
        
        #All buttons set
        save_btn=Button(bg_img_lbl,command=self.add_data,text="Save",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        save_btn.place(x=0,y=500,width=194,height=60)
        
        update_btn=Button(bg_img_lbl,command=self.update_data,text="Update",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        update_btn.place(x=194,y=500,width=194,height=60)
        
        delete_btn=Button(bg_img_lbl,command=self.delete_data,text="Delete",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        delete_btn.place(x=388,y=500,width=194,height=60) 
        
        reset_btn=Button(bg_img_lbl,command=self.rest_data,text="Reset",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        reset_btn.place(x=582,y=500,width=194,height=60)
        
        take_photo_btn=Button(bg_img_lbl,command=self.generate_dataset,text="Take Photo Sample",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        take_photo_btn.place(x=0,y=570,width=387,height=60)
        
        update_photo_btn=Button(bg_img_lbl,text="Update Photo Sample",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        update_photo_btn.place(x=388,y=570,width=387,height=60)
        
        
        #searching system title
        searching_system_lbl=Label(bg_img_lbl,text="Searching System",font=("times new roman",15,"bold"),bg="yellow",fg="blue")
        searching_system_lbl.place(x=777,y=45,width=775,height=40)
        
        
        # Searching system set
        search_by_lbl=Label(bg_img_lbl,text="Search By : ",font=("times new roman",15,"bold"),bg="red",fg="black")
        search_by_lbl.place(x=780,y=105,width=110,height=30)
        
        search_by_combo= ttk.Combobox(bg_img_lbl,font=("times new roman",15),width=17,state="readonly")
        search_by_combo["values"]=("Select","Regd no.","Roll no.")
        search_by_combo.current(0)
        search_by_combo.place(x=900,y=105,width=110,height=30)
        
        search_entry= ttk.Entry(bg_img_lbl,font=("times new roman",15),width=17)
        search_entry.place(x=1020,y=105,width=150,height=30)
        
        search_btn=Button(bg_img_lbl,text="Search",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        search_btn.place(x=1180,y=105,width=180,height=30)
        
        search_all_btn=Button(bg_img_lbl,text="Search All",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        search_all_btn.place(x=1370,y=105,width=180,height=30)
        
        
        # =====================Table Frame===============================
        table_frame=Frame(bg_img_lbl,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=777,y=145,width=750,height=520)
        
        
        #ScrollBar set
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("Branch","Year","Semester","Regd no","roll no","Name","Gender","DOB","City","Phone no","email","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        #Table heading set
        self.student_table.heading("Branch",text="Branch")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Regd no",text="Regd no")
        self.student_table.heading("roll no",text="roll no")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("City",text="City")
        self.student_table.heading("Phone no",text="Phone no")
        self.student_table.heading("email",text="email")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"
        
        
        #Table heading width set
        self.student_table.column("Branch",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Regd no",width=100)
        self.student_table.column("roll no",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("City",width=100)
        self.student_table.column("Phone no",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("Photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_br.get()=="Select Branch" or self.var_name.get()=="" or self.var_regd.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rakesh@347",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into STUDENT VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_br.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_regd.get(),
                                                                                                    self.var_roll.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_city.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_rbtn1.get(),
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added succeessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        
        
        
    # ===================Fetch Data====================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Rakesh@347",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    # =============Get cursor==============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_br.set(data[0]),
        self.var_year.set(data[1]),
        self.var_sem.set(data[2]),
        self.var_regd.set(data[3]),
        self.var_roll.set(data[4]),
        self.var_name.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_city.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_email.set(data[10]),
        self.var_rbtn1.set(data[11])
        
    # ========Update Function=============
    def update_data(self):
        if self.var_br.get()=="Select Branch" or self.var_name.get()=="" or self.var_regd.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","do you want to update this details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Rakesh@347",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Branch=%s,Year=%s,Semester=%s,Regd_no=%s,s_name=%s,Gender=%s,DOB=%s,City=%s,Phone_no=%s,email=%s,Photo=%s where Roll_no=%s",(
                                                                                                                                                                                        self.var_br.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                        self.var_regd.get(),
                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_city.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_rbtn1.get(),
                                                                                                                                                                                        self.var_roll.get()
                                                                                                                                                                                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student Detailes updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)
           
           
    # ==========delete functio===========
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Student roll no.must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Rakesh@347",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where roll_no=%s"
                    val=(self.var_roll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student Detailes deleted successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)
                
                
    # ===========reset function=============
    def rest_data(self):
        self.var_br.set("Select Branch"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_regd.set(""),
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_city.set(""),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_rbtn1.set("")
        
        
        
    # ==========_==Generate Dataset and Take photo sample=================
    def generate_dataset(self):
        if self.var_br.get()=="Select Branch" or self.var_name.get()=="" or self.var_regd.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rakesh@347",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Branch=%s,Year=%s,Semester=%s,Regd_no=%s,s_name=%s,Gender=%s,DOB=%s,City=%s,Phone_no=%s,email=%s,Photo=%s where Roll_no=%s",(
                                                                                                                                                                                        self.var_br.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                        self.var_regd.get(),
                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_city.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_rbtn1.get(),
                                                                                                                                                                                        self.var_roll.get()
                                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.rest_data()
                conn.close()
                
                # ===========Load predefined data on face frontals from opencv==========
                face_classfier=cv2.CascadeClassifier(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\Programs\haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray_scale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classfier.detectMultiScale(gray_scale,1.3,5)
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path=r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\Student pictures/student."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset completed!!!")
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)
                
                
                
                
                
                
                
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
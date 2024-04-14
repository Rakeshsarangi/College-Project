from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="sky blue")
        
        # ===============Variables===============
        
        self.var_username=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_c_password=StringVar()
        
        frame=Frame(self.root,bg="white")
        frame.place(x=450,y=100,width=600,height=600)
        
        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold","underline"),fg="green",bg="white")
        register_lbl.place(x=220,y=5)
        
        username_lbl=Label(frame,text="Full Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        username_lbl.place(x=40,y=68)
        
        user_entry= ttk.Entry(frame,textvariable=self.var_username,font=("times new roman",15),width=50)
        user_entry.place(x=220,y=70,width=300,height=30)
        
        email_lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email_lbl.place(x=40,y=128)
        
        email_entry= ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15),width=50)
        email_entry.place(x=220,y=130,width=300,height=30)
        
        securityq_lbl=Label(frame,text="Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
        securityq_lbl.place(x=40,y=188)
        
        securityq_combo= ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15),width=17,state="readonly")
        securityq_combo["values"]=("Select Question","What is Your birth date","What is your home city","What is your surname")
        securityq_combo.current(0)
        securityq_combo.place(x=220,y=190,width=300,height=30)
        
        securityA_lbl=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        securityA_lbl.place(x=40,y=248)
        
        securityA_entry= ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15),width=50)
        securityA_entry.place(x=220,y=250,width=300,height=30)
        
        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password_lbl.place(x=40,y=308)
        
        password_entry= ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15),width=50)
        password_entry.place(x=220,y=310,width=300,height=30)
        
        c_password_lbl=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        c_password_lbl.place(x=40,y=368)
        
        c_password_entry= ttk.Entry(frame,textvariable=self.var_c_password,font=("times new roman",15),width=50)
        c_password_entry.place(x=220,y=370,width=300,height=30)
        
        register_btn=Button(frame,text="Register",command=self.register_data,cursor="hand2",font=("times new roman",20,"bold"),bd=3,relief=RIDGE,bg="light green",fg="red",)
        register_btn.place(x=250,y=420,width=150,height=45)
        
        or_lbl=Label(frame,text="Or",font=("times new roman",20,"bold"),fg="black",bg="white")
        or_lbl.place(x=300,y=485)
        
        login_btn=Button(frame,text="Login",cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="black",)
        login_btn.place(x=250,y=540,width=150,height=40)
        
    # =============function declare=========
    def register_data(self):
        if self.var_username.get()=="" or self.var_email.get()=="" or self.var_password.get()=="":
            messagebox.showerror("error","All fields are required")
        elif self.var_password.get()!=self.var_c_password.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Rakesh@347",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from user where user_email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email Id already exist")
            else:
                my_cursor.execute("insert into user values(%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_username.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_password.get(),
                                                                                    self.var_c_password.get()
                                                                                    ))
                conn.commit()
                conn.close()                                                                   
                messagebox.showinfo("Success","Registration Successful")
            

        
if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()
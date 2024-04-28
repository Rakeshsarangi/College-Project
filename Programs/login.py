from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_Recognition_System
import mysql.connector

def common():
    win=Tk()
    app=Login(win)
    win.mainloop()

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="light blue")
        self.root.wm_iconbitmap(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\face_detector.ico")

        
        title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1550,height=45)
    
        
        frame=Frame(self.root,bg="light grey")
        frame.place(x=610,y=100,width=340,height=600)
        
        img1=Image.open(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\user_logo.png")
        img1=img1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(img1)
        img1_lbl=Label(image=self.photoimage1,bg="black",borderwidth=0)
        img1_lbl.place(x=730,y=105,width=100,height=100)
        
        
        login_lbl=Label(frame,text="Sign in",font=("times new roman",20,"bold"),fg="green",bg="light grey")
        login_lbl.place(x=130,y=100)
        
        # Label
        
        email_lbl=Label(frame,text="Enter Email",font=("times new roman",20,"bold"),fg="black",bg="light grey")
        email_lbl.place(x=50,y=155)
        
        self.email= ttk.Entry(frame,font=("times new roman",15),width=50)
        self.email.place(x=50,y=190,width=250,height=30)
        
        password_lbl=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="black",bg="light grey")
        password_lbl.place(x=50,y=250)
        
        self.password= ttk.Entry(frame,font=("times new roman",15),width=50)
        self.password.place(x=50,y=285,width=250,height=30)
        
        login_btn=Button(frame,command=self.login,text="Sign In",cursor="hand2",font=("times new roman",20,"bold"),bd=3,relief=RIDGE,bg="green",fg="white",)
        login_btn.place(x=100,y=340,width=150,height=40)
        
        forgot_btn=Button(frame,text="Forgot Password",command=self.forgot_password_window,cursor="hand2",font=("times new roman",15,"bold"),borderwidth=0,bg="light grey",fg="black",activebackground="light grey",activeforeground="black")
        forgot_btn.place(x=100,y=380,width=150,height=40)
        
        or_lbl=Label(frame,text="Or",font=("times new roman",20,"bold"),fg="black",bg="light grey")
        or_lbl.place(x=145,y=430)
        
        register_btn=Button(frame,text="Register",command=self.register,cursor="hand2",font=("times new roman",15,"bold"),bg="grey",fg="black",)
        register_btn.place(x=100,y=500,width=150,height=40)
        
    def login(self):
        if self.email.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All Field required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Rakesh@347",database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from user where user_email=%s and password=%s",(
                                                                                        self.email.get(),
                                                                                        self.password.get()
                                                                                        ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("Yesno","Access Only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                    # self.root.withdraw()# Destroy the login window
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()  


            
    
    # ================reset password===================
    def reset_password(self):
        if self.securityq_combo.get()=="Select Question":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.securityA_entry.get()=="":
            messagebox.showerror("Error","Please enter the security question answer",parent=self.root2)    
        elif self.re_password_entry.get()=="":
            messagebox.showerror("Error","Please Enter the new password",parent=self.root2)
        elif self.re_confirm_password_entry.get()=="":
            messagebox.showerror("Error","Please Enter the Confirm new password",parent=self.root2)
        elif self.re_confirm_password_entry.get()!=self.re_confirm_password_entry.get():
            messagebox.showerror("Error","Password and Confirm password must be same",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Rakesh@347",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from user where user_email=%s and securityQ=%s and securityA=%s")
            value=(self.email.get(),self.securityq_combo.get(),self.securityA_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Enter the correct answer",parent=self.root2)
            else:
                query1=("update user set password=%s,c_password=%s where user_email=%s")
                value1=(self.re_password_entry.get(),self.re_confirm_password_entry.get(),self.email.get())
                my_cursor.execute(query1,value1)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password Reset Successfully",parent=self.root2)
                self.root2.destroy()
    
    # ===========forgot Password==============        
    def forgot_password_window(self):
        if self.email.get()=="":
            messagebox.showerror("Error","Please Enter the Email")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Rakesh@347",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from user where user_email=%s")
            value=(self.email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Please Enter the valid email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                self.root2.configure(bg="white")
                
                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                securityq_lbl=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
                securityq_lbl.place(x=50,y=80)
                
                self.securityq_combo= ttk.Combobox(self.root2,font=("times new roman",15),width=17,state="readonly")
                self.securityq_combo["values"]=("Select Question","What is Your birth date","What is your home city","What is your surname")
                self.securityq_combo.current(0)
                self.securityq_combo.place(x=50,y=120,width=250,height=30)
                
                securityA_lbl=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
                securityA_lbl.place(x=50,y=165)
                
                self.securityA_entry= ttk.Entry(self.root2,font=("times new roman",15),width=50)
                self.securityA_entry.place(x=50,y=200,width=250,height=30)
                
                re_password_lbl=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black",bg="white")
                re_password_lbl.place(x=50,y=240)
                
                self.re_password_entry= ttk.Entry(self.root2,font=("times new roman",15),width=50)
                self.re_password_entry.place(x=50,y=275,width=250,height=30)
                
                re_confirm_password_lbl=Label(self.root2,text="Confirm New Password",font=("times new roman",15,"bold"),fg="black",bg="white")
                re_confirm_password_lbl.place(x=50,y=315)
                
                self.re_confirm_password_entry= ttk.Entry(self.root2,font=("times new roman",15),width=50)
                self.re_confirm_password_entry.place(x=50,y=350,width=250,height=30)
                
                reset_btn=Button(self.root2,text="Reset",command=self.reset_password,cursor="hand2",font=("times new roman",20,"bold"),bd=3,relief=RIDGE,bg="green",fg="white",)
                reset_btn.place(x=90,y=400,width=175,height=40)
                
    def register(self):
        win = Toplevel(self.root)
        app = Register(win)
        

                
            
    
        
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
        self.var_role_type=StringVar()
        
        frame=Frame(self.root,bg="white")
        frame.place(x=450,y=50,width=600,height=700)
        
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
        
        role_lbl=Label(frame,text="Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
        role_lbl.place(x=40,y=428)
        
        role_combo= ttk.Combobox(frame,textvariable=self.var_role_type,font=("times new roman",15),width=17,state="readonly")
        role_combo["values"]=("Select Role","Teacher","Student")
        role_combo.current(0)
        role_combo.place(x=220,y=430,width=300,height=30)
        
        register_btn=Button(frame,text="Register",command=self.register_data,cursor="hand2",font=("times new roman",20,"bold"),bd=3,relief=RIDGE,bg="light green",fg="red",)
        register_btn.place(x=250,y=480,width=150,height=45)
        
        or_lbl=Label(frame,text="Or",font=("times new roman",20,"bold"),fg="black",bg="white")
        or_lbl.place(x=300,y=545)
        
        login_btn=Button(frame,text="Login",command=self.return_login,cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="black",)
        login_btn.place(x=250,y=600,width=150,height=40)
        
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
                my_cursor.execute("insert into user values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_username.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_password.get(),
                                                                                    self.var_c_password.get(),
                                                                                    self.var_role_type.get()
                                                                                    ))
                conn.commit()
                conn.close()                                                                   
                messagebox.showinfo("Success","Registration Successful",parent=self.root)
        
    def return_login(self):
        if self.root.winfo_exists():  # Check if the root window still exists
            self.root.destroy()  # Destroy the register window
        if hasattr(self, 'root2') and self.root2.winfo_exists():  # Check if the root2 window exists
            self.root2.destroy()  # Destroy the forgot password window if it exists
        win = Tk()
        app = Login(win)
        win.mainloop()

        
        
        
if __name__ == "__main__":
    common()
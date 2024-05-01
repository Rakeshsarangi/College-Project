import pandas as pd
from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import datetime 

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance")
        self.root.geometry("1530x790+0+0")
# Read data from Excel file into a DataFrame
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        file_path = f"D:\\PROJECT\\FACE RECOGNITION ATTENDANCE SYSTEM\\College-Project\\Programs\\attendance_{date_str}.csv"
        df = pd.read_csv(file_path)

        # Create a Treeview widget
        tree = ttk.Treeview(root, columns=('Roll Number','Name','Branch','Teacher','Course','Time','Date','Status'), show='headings')
        tree.pack()

        # Add column headings
        for col in df.columns:
            tree.heading(col, text=col)

        # Add data to the Treeview
        for i, row in df.iterrows():
            tree.insert('', 'end', values=list(row))

if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()


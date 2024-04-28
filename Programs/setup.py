import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = (r"C:\Users\Rakesh Kumar Sarangi\AppData\Local\Programs\Python\Python312\tcl\tcl8.6")
os.environ['TK_LIBRARY'] = (r"C:\Users\Rakesh Kumar Sarangi\AppData\Local\Programs\Python\Python312\tcl\tk8.6")

executables = [cx_Freeze.Executable(r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\Programs\login.py", base=base, icon="face_detector.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":[r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg\face_detector.ico",r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\pictures-bg",r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\Programs\tcl86t.dll",r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\Programs\tk86t.dll",r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\Student pictures",r"D:\PROJECT\FACE RECOGNITION ATTENDANCE SYSTEM\College-Project\Database"]}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System ",
    executables = executables
    )

from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Portal")


        
# header 
# first image 
        img1=Image.open(r"images/biometric1.jpg")
        img1=img1.resize((500,150),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=150)
# second image
        img2=Image.open(r"images/biometric2.jpg")
        img2=img2.resize((500,150),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=510,y=0,width=505,height=150)
# third imageF
        img3=Image.open(r"images/biometric3.jpg")
        img3=img3.resize((600,150),Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1020,y=0,width=510,height=150)

# baground image
        img4=Image.open(r"images/nsti.jpg")
        img4=img4.resize((1530,755),Image.ADAPTIVE)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=850)

        title_lbl=Label(bg_img,text="STUDENT DETAIL PORTAL",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1540,height=50)

# student detail section
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=15,y=80,width=1495,height=690)


# left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"),bg="white",fg="green")
        Left_frame.place(x=20,y=10,width=700,height=640)

        img5=Image.open(r"images/student icon.jpg")
        img5=img5.resize((350,150),Image.ADAPTIVE)
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_lbl=Label(Left_frame,image=self.photoimg5)
        f_lbl.place(x=10,y=10,width=680,height=100)


        # current course
        Current_course_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",10,"bold"),bg="white",fg="green")
        Current_course_frame.place(x=30,y=160,width=680,height=120)

# department

        dep_label=Label(Current_course_frame,text="Department",font=("times new roman",10,"bold"),bg="white",fg="green")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(Current_course_frame,font=("times new roman",10,"bold"),width=12,state="readonly")
        dep_combo['values']=("Select Department","CITS","CTS","IBM")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

#course

        course_label=Label(Current_course_frame,text="Course",font=("times new roman",10,"bold"),bg="white",fg="green")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(Current_course_frame,font=("times new roman",10,"bold"),width=12,state="readonly")
        course_combo['values']=("Select Course","CSA","ADIT","CHNM","Solar","EM","Electrician")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=10)

# Batch

        Batch_label=Label(Current_course_frame,text="Batch",font=("times new roman",10,"bold"),bg="white",fg="green")
        Batch_label.grid(row=1,column=0,padx=10,sticky=W)

        Batch_combo=ttk.Combobox(Current_course_frame,font=("times new roman",10,"bold"),width=12,state="readonly")
        Batch_combo['values']=("Select Batch","First","Second")
        Batch_combo.current(0)
        Batch_combo.grid(row=1,column=1,padx=5,pady=10)

# Semester

        Semester_label=Label(Current_course_frame,text="Semester",font=("times new roman",10,"bold"),bg="white",fg="green")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        Semester_combo=ttk.Combobox(Current_course_frame,font=("times new roman",10,"bold"),width=12,state="readonly")
        Semester_combo['values']=("Select Semeste r","1st","2nd")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=5,pady=10)


     # Class Student Information
        Class_student_information=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",10,"bold"),bg="white",fg="green")
        Class_student_information.place(x=30,y=300,width=680,height=120)

        StudentID_label=Label(Class_student_information,text="StudentID",font=("times new roman",10,"bold"),bg="white",fg="green")
        StudentID_label.grid(row=0,column=0,padx=10,sticky=W)

        StudentID_entry=Entry(Class_student_information,width=20,font=("times new roman",13,"bold"))
        StudentID_entry.grid(row=0,column=1,sticky=W)









# right frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"),bg="white",fg="green")
        Right_frame.place(x=750,y=10,width=700,height=640)




















if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
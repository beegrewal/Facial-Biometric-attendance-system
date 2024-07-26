from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1200+0+0")
        self.root.title("Student Portal")

#variables for database
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_batch=StringVar()
        self.var_semester=StringVar()
        self.var_student_id=StringVar()
        self.var_class_division=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_student_name=StringVar()
        self.var_roll_number=StringVar()
        self.var_DOB=StringVar()
        self.var_Phone_no=StringVar()
        self.var_Teacher_name=StringVar()
        
### header 

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


### left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"),bg="white",fg="green")
        Left_frame.place(x=20,y=10,width=700,height=640)

        img5=Image.open(r"images/student icon.jpg")
        img5=img5.resize((350,150),Image.ADAPTIVE)
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_lbl=Label(Left_frame,image=self.photoimg5)
        f_lbl.place(x=10,y=10,width=680,height=100)

 ## current course Information
        Current_course_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",10,"bold"),bg="white",fg="green")
        Current_course_frame.place(x=30,y=160,width=680,height=120)

       # department

        dep_label=Label(Current_course_frame,text="Department",font=("times new roman",10,"bold"),bg="white",fg="green")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=20,state="readonly")
        dep_combo['values']=("Select Department","CITS","CTS","IBM")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        #course

        course_label=Label(Current_course_frame,text="Course",font=("times new roman",10,"bold"),bg="white",fg="green")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),width=20,state="readonly")
        course_combo['values']=("Select Course","CSA","ADIT","CHNM","Solar","EM","Electrician")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=10)

        # Batch

        Batch_label=Label(Current_course_frame,text="Batch",font=("times new roman",10,"bold"),bg="white",fg="green")
        Batch_label.grid(row=1,column=0,padx=10,sticky=W)

        Batch_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_batch,font=("times new roman",10,"bold"),width=20,state="readonly")
        Batch_combo['values']=("Select Batch","First","Second")
        Batch_combo.current(0)
        Batch_combo.grid(row=1,column=1,padx=5,pady=10)

        # Semester

        Semester_label=Label(Current_course_frame,text="Semester",font=("times new roman",10,"bold"),bg="white",fg="green")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        Semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),width=20,state="readonly")
        Semester_combo['values']=("Select Semeste r","1st","2nd")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=5,pady=10)


## Class Student Information
        Class_student_information=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",10,"bold"),bg="white",fg="green")
        Class_student_information.place(x=30,y=300,width=680,height=340)

        #Student ID
        StudentID_label=Label(Class_student_information,text="StudentID",font=("times new roman",10,"bold"),bg="white",fg="green")
        StudentID_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        StudentID_entry=Entry(Class_student_information,textvariable=self.var_student_id,width=20,font=("times new roman",13,"bold"))
        StudentID_entry.grid(row=0,column=1,sticky=W)

         #Student Name
        StudentN_label=Label(Class_student_information,text="Student Name",font=("times new roman",10,"bold"),bg="white",fg="green")
        StudentN_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        StudentN_entry=Entry(Class_student_information,textvariable=self.var_student_name,width=20,font=("times new roman",13,"bold"))
        StudentN_entry.grid(row=1,column=1,sticky=W)

         #Gender
        Gender_label=Label(Class_student_information,text="Gender",font=("times new roman",10,"bold"),bg="white",fg="green")
        Gender_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)
        
        
        Gender_combo=ttk.Combobox(Class_student_information,textvariable=self.var_gender,font=("times new roman",10,"bold"),width=23,state="readonly")
        Gender_combo['values']=("Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=1,column=3,sticky=W)

         #Address
        Address_label=Label(Class_student_information,text="Address",font=("times new roman",10,"bold"),bg="white",fg="green")
        Address_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        Address_entry=Entry(Class_student_information,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        Address_entry.grid(row=2,column=1,sticky=W)

          # Email
        Email_label=Label(Class_student_information,text="Email",font=("times new roman",10,"bold"),bg="white",fg="green")
        Email_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        Email_entry=Entry(Class_student_information,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        Email_entry.grid(row=2,column=3,sticky=W)

       

       
         #Roll Number
        Roll_Number_label=Label(Class_student_information,text="Roll Number",font=("times new roman",10,"bold"),bg="white",fg="green")
        Roll_Number_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        Roll_Number_entry=Entry(Class_student_information,textvariable=self.var_roll_number,width=20,font=("times new roman",13,"bold"))
        Roll_Number_entry.grid(row=3,column=1,sticky=W)

         #DOB
        DOB_label=Label(Class_student_information,text="DOB (YY/MM/DD)",font=("times new roman",10,"bold"),bg="white",fg="green")
        DOB_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)

        DOB_entry=Entry(Class_student_information,textvariable=self.var_DOB,width=20,font=("times new roman",13,"bold"))
        DOB_entry.grid(row=3,column=3,sticky=W)

         #Phone NO
        Phone_Number_label=Label(Class_student_information,text="Phone Number",font=("times new roman",10,"bold"),bg="white",fg="green")
        Phone_Number_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        Phone_Number_entry=Entry(Class_student_information,textvariable=self.var_Phone_no,width=20,font=("times new roman",13,"bold"))
        Phone_Number_entry.grid(row=4,column=1,sticky=W)

         #Teacher Name
        Teacher_label=Label(Class_student_information,text="Teacher Name",font=("times new roman",10,"bold"),bg="white",fg="green")
        Teacher_label.grid(row=4,column=2,padx=10,pady=10,sticky=W)

        Teacher_entry=Entry(Class_student_information,textvariable=self.var_Teacher_name,width=20,font=("times new roman",13,"bold"))
        Teacher_entry.grid(row=4,column=3,sticky=W)

## Radio Buttons
        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(Class_student_information,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        Radiobutton1.grid(row=5,column=0)
       
        self.var_radio2=StringVar()
        Radiobutton2=ttk.Radiobutton(Class_student_information,variable=self.var_radio1,text="No Photo Sample",value="No")
        Radiobutton2.grid(row=5,column=1)

        #Buttons frame
        button_frame=Frame(Class_student_information,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=5,y=250,width=665,height=70)
        
        save_button=Button(button_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="green",fg="white")
        save_button.grid(row=0,column=0)

        Update_button=Button(button_frame,text="Update",command=self.Update_data,width=16,font=("times new roman",13,"bold"),bg="green",fg="white")
        Update_button.grid(row=0,column=1)

        Delete_button=Button(button_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="green",fg="white")
        Delete_button.grid(row=0,column=2)
        
        Reset_button=Button(button_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="green",fg="white")
        Reset_button.grid(row=0,column=3)

        button_frame1=Frame(Class_student_information,bd=2,relief=RIDGE,bg="white")
        button_frame1.place(x=5,y=285,width=665,height=35)

        Take_photo_button=Button(button_frame1,text="Take Photo Sample",width=33,font=("times new roman",13,"bold"),bg="green",fg="white")
        Take_photo_button.grid(row=1,column=0)
        
        Update_Photo_button=Button(button_frame1,text="Update Photo Sample",width=33,font=("times new roman",13,"bold"),bg="green",fg="white")
        Update_Photo_button.grid(row=1,column=1)


### right frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"),bg="white",fg="green")
        Right_frame.place(x=750,y=10,width=700,height=640)

        
        img6=Image.open(r"images/student icon.jpg")
        img6=img6.resize((350,150),Image.ADAPTIVE)
        self.photoimg6=ImageTk.PhotoImage(img6)

        f_lbl=Label(Right_frame,image=self.photoimg6)
        f_lbl.place(x=10,y=10,width=680,height=100)
 
## Search System

        #search frame
        Search_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Search Student Information",font=("times new roman",10,"bold"),bg="white",fg="green")
        Search_frame.place(x=760,y=160,width=680,height=120)

        Search_label=Label(Search_frame,text="Search By :",font=("times new roman",10,"bold"),bg="white",fg="green")
        Search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",10,"bold"),width=20,state="readonly")
        Search_combo['values']=("Select","Roll No","Phone No")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=5,pady=10)

        Search_button=Button(Search_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="green",fg="white")
        Search_button.grid(row=0,column=2,padx=8)

        Show_button=Button(Search_frame,text="Show",width=12,font=("times new roman",13,"bold"),bg="green",fg="white")
        Show_button.grid(row=0,column=3,padx=8)

        #table frame
        Table_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Search Student Information",font=("times new roman",10,"bold"),bg="white",fg="green")
        Table_frame.place(x=760,y=300,width=680,height=340)

        Scrollbar_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,columns=("dep","course","batch","semester","student_id","student_name","gender","address","email","roll_number","DOB","phone_no","Teacher_name"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)

        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        Scrollbar_x.config(command=self.student_table.xview)
        Scrollbar_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("batch",text="Batch")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("student_id",text="Student Id")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("student_name",text="Student Name")
        self.student_table.heading("roll_number",text="Roll Number")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("phone_no",text="Phone No")
        self.student_table.heading("Teacher_name",text="Teacher Name")
        
        self.student_table['show']="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("batch",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("student_id",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("student_name",width=100)
        self.student_table.column("roll_number",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("phone_no",width=100)
        self.student_table.column("Teacher_name",width=100)



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
### Database System 

    def add_data(self):
        if self.var_dep.get()=="Select Deaprtment" or self.var_student_name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1973",database="face_recognisation_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_batch.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_student_id.get(),
                                                                                                                self.var_student_name.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_roll_number.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_Phone_no.get(),
                                                                                                                self.var_Teacher_name.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                               
                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Deatails added successfully",parent=self.root)
            except  Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 

## Fetch Data

    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="1973",database="face_recognisation_system")
         my_cursor=conn.cursor()
         my_cursor.execute("select * From Student")
         data=my_cursor.fetchall()

         if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                        self.student_table.insert("",END,values=i)
                conn.commit()
         conn.close()


## Get Cursor


    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_batch.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_student_id.set(data[4]),
        self.var_student_name.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_address.set(data[7]),
        self.var_email.set(data[8]),
        self.var_roll_number.set(data[9]),
        self.var_DOB.set(data[10]),
        self.var_Phone_no.set(data[11]),
        self.var_Teacher_name.set(data[12]),
        self.var_radio1.set(data[13]),
       

##Update Function

    def Update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_student_name.get() == "" or self.var_student_id.get() == "":
              messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                         host="localhost",
                         username="root",
                         password="1973",
                         database="face_recognisation_system"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        UPDATE student SET 
                            dep = %s,
                            course = %s,
                            batch = %s,
                            semester = %s,
                            student_name = %s,
                            gender = %s,
                            address = %s,
                            email = %s,
                            roll_number = %s,
                            DOB = %s,
                            phone_no = %s,
                            Teacher_name = %s
                        WHERE 
                            student_id = %s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_batch.get(),
                        self.var_semester.get(),
                        self.var_student_name.get(),
                        self.var_gender.get(),
                        self.var_address.get(),
                        self.var_email.get(),
                        self.var_roll_number.get(),
                        self.var_DOB.get(),
                        self.var_Phone_no.get(),
                        self.var_Teacher_name.get(),
                        self.var_student_id.get()
                    )) 
                   

                    conn.commit()
                    messagebox.showinfo("Success", "Student Details Updated Successfully", parent=self.root)
                    self.fetch_data()
                    conn.close()
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
        
##Delete Function   

    def delete_data(self):
        if self.var_student_id.get() == "":
           messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
               delete = messagebox.askyesno("Student Delete Page", "Do you want to delete student data?", parent=self.root)
               if delete > 0:
                   conn = mysql.connector.connect(
                       host="localhost",
                       username="root",
                       password="1973",
                       database="face_recognisation_system"
                   )
                   my_cursor = conn.cursor()
                   sql = "DELETE FROM student WHERE student_id = %s"
                   val = (self.var_student_id.get(),)
                   my_cursor.execute(sql, val)
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Success", "Student Details Deleted Successfully", parent=self.root)
               else:
                   return
            except Exception as es:
               messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

##Reset Function
    def reset_data(self):
        self.var_dep.set("")
        self.var_course.set("")
        self.var_batch.set("")
        self.var_semester.set("")
        self.var_student_id.set("")
        self.var_student_name.set("")
        self.var_gender.set("")
        self.var_address.set("")
        self.var_email.set("")
        self.var_roll_number.set("")
        self.var_DOB.set("")
        self.var_Phone_no.set("")
        self.var_Teacher_name.set("")
        self.var_radio1.set("")
        messagebox.showinfo("Success", "Form has been reset", parent=self.root)

        

      
               
                
                





if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
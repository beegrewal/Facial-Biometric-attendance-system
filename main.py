from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from student import Student

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1200+0+0")
        self.root.title("face recognition system")


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

        title_lbl=Label(bg_img,text="FACE RECOGNITION BIOMETRIC ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="Green")
        title_lbl.place(x=0,y=0,width=1540,height=50)

# student button

        img5=Image.open(r"images/student icon.jpg")
        img5=img5.resize((200,250),Image.ADAPTIVE)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.studentP,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=220)


        b1_1=Button(bg_img,text="Student Detail",command=self.studentP,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Green")
        b1_1.place(x=200,y=300,width=200,height=40)

# detect face

        img6=Image.open(r"images/detectface.jpg")
        img6=img6.resize((190,220),Image.ADAPTIVE)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=550,y=100,width=200,height=220)


        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Green")
        b1_1.place(x=550,y=300,width=200,height=40)


# Attendance

        img7=Image.open(r"images/attendance.jpeg")
        img7=img7.resize((180,200),Image.ADAPTIVE)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=850,y=100,width=200,height=220)


        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Green")
        b1_1.place(x=850,y=300,width=200,height=40)

# Help Desk

        img8=Image.open(r"images/helpdesk.jpg")
        img8=img8.resize((190,200),Image.ADAPTIVE)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=1150,y=100,width=200,height=220)


        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Green")
        b1_1.place(x=1150,y=300,width=200,height=40)



# Train Data

        img9=Image.open(r"images/data train.jpg")
        img9=img9.resize((190,200),Image.ADAPTIVE)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=200,y=400,width=200,height=220)


        b1_1=Button(bg_img,text="Training Data",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Green")
        b1_1.place(x=200,y=600,width=200,height=40)

# Photos

        img10=Image.open(r"images/gallery.jpg")
        img10=img10.resize((200,250),Image.ADAPTIVE)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=550,y=400,width=200,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Green")
        b1_1.place(x=550,y=600,width=200,height=40)


# Developer

        img11=Image.open(r"images/developer logo.jpg")
        img11=img11.resize((200,270),Image.ADAPTIVE)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=850,y=400,width=200,height=220)


        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Green")
        b1_1.place(x=850,y=600,width=200,height=40)

# Exit

        img12=Image.open(r"images/exit.jpg")
        img12=img12.resize((200,250),Image.ADAPTIVE)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2")
        b1.place(x=1150,y=400,width=200,height=220)


        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Green")
        b1_1.place(x=1150,y=600,width=200,height=40)




### Function Button 
    def studentP(self):
        self.new_windows=Toplevel(self.root)
        self.app=Student(self.new_windows)








if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
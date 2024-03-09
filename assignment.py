from tkinter import *
from tkcalendar import *
from tkinter import messagebox
import mysql.connector 
login = Tk()

login.title("student profile")
login.geometry("540x640+200+10")
login.resizable(0,0)
Frame1 = Frame(login, width=610,height=640,bg="#C39BD3")
Frame1.place(x=0,y=0)

my_label1 = StringVar()
my_label2 = StringVar()
my_label3 = StringVar()
my_label4 = StringVar()
my_label5 = StringVar()
gender1 = StringVar()
my_label8 = StringVar()
my_label9 = StringVar()
OM = StringVar()
cal = StringVar()

course = ["M.TECH(IT)","MCA","B.COM(HONS.)","MBA(APR)","MBA(E-SHIP)","MBA(MS)","MBA(MS)2YEARS","MBA(TA)","MBA(TOURISM)","PH.D(CS)","PH.D(MANAG)"]
OM.set("select course")

my_font = ("anuphan",20,"bold")
my_label = Label(login, text = "IIPS STUDENT RECORD",font= my_font,width=20)
font = ("poppins",15,"bold")

my_label1 = Label(login, text = "FIRST NAME:",font= font,bg="#C39BD3")
my_label2 = Label(login, text = "LAST NAME:",font= font,bg="#C39BD3")
my_label3 = Label(login, text = "ENROLLMENT NO.:",font= font,bg="#C39BD3")
my_label4 = Label(login, text = "COURSE:",font= font,bg="#C39BD3")
my_label5 = Label(login, text = "BATCH:",font= font,bg="#C39BD3")
my_label6 = Label(login, text = "DATE OF BIRTH:",font= font,bg="#C39BD3")
genderlabel = Label(login, text = "GENDER:",font= font,bg="#C39BD3")
my_label8 = Label(login, text = "ADDRESS:",font= font,bg="#C39BD3")
my_label9 = Label(login, text = "CONTACT:",font= font,bg="#C39BD3")

my_label.place(x=90,y=3)
my_label1.place(x=10,y=70)
my_label2.place(x=10,y=110)
my_label3.place(x=10,y=150)
my_label4.place(x=10,y=190)
my_label5.place(x=10,y=230)
my_label6.place(x=10,y=270)
genderlabel.place(x=10,y=310)
my_label8.place(x=10,y=350)
my_label9.place(x=10,y=390)
my_entry = Entry(login, width=40,borderwidth=2)
my_entry.place(x=240,y=70)

my_entry1 = Entry(login, width=40,borderwidth=2)
my_entry1.place(x=240,y=110)

my_entry3 = Entry(login, width=40,borderwidth=2)
my_entry3.place(x=240,y=150)

my_entry4 = Entry(login, width=40,borderwidth=2)
my_entry4.place(x=240,y=230)

my_entry5 = Entry(login, width=40,borderwidth=2)
my_entry5.place(x=240,y=350)

my_entry6 = Entry(login, width=40,borderwidth=2)
my_entry6.place(x=240,y=390)

gender1.set(0)
radio1 = Radiobutton(login, text="Male", variable=gender1, value= "Male", font="poppins 13")
radio1.place(x=240,y=310)

radio2 = Radiobutton(login, text="Female", variable=gender1,value="female",font="poppins 13")
radio2.place(x=310,y=310)

radio3 = Radiobutton(login, text="Others",variable=gender1,value="others",font="poppins 13")
radio3.place(x=400,y=310)


dropdown1 = OptionMenu(login,OM, *course)
dropdown1.place(x=240,y=190)
#calendar

cal = DateEntry(login, selectmode= "day",width=30, date_pattern="y/mm/dd")
cal.place(x=240,y=270)

def answer():

    if my_entry.get() == " ":
        messagebox.showerror("please enter your first name")
    
    elif my_entry1.get() ==" ":
        messagebox.showerror("please enter your last name")

    elif my_entry3.get() ==" ":
        messagebox.showerror("please enter your enrollment no.")

    elif OM.get() ==" ":
        messagebox.showerror("please enter your course")

    elif my_entry4.get() ==" ":
        messagebox.showerror("please enter your batch")

    elif cal.get() ==" ":
        messagebox.showerror("please enter your DOB")

    elif gender1.get() ==" ":
        messagebox.showerror("please enter your gender")

    elif my_entry5.get() ==" ":
        messagebox.showerror("please enter your address")
   
    elif my_entry6.get() ==" ":
        messagebox.showerror("please enter your contact")

    else:
        mydb = mysql.connector.connect(host="localhost",user="root",password="swarnali0601@",database="iips_student_record")
        try: 
          cur=mydb.cursor()
          cur.execute("CREATE DATABASE IIPS_STUDENT_RECORD")
          cur.execute("use IIPS_STUDENT_RECORD")    
        #messagebox.showinfo("success","successful")
        #print("worked")
          cur.execute("CREATE TABLE STUDENT (FIRST_NAME VARCHAR(50),LAST_NAME VARCHAR(50),ENROLLMENT_NO VARCHAR(30),COURSE VARCHAR(30),BATCH VARCHAR(30),DOB DATE,GENDER ENUM('M','F','O'),ADDRESS VARCHAR(55),CONTACT BIGINT,PRIMARY KEY(ENROLLMENT_NO))")
          messagebox.showinfo("table established")
          cur.execute("ALTER TABLE student modify COLUMN gender VARCHAR(30)")
          messagebox.showinfo("success,altered")
        except:
            query='INSERT INTO STUDENT(FIRST_NAME,LAST_NAME,ENROLLMENT_NO,COURSE,BATCH,DOB,GENDER,ADDRESS,CONTACT) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'          
            val= (my_entry.get(),my_entry1.get(),my_entry3.get(),OM.get(),my_entry4.get(),cal.get(),gender1.get(),my_entry5.get(),my_entry6.get())
            cur.execute(query,val)
            mydb.commit()
            mydb.close()
            messagebox.showinfo("success,value inserted")
    
    my_entry.delete(0,END)
    my_entry1.delete(0,END)
    my_entry3.delete(0,END)
    my_entry4.delete(0,END)
    my_entry5.delete(0,END)
    my_entry6.delete(0,END)

def eliminate():
        mydb = mysql.connector.connect(host="localhost",user="root",password="swarnali0601@",database="iips_student_record")
        sql = "DELETE FROM student"
        cur=mydb.cursor()
        cur.execute(sql)
        mydb.commit()
        messagebox.showinfo(",value deleted")

my_button1 = Button(login, text = "submit",command=answer,fg="white",bg="black",font="poppin 15",width=10,height=1,borderwidth=2)
my_button1.place(x=200,y=450)

delete = Button(login,text = "delete",command = eliminate,fg="white",bg="black",font="poppin 15",width=10,height=1,borderwidth=2)
delete.place(x=200,y=500)
login.mainloop()


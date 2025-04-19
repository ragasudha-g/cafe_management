import  tkinter as t
import tkinter.messagebox as m
import sqlite3
db=sqlite3.connect('student.db')
cur=db.cursor()
cur.execute("CREATE TABLE ADMISSION(Enroll_no CHAR(7),Name CHAR(30),Age INT,Gender CHAR(1), Course CHARSSSS(10))");

master=t.Tk()
group=t.LabelFrame(master,text="Student Data Entry Screen", padx=10,pady=10)
group.pack(padx=10,pady=10)

admission_no=t.StringVar()
name=t.StringVar()
age=t.StringVar()
gender=t.IntVar()
course=t.StringVar()

def add_records():
        if gender.get()==1:
                gen="Male"
        elif gender.get()==2:
                gen="Female"
        elif gender.get()==3:
                gen="Transgender"
        course=courselist.get(courselist.curselection())
        sql="INSERT INTO ADMISSION(Enroll_no,Name,Age,Gender,Course)VALUES('%s','%s','%s','%s','%s');"%(admission_no.get(),name.get(),age.get(),gen,course)
        cur.execute(sql)
        db.commit()
        m.showinfo("Add Record","One Record Added Successfully")

def clr():
        widjet.delete(0,t.END)
        widjet1.delete(0,t.END)
        widjet2.delete(0,t.END)

def disp():
        sql="SELECT*FROM ADMISSION"
        cur.execute(sql)
        rows=cur.fetchall()
        for row in rows:
                print(row)

t.Label(group,text="Admission No:").grid(row=0,column=3)
widjet=t.Entry(group,textvariable=admission_no)
widjet.grid(row=0,column=15)

t.Label(group,text="Student Name:").grid(row=2,column=3)
widjet1=t.Entry(group,textvariable=name)
widjet1.grid(row=2,column=15)

t.Label(group,text="Age:").grid(row=4,column=3)
widjet2=t.Entry(group,textvariable=age)
widjet2.grid(row=4,column=15)

t.Label(group,text="Gender:").grid(row=6,column=3)
radio1=t.Radiobutton(group,text="Male",variable=gender,value=1).grid(row=6,column=10)
radio2=t.Radiobutton(group,text="Female",variable=gender,value=2).grid(row=6,column=15)
radio3=t.Radiobutton(group,text="Transgender",variable=gender,value=3).grid(row=6,column=20)

t.Label(group,text="Course").grid(row=8,column=3)
courselist=t.Listbox(group)
courselist.insert(1,"C")
courselist.insert(2,"C++")
courselist.insert(3,"Java")
courselist.insert(4,"Python")
courselist.insert(5,"None")
courselist.grid(row=8,column=15)

add=t.Button(group,text="Add",command=add_records).grid(row=18,column=5)
clear=t.Button(group,text="Clear",command=clr).grid(row=18,column=15)
display=t.Button(group,text="Show",command=disp).grid(row=18,column=10)

t.mainloop()
db.close()

from tkinter import *
import sqlite3
import tkinter.messagebox
from PIL import Image,ImageTk

root = Tk()
root.geometry("700x700")
root.title("Registration form")

img=Image.open("C:/Users/KARTHIK SHETTY/Desktop/my files/karthik.jpg")
photo=ImageTk.PhotoImage(img)
lab=Label(image=photo).pack()

menu=Menu(root)
root.config(menu=menu)

fn=StringVar()
ln=StringVar()
dob=StringVar()
var=StringVar()
var_chkbtn1="python"
var_chkbtn2="java"
var_radiobtn=StringVar()

def exit_1():
    exit()

def abt():
    tkinter.messagebox.showinfo("welcome","menu option")

def database():
    name = fn.get()
    lastname = ln.get()
    dateofbirth = dob.get()
    gender = var_radiobtn.get()
    country = var.get()
    proglang = var_chkbtn2
    conn = sqlite3.connect("Form.db")
    with conn:
        cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student(name TEXT,lastname TEXT,dob TEXT,gender TEXT,country TEXT,proglang TEXT)')
    cursor.execute('INSERT INTO Student (name,lastname,dob,gender,country,proglang) VALUES(?,?,?,?,?,?)',(name, lastname, dateofbirth, gender, country, proglang,))
    conn.commit()

submenu1 = Menu(menu)
menu.add_cascade(label="file", menu=submenu1)
submenu1.add_command(label="exit", command=exit_1)

submenu2 = Menu(menu)
menu.add_cascade(label="option", menu=submenu2)
submenu2.add_command(label="about", command=abt)

label1=Label(root,text='registration box',relief='solid',bg='white',fg='black',font=('arial',20,'bold')).place(x=240,y=250)

label2=Label(root,text="name:",font=("arial",15,"bold")).place(x=100,y=300)
entry2=Entry(root,text=fn).place(x=250,y=306)

label3=Label(root,text="lastname",font=("arial",15,"bold")).place(x=100,y=330)
entry3=Entry(root,text=ln).place(x=250,y=333)

label4=Label(root,text="date of birth",font=("arial",15,"bold")).place(x=100,y=360)
entry4=Entry(root,text=dob).place(x=250,y=363)

label5=Label(root,text="gender",font=("arial",15,"bold")).place(x=100,y=390)
radiobutton1=Radiobutton(root,text="male",variable=var_radiobtn,value="male").place(x=250,y=393)
radiobutton2=Radiobutton(root,text="female",variable=var_radiobtn,value="female").place(x=350,y=393)

label6=Label(root,text="program lang",font=("arial",15,"bold")).place(x=100,y=416)
checkbutton1=Checkbutton(root,text="python",variable=var_chkbtn1).place(x=250,y=418)
checkbutton2=Checkbutton(root,text="java",variable=var_chkbtn2).place(x=350,y=418)

label7=Label(root,text="country",font=("arial",15,"bold")).place(x=100,y=445)
list1=["india","nepal","canada"]
droplist=OptionMenu(root,var,*list1)
var.set("select country")
droplist.config(width=15)
droplist.place(x=250,y=446)

but_signup=Button(root,text="signup",bg="red",font=("arial",15,"bold"),command=database).place(x=110,y=500)
root.bind("<Return>",database)
but_login=Button(root,text="login",bg="red",font=("arial",15,"bold"),command=exit_1).place(x=210,y=500)

root.mainloop()



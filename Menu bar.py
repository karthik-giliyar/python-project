from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("700x700")
root.title("complete registarion box")

img = Image.open("C:/Users/KARTHIK SHETTY/Desktop/my files/karthik.jpg")
photo = ImageTk.PhotoImage(img)
lab = Label(image=photo.pack()

menu = Menu(root)
root.config(menu=menu)


fn=StringVar()
ln=StringVar()
dob=StringVar()
var=StringVar()
var_chkbtn1=StringVar()
var_chkbtn2=StringVar()
var_radiobtn=StringVar()

def exit_1():
    exit()


def abt():
    tkinter.messagebox.showinfo("welcome", "this is demo for menu field")

def print_1():
    name=fn.get()
    lastname=ln.get()
    dateofbirth=dob.get()
    gender=var_radiobtn.get()
    country=var.get()
    proglang="python"
    proglang="java"
    print(f"Name of the candidate is {name} {lastname}")
    print(f"And his date of birth is {dateofbirth}")
    print(f"And he is {gender}")
    print(f"And he is from {country}")
    print(f"And his language proficiency is {proglang}")

def new_window():
    window=Tk()
    window.geometry("250x250")
    window.title("second window")

    label8=Label(window,text="karthik",font=("arial",15,"bold")).pack()
    but_ok=Button(window,text="ok",font=("arial",15,"bold"),bg="red",command=exit_1).place(x=100,y=175)


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

but_signup1=Button(root,text="signup",bg="red",font=("arial",15,"bold"),command=print_1).place(x=110,y=500)
but_signup2=Button(root,text="quit",bg="red",font=("arial",15,"bold"),command=exit_1).place(x=300,y=500)
but_login=Button(root,text="login",bg="red",font=("arial",15,"bold"),command=new_window).place(x=210,y=550)

root.mainloop()

from tkinter import *
from PIL import Image,ImageTk

root= Tk()
root.geometry("500x500")
root.title("registration form")

img=Image.open("C:/Users/KARTHIK SHETTY/Desktop/my files/karthik.jpg")
imagee=ImageTk.PhotoImage(img)

label_=Label(image=imagee)
label_.pack()

fn=StringVar()
ln=StringVar()
dob=StringVar()
nation=StringVar()

def print_1():
    nam=fn.get()
    second=ln.get()
    birth=dob.get()
    nationality=nation.get()
    print(f"the name is {nam} {second}")
    print(f"date of birth is {birth}")
    print(f"the nationality is {nationality}")

def exit_1():
    exit()

label= Label(root, text="Registration Form", fg="black", bg="white", relief="solid", font=("", 15, "bold"))
label.pack()


label_1= Label(root, text="name:", fg="black", bg="white",font=("", 15, "bold"))
label_1.place(x=120,y=300)

entry_1=Entry(root,textvar=fn)
entry_1.place(x=300,y=307)

label_2= Label(root, text="last name:", fg="black", bg="white", font=("", 15, "bold"))
label_2.place(x=120,y=333)

entry_2=Entry(root,textvar=ln)
entry_2.place(x=300,y=340)

label_3= Label(root, text="DOB:", fg="black", bg="white", font=("", 15, "bold"))
label_3.place(x=120,y=360)

entry_3=Entry(root,textvar=dob)
entry_3.place(x=300,y=365)

list_1=["India","Nepal","Denmark","Canada","England"]
droplist=OptionMenu(root,nation,*list_1)
nation.set("select country")
droplist.config(width=10)
droplist.place(x=300,y=393)

label_3= Label(root, text="country:", fg="black", bg="white", font=("", 15, "bold"))
label_3.place(x=120,y=390)

entry_4=Entry(root,textvar=nation,width=14)
entry_4.place(x=300,y=398)

button_1=Button(root,text="login", fg="green", bg="brown", relief="groove", font=("ariel", 15, "bold"),command=print_1)
button_1.place(x=100,y=450)
button_2=Button(root,text="exit0", fg="green", bg="brown", relief="groove", font=("ariel", 15, "bold"),command=exit_1)
button_2.place(x=350,y=450)

root.mainloop()
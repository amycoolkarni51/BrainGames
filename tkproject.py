from tkinter import *
from tkinter import messagebox
from subprocess import Popen



root = Tk()
root.geometry('400x400')
root.title("Brain Games")
#on submit button start game
def printt():  
    fn1=fn.get()
    var1=var.get()
    print(fn1,var1)
    messagebox.showinfo("Welcome","DO YOU WANT TO CONTINUE??")
#On quit button exit game
def exit1():
    exit()
#AboutUs
def abt():
    messagebox.showinfo("Know AboutUs","""This is a fun game portal for kids mostly in the age group of 10-20. 
Helps sharpen the young minds.""")
#TicTacToe
def first():
    Popen('python tkproject1.py')
def second():
    Popen('python tkproject2.py')
def third():
    Popen('python tkproject3.py')
def forth():
    Popen('python tkproject4.py')

    
menu=Menu(root)
root.config(menu=menu)
subm1=Menu(menu)
menu.add_cascade(label="File",menu=subm1)
subm1.add_command(label="Exit",command=exit1)
subm2=Menu(menu)
menu.add_cascade(label="Option",menu=subm2)
subm2.add_command(label="About",command=abt)
lable_1=Label(root,text="Brain Games",width=40,fg="black",relief="solid",bg="light blue",font=("bold",30)).pack(fill=BOTH,padx=2,pady=2)
fn=StringVar()
var=StringVar()

lable_3=Label(root,text="Select game from the list below:",width=30,fg="black",font=("bold",15)).pack(fill=BOTH,padx=2,pady=2)
var=IntVar()
Button1=Button(root,text="TicTacToe",width=10,fg="black",relief="solid",bg="light blue",font=("bold",15),command=first)
Button1.pack(fill=BOTH,padx=120,pady=5)
Button2=Button(root,text="Tiles Game",width=10,fg="black",relief="solid",bg="light blue",font=("bold",15),command=second)
Button2.pack(fill=BOTH,padx=120,pady=5)
Button3=Button(root,text="Number Game",width=10,fg="black",relief="solid",bg="light blue",font=("bold",15),command=forth)
Button3.pack(fill=BOTH,padx=120,pady=5)
Button4=Button(root,text="GK Quiz",width=10,fg="black",relief="solid",bg="light blue",font=("bold",15),command=third)
Button4.pack(fill=BOTH,padx=120,pady=5)
Button5=Button(root,text="Quit",width=20,fg="black",relief="solid",bg="orange",font=("bold",15),command=exit1)
Button5.pack(fill=BOTH,padx=20,pady=20)






root.mainloop()
from tkinter import *
from tkinter import messagebox
import random
window2=Tk()
window2.title('Tile-Match game')
window2.geometry('500x500')
Label2=Label(text="Tile Game",font=("Arial",20,"bold"),bg="light blue",relief="solid")
Label2.pack(fill=BOTH,padx=2,pady=2)
global winner
winner=0

#create our matches
matches=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
# Shuffle our matches
random.shuffle(matches)
print(matches)
#create button frames
my_frame=Frame(window2)
my_frame.pack(pady=10)
#define variables
count=0
answer_list=[]
answer_dict={}
# Reset function
def reset():
    global matches, winner
    #create our matches
    matches=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
    # Shuffle our matches
    random.shuffle(matches)
    # reset label
    label1.config(text="")
    # reset tiles
    button_list=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]
    #loop through button and change colors
    for button in button_list:
        button.config(text="",bg="SystemButtonFace",state="normal")
#create winner function
def win():
    label1.config(text="Congratulations!!! You Win")
    button_list=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]
    #loop through button and change colors
    for button in button_list:
        button.config(bg="light blue",relief=SOLID,font=("Helvetica",10,"bold"))
#function for clicking button
def button_click(b,number):
    global count, answer_list, answer_dict,winner
    if b["text"]==' ' and count<2:
        b["text"]=matches[number]
        # Add number to answer list
        answer_list.append(number)
        # Add button and number to Answer dict
        answer_dict[b]=matches[number]
        #increment our counter
        count=count+1
    #start to determine correct or not
    if len(answer_list)==2:
        if matches[answer_list[0]]==matches[answer_list[1]]:
            label1.config(text="Match!",bg="yellow")
            for key in answer_dict:
                key["state"]="disabled"
            count=0
            answer_list=[]
            answer_dict={}
            # increment our winner counter
            winner = winner + 1
            if winner==8:
                win()
        else:
            count=0
            answer_list=[]
            # pop up box
            messagebox.showinfo("Tile-Match game","Incorrect")
            #Reset
            for key in answer_dict:
                key["text"]=" "
            answer_dict={}

#Define our buttons
b0= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b0,0),relief="groove")
b1= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b1,1),relief="groove")
b2= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b2,2),relief="groove")
b3= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b3,3),relief="groove")
b4= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b4,4),relief="groove")
b5= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b5,5),relief="groove")
b6= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b6,6),relief="groove")
b7= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b7,7),relief="groove")
b8= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b8,8),relief="groove")
b9= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b9,9),relief="groove")
b10= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b10,10),relief="groove")
b11= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b11,11),relief="groove")
b12= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b12,12),relief="groove")
b13= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b13,13),relief="groove")
b14= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b14,14),relief="groove")
b15= Button(my_frame, text=" ",font=("Helvetica",18,"bold"),height=2,width=4,command=lambda:button_click(b15,15),relief="groove")


#grid our buttons
b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)
b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)
b12.grid(row=3,column=0)
b13.grid(row=3,column=1)
b14.grid(row=3,column=2)
b15.grid(row=3,column=3)
label1=Label(window2,text="")
label1.pack(pady=10)
#create menu
my_menu=Menu(window2)
window2.config(menu=my_menu)
option_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="Reset game",command=reset)
option_menu.add_separator()
option_menu.add_command(label="Back",command=window2.quit)


window2.mainloop()
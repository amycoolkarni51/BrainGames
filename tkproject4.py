from tkinter import * 
from random import randint, choice
window4=Tk()
window4.title("Maths Quiz")
window4.geometry("400x400")
#Creating first question
number1=randint(1,10)
number2=randint(1,10)
list1=["+","-","*"]
method=choice(list1)

question="          "+str(number1)+method+str(number2)+" ?           "
correctAnswer=number1+number2
question1=Label(text=question,font=("Arial",20,"bold"),bg="light blue",borderwidth=10)
question1.place(relx=.5, rely=.3,anchor= CENTER)

givenAnswer=IntVar()
score=0 
questions=1
total=10

def nextQuestion():
    global score
    global correctAnswer
    global questions
    global method
    #check answer
    if givenAnswer.get()==correctAnswer:
        score = score+1
    correctAnswer= -1
    #show updated score
    Score=Label(text=f"Current Score: {score}/{total}",font=("Arial",10,"bold"),bg="light blue",borderwidth=10)
    Score.place(relx=.5, rely=.9,anchor= CENTER)

    if questions>=total:
        Score=Label(text=f"final Score: {score}/{questions}",font=("Arial",10,"bold"),bg="light blue",borderwidth=10)
        Score.place(relx=.5, rely=.9,anchor= CENTER)
        return
    #next question
    questions=questions+1
    number1=randint(1,10)
    number2=randint(1,10)

    question="          "+str(number1)+method+str(number2)+" ?           "
    if method == "+":
        correctAnswer=number1+number2
    elif method == "-":
        correctAnswer=number1-number2
    elif method == "*":
        correctAnswer=number1*number2

    
    question1=Label(text=question,font=("Arial",20,"bold"),width=30,bg="light blue",borderwidth=10)
    question1.place(relx=.5, rely=.3,anchor= CENTER)

Label1=Label(text="Maths Quiz",font=("Arial",40,"bold"),bg="light blue",borderwidth=10)
Label1.place(relx=.5, rely=.1,anchor= CENTER)


#Answer Entry
answer1=Entry(textvariable=givenAnswer,font=("Arial",20,"bold"),borderwidth=10)
answer1.place(relx=.5, rely=.5,anchor= CENTER)

submit=Button(text="Submit",font=("Arial",20,"bold"),bg="light blue",borderwidth=10,command=nextQuestion)
submit.place(relx=.5,rely=.7,anchor=CENTER)

Score=Label(text=f"Current Score: 0/{total}",font=("Arial",10,"bold"),bg="light blue",borderwidth=10)
Score.place(relx=.5, rely=.9,anchor= CENTER)
my_menu=Menu(window4)
window4.config(menu=my_menu)
    #create menu options
option_menu=Menu(my_menu)
my_menu.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="Back",command=window4.quit)
window4.mainloop()
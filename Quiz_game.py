import pandas as pd
import tkinter as tk
import random 

data=pd.read_csv('Quizfile.csv')
# print(data)
root=tk.Tk()
root.geometry('500x500')
root.title("Quiz Game")
root.configure(bg="pink")

welcome_text=tk.Label(root,text="Quiz",bg="pink",anchor="center",justify="center",font="pixel_font,20",wraplength="500")
welcome_text.pack(pady=20)


btn1=tk.Button(root,text="",command=lambda:check_answer(btn1),width=50,height=3)
btn2=tk.Button(root,text="",command=lambda:check_answer(btn2),width=50,height=3)
btn3=tk.Button(root,text="",command=lambda:check_answer(btn3),width=50,height=3)
btn4=tk.Button(root,text="",command=lambda:check_answer(btn4),width=50,height=3)

# btn1.pack_forget()
# btn2.pack_forget()
# btn3.pack_forget()
# btn4.pack_forget()
button_next=tk.Button(root,text="Next",command=lambda:onclick(),width=20,height=3)
button_next.pack_forget()

Current_answer=""
button_start=tk.Button(root,text="Start Quiz",command=lambda:startquiz(),width=20,height=3,bg="pink")
button_start.pack(padx=10,pady=10)
count=0
def startquiz():
    button_start.pack_forget()
    button_next.config(state=tk.NORMAL)
    
    btn1.pack(padx=10,pady=10)
    btn2.pack(padx=10,pady=10)
    btn3.pack(padx=10,pady=10)
    btn4.pack(padx=10,pady=10)
    button_next.pack(padx=10,pady=10)
    onclick()

def onclick():
    global Current_answer , count
    random_value=data.sample(n=1).iloc[0]
    question=random_value['Question']
    CorrectAnswer=random_value['Correct Answer']
    Current_answer=CorrectAnswer
    IncorrectAnswer=eval(random_value['Incorrect Answer'])


    all_answers=[CorrectAnswer]+IncorrectAnswer
    random.shuffle(all_answers)
    count+=1
    if count>5:
        btn1.pack_forget()
        btn2.pack_forget()
        btn3.pack_forget()
        btn4.pack_forget()
        button_next.pack_forget()
        welcome_text.pack_forget()
        text=tk.Label(root,text=" YOU COMPLETED THE QUIZ ",bg="pink",anchor="center",justify="center",font="pixel_font,20",wraplength="500")
        text.pack(pady=20)
        result=tk.Label(root,text=f"You scored {score} out of 5",bg="pink",anchor="center",justify="center",font="pixel_font,20",wraplength="500")
        result.pack(pady=30)
    else:
        welcome_text.config(text=question)
        btn1.config(text=all_answers[0],bg="lightgray")
        btn2.config(text=all_answers[1],bg="lightgray")
        btn3.config(text=all_answers[2],bg="lightgray")
        btn4.config(text=all_answers[3],bg="lightgray")
        
score=0 
def check_answer(button):
    global score
    selected_answer=button.cget("text")
    if selected_answer == Current_answer:
        score+=1
        button.config(bg="lightgreen")
    else:
        button.config(bg="red")
    root.after(250,onclick)


  

root.mainloop()


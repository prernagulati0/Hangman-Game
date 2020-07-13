#main function
def hangman():
    global picked,right,n,entryy,wrong,x,temp,chances
    guess = inp.get()
    entry.delete(0,END)
    
    if(n>1):      
        if guess in picked:
            for i in range(len(picked)):
                while picked[i]==guess :
                    right.pop(i)
                    right.insert(i,guess)
                    x=''.join(right)
                    word.configure(text=x)
                    if x==temp:
                        result.configure(text='you won, congratulation!!')
                        reset=messagebox.askyesno("Notification",' want to play again?')
                        if reset==True:
                            chooseword()
                            photo3 = ImageTk.PhotoImage(Image.open("/Users/dell/Downloads/5.png"))
                            label.configure(image = photo3) 
                            label.place(x=590,y=150)
                            label.update(photo3)
                        else:
                            root.destroy()
                    else:
                        break
        else:
            n -= 1 
            guesses.configure(text='No. of guesses = {}'.format(n))
            chng()
    
    if n==1:
        guesses.configure(text='No. of guesses = 0')
        result.configure(text='You lose the game!!') 
        z.configure(text='I picked:  {}'.format(picked))
        photo3 = ImageTk.PhotoImage(Image.open("/Users/dell/Downloads/0.png"))
        label.configure(image = photo3) 
        label.place(x=590,y=150)
        label.update(photo3)
       
def jj(event):
    hangman()  

def b():
    chooseword()
    photo3 = ImageTk.PhotoImage(Image.open("/Users/dell/Downloads/5.png"))
    label.configure(image = photo3) 
    label.place(x=590,y=150)
    label.update(photo3)
    
#import modules       
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root = Tk()
root.geometry('1200x670+90+15')
root.configure(bg='#f0f0f0',padx=100)
root.title('Hangman Game')

words = ['titanic','cindrella','goodfellas','vertigo','alien','batman','joker','halloween','superman','aladin',
         'bambi','shrek','inception','predator','matilda','memento','cocktail','parasite','fanaa','kahani','hungama',
        'zero','deadpool','dangal','mowgli','baaghi','war','barfi','pk','raees','fashion','sanju,super30']

#labels
f= Label(root,text='Guess the movie-',font=('oswal',17,'bold'),bg='#f0f0f0')
f.place(x=120,y=200)
intro = Label(root,text='Welcome to HAngman game',font=('oswal',20,'bold'),bg='#f0f0f0')
intro.place(x=260,y=40)
word = Label(root,text='- - - -',font=('oswal',20,'bold'),bg='#f0f0f0')
word.place(x=220,y=270)
guesses = Label(root,text='No. of guesses:',font=('oswal',12,'bold'),bg='#f0f0f0')
guesses.place(x=160,y=340)
enter=Label(root, text="Enter your guess :",bg='#f0f0f0',font=('oswal',14,'bold'))
enter.place(x=82,y=393)
result = Label(root,text='You won!!',font=('oswal',15,'bold'),bg='#f0f0f0')
result.place(x=345,y=520)
z= Label(root,text='',font=('oswal',12,'bold'),bg='#f0f0f0')
z.place(x=365,y=550)
#entry box
inp = StringVar()
entry = Entry(root,font=('oswal',25,'bold'),relief=RIDGE,bd=3,textvariable=inp, width=3)
entry.focus_set()
entry.place(x=180,y=450)
#buttons
bt1 = Button(root,text='Enter',font=('oswal',15,'bold'),width=7,bd=4,bg='black',relief=RIDGE 
             ,fg='white',command=hangman)
bt1.place(x=260,y=450)
root.bind("<Return>",jj)
bt2 = Button(root,text='Exit',font=('oswal',15,'bold'),width=7,bd=5,bg='black',relief=RIDGE 
             ,fg='white',command=root.destroy)
bt2.place(x=460,y=595)
bt3 = Button(root,text='restart',font=('oswal',15,'bold'),width=7,bd=5,bg='black',relief=RIDGE 
             ,fg='white',command=b)
bt3.place(x=310,y=595)
#photo
image=Image.open("/Users/dell/Downloads/5.png")
photo= ImageTk.PhotoImage(image)
label=Label(image=photo)
label.place(x=590,y=150)

def chooseword():
    global picked,right,n,temp
    picked= random.choice(words)
    right = ['-' for i in picked]   
    n=5
    guesses.configure(text='No. of guesses = {}'.format(n))
    temp= picked   
    word.configure(text=right)
    result.configure(text='')
chooseword()

def chng():    
    imagepaths=[0.png, 1.png, 2.png, 3.png, 4.png, 5.png]
    photo2 = ImageTk.PhotoImage(Image.open(imagepaths[n]))
    label.config(image = photo2) 
    label.update(photo2)

root.mainloop()

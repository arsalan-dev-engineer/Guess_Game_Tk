# Tkinter guessing game
from tkinter import *
import random


window = Tk()

# Bot Generator
bot = random.randint(1, 20+1)
print(bot)


def submit():
    tries = 5
    while tries >= 0:
        e1 = (int(guessE.get()))
        if e1 == bot:
            print("You win")
            break
            
        elif e1 != bot:
            print("Try again")
            tries -= 1
            break


def clear():
    guessE.delete(0, "end")
    
    
# Guess Label
guessL = Label(window, text="Guess a number (between 1 and 20}")
guessL.place(x=75, y=50)

# Guess Entry
guessE = Entry(window, width=25, bg="lightgrey")
guessE.place(x=95, y= 80)

# Submit Button
submitBtn = Button(window, width=10, height=2, text="Submit", command=submit)
submitBtn.place(x=85, y=115)

# Clear Button
clearBtn = Button(window, width=10, height=2, text="Clear", command=clear)
clearBtn.place(x=175, y=115)


window.geometry("350x350")
window.resizable(0, 0)
window.attributes("-topmost", True)
window.mainloop()

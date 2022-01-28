# Tkinter guessing game
from tkinter import *
import random
from tkinter import messagebox

window = Tk()

# Bot Generator
bot = random.randint(1, 10+1)

# define outside of function to not overwrite each time
tries = 5


def submit():
    global tries  # to make tries a global variable
    while tries > 0:  # this matches your tries amount correctly
        e1 = (int(guessE.get()))
        if e1 == bot:
            messagebox.showinfo("Game Over", f"The number was {e1}, congratulations!")
            window.destroy()
            
        elif e1 != bot:
            print("Try again")
            tries -= 1
            break

    # print status, disable the widgets
    if tries == 0:
        print("No more tries left")
        guessE.configure(state="disabled")
        submitBtn.configure(state="disabled")
        over = messagebox.showerror("Game Over", f"The number was {e1}\nThank you for playing!")
        window.destroy()
        

# Clear function will remove entries
def clear():
    guessE.delete(0, "end")
    
    
# Guess Label
guessL = Label(window, text="Guess a number (between 1 and 10}")
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

# Window Configs
window.geometry("350x350")
window.resizable(0, 0)
window.attributes("-topmost", True)
window.mainloop()

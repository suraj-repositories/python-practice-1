from tkinter import *

def doSomething(event): # it always need a event parameter
    print("You pressed : "+ event.keysym)   # to get key symbol
    label.config(text=event.keysym)

window = Tk()

# CREATING KEY BINDINGS

# window.bind("<Return>", doSomething)    # Retrun use for Enter key
# window.bind("<q>", doSomething)     # specific key
window.bind("<Key>", doSomething)   # for all keys  

label=Label(window, font=("Helvetica",100))
label.pack()

window.mainloop()
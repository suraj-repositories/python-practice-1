from tkinter import *
from tkinter import colorchooser         # submodule

def click():
    color = colorchooser.askcolor() # it return the list of color(touple of RGB, hex_value)
    colorHex = color[1]         # we need hex value which is on second index [1]
    window.config(bg=colorHex)  # setting the window color
            # or 
    # window.config(bg=colorchooser.askcolor()[1])    # this is a shortcut for above three lines

window = Tk()
window.geometry("420x420")
button = Button(text='click me', command=click)
button.pack()
window.mainloop()

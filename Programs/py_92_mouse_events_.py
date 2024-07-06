from tkinter import *

def doSomething(event):     # it always need a event parameter
    print("Mouse cordinates : " + str(event.x) + "," + str(event.y))    #(to get the position of mouse cursor)

window = Tk()

window.bind("<Button-1>", doSomething)  # left mouse click
# window.bind("<Button-2>", doSomething)  # scroll click
# window.bind("<Button-3>", doSomething)  # right mouse click
# window.bind("<ButtonRelease>", doSomething) 
# window.bind("<Enter>", doSomething) # enter the window
# window.bind("<Leave>", doSomething) # leave the window
# window.bind("<Motion>", doSomething) # where the mouse moved



window.mainloop()
from tkinter import *

def drag_start(event):
    label.startX = event.x   # label.startX == creating attribute and setting the value
    label.startY = event.y
   

def drag_motion(event):
    # label.winfo_x() # return the x cordinate of the upper left corner of this widget in the parent 
    x = label.winfo_x() - label.startX + event.x    # formula to get new cordinate of label to be placed
    y = label.winfo_y() - label.startY + event.y
    label.place(x=x, y=y)

window = Tk()

label = Label(window, bg="red", width=10, height=5)
label.place(x=0,y=0)

label.bind("<Button-1>", drag_start)    # to start the drag which set the value  of attributes 
label.bind("<B1-Motion>", drag_motion)  # keep the drag | <B1-Motion> : represents we click and hold the button-1 which is left click


window.mainloop()
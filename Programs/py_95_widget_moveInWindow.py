from tkinter import *

def move_up(event):         # simple logic to move image
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)
def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)
def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())
def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())


window = Tk()
window.geometry("500x500")

window.bind("<w>", move_up)     # creating key bindings
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)


myimage = PhotoImage(file="images/x.png")   # creating an image and setting the image to lable
label = Label(window, image=myimage)
label.place(x=0,y=0)

window.mainloop()
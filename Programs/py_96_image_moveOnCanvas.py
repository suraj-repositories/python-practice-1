from tkinter import *

def move_up(event):         # simple logic to move image
   canvas.move(myimage,0,-10)
def move_down(event):
    canvas.move(myimage,0,10)
def move_left(event):
   canvas.move(myimage,-10,0)
def move_right(event):
   canvas.move(myimage,10,0)

window = Tk()

window.bind("<w>", move_up)     # creating key bindings
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)


canvas = Canvas(window, width=500, height=500)
canvas.pack()

photoimage = PhotoImage(file="images/x.png")
myimage = canvas.create_image(0,0,image=photoimage, anchor=NW)  # anchor notrth west is used to fix the mis-place problem

window.mainloop()
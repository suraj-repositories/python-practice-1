from tkinter import *
import time
from py_98_helping_module import Ball       # need to import as well

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,5,5,"white")  # creating many different object form a single class
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")  
basket_ball = Ball(canvas,0,0,125,6,7,"Orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
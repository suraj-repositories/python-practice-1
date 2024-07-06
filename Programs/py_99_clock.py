from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string) 
 
    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)       # to update window after 1000 millis | it is recursive call || call this method again after 1000 millis

window = Tk()

time_label = Label(window, font=("Arial",50), fg="#00ff00",bg="black")
time_label.pack()

day_label = Label(window, font=("Times New Roman",30),fg="red")
day_label.pack()

date_label = Label(window, font=("Times New Roman",30),fg="blue")
date_label.pack()

update()

window.mainloop()
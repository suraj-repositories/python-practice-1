from tkinter import *

# button = you click it, then it does stuff
count = 0

def click():
    global count
    count += 1      # creating a counter
    print("You clicked the button !")
    print("number of clicks => ", count)

window = Tk()

photo = PhotoImage(file='images/smile.png')

button = Button(window,                     # parent of this button
                text="click me",
                command=click,
                font=("Comic Sans", 30),    
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,               # state of button active or not
                image=photo,                # adding the photoimage
                compound='bottom'           # position of images relative to text
                )


button.pack()           # adding button to the window
window.mainloop()



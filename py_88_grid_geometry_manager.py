from tkinter import *

# grid() = geometry manager that organizes widgets in a table like structure in a parent

window = Tk()

titleLabel = Label(window, text="Enter Your info", font=("Arial",25)).grid(row=0, column=0,columnspan=2)

firstNameLabel = Label(window, text="First name : ", width=20, bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window, text="Last name : " ,bg="yellow").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window, text="email : " ,bg="green", width=30).grid(row=3,column=0)
emialEntry = Entry(window).grid(row=3,column=1)

submitBtn = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)

window.mainloop()
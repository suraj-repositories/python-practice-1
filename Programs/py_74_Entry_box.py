from tkinter import *

#entry widget = textbox that accepts a single line of user input 

def submit():
    name = entry.get()
    print(f"Hello {name}")
    # entry.config(state=DISABLED)  # used to add extra features on widget(if you forget something or want to do anything in certaing time)

def delete():
    entry.delete(0,END)     # (begin_index, end_index)

def backspace():
    entry.delete(len(entry.get())-1, END)  # (begin_index, end_index)

window = Tk()


entry = Entry(window,
              font=("Arial", 50),
              fg="#00FF00",
              bg="black")

# entry.insert(0, "default value")        # add default value in entry box (positioal argument , string) 0 for begining
entry.config(show="*")      # used to add extra features on widget(if you forget something or want to do anything in certaing time)

entry.pack(side=LEFT)       # adding in window and setting the position of entry

submit_btn = Button(window, text="submit", command=submit)
submit_btn.pack(side=RIGHT)     # adding in window and setting the position of btn

delete_btn = Button(window, text="delete", command=delete)
delete_btn.pack(side=RIGHT)

backspace_btn = Button(window, text="backspace", command=backspace)
backspace_btn.pack(side=RIGHT)

window.mainloop()
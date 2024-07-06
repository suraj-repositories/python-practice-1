from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir=".",   # for defalt directory to open( dot represents our project folder in which this file is stored)
                                          title="Open file Okey?",      # we can change the title
                                          filetypes=(("text files", "*.txt"),   # we can set filter for files
                                            ("all files","*.*")))

    file = open(filepath, 'r')      # r -> read | rw -> readwrite | rb -> read binary
    print(file.read())
    file.close()

window = Tk()

button = Button(text="Open", command=openFile)
button.pack()
window.mainloop()
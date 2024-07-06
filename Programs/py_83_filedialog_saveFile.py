from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir=".",     # setting the default directory
                                    defaultextension='.txt',    # default extension of file to be save
                                    filetypes=[                 # list the filetypes in which extensions you want to save your file
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                    ])

    if file is None:    # To handle the exception if user cancel to choose location or name or cut the savedialog 
        return

    filetext = str(text.get(1.0,END))   # getting the text and typecasting as a string 
    filetext=input("Enter some text : ")    # use this if you want to use console
    file.write(filetext)                # writeing the text in file
    file.close()    

window = Tk()

button = Button(text="Save", command=saveFile)
button.pack()

text = Text(window)     # creating textarea
text.pack()

window.mainloop()
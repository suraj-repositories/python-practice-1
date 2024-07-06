from tkinter import *

def openFile():
    print("file opened")
def saveFile():
    print("file saved ")
def cut():
    print("you cut some text")
def copy():
    print("You copy the text")
def paste():
    print("you paste the text")

window = Tk()

openImage = PhotoImage(file="images/folder.png")
saveImage = PhotoImage(file="images/save.png")
exitImage = PhotoImage(file="images/x.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile,image=openImage, compound='left')
fileMenu.add_command(label="Save", command=saveFile,image=saveImage, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit,image=exitImage, compound='left')

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)


window.mainloop()
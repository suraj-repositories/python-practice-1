# radio buttons : similar to checkbox, but you can only select one from a group
from tkinter import *

def order():
    if(x.get()==0):
        print("You are happy")
    elif(x.get()==1):
        print("You are crying")
    elif(x.get()==2):
        print("You looks wierd")
    else:
        print("heh?")

faces = ["smile", "cry", "dizzy"]

window = Tk()

x = IntVar()

smileImg = PhotoImage(file='images/smile.png')
cryImg = PhotoImage(file='images/cry.png')
dizzyImg = PhotoImage(file='images/dizzy.png')
faceImgs = [smileImg, cryImg, dizzyImg]


for index in range(len(faces)):
    radio_btn = Radiobutton(window,
                             text=faces[index], # adds text to radio button
                             variable=x,    # group radiobuttons together if they share the same variable
                             value=index,   # assign each radio buttons a different values
                             padx=25,
                             font=('Impact',25),
                             image=faceImgs[index], # add image to the radio btn
                             compound='left',   # adds image & text(left side)
                             indicatoron=0,     # eliminate circle indicators
                             width=300, # set width of radio btns
                             command= order # set command of radiobutton to function
                            )

    radio_btn.pack(anchor=W)    # anchor to the west(W or 'w')

window.mainloop()
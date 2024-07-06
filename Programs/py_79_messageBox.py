from tkinter import *
from tkinter import messagebox  # importing messagebox library

def click():
    # messagebox.showinfo(title='This is an info message box', message="You are a person")
    # messagebox.showwarning(title="WARNING!", message="You have a VIRUS!!!!!")
    # messagebox.showerror(title="ERROR!", message="Something went wrong!!!")

    # ----------------------------------------------------------------------------------------------

    if messagebox.askokcancel(title='ask ok cancel', message='Do you want to do the thing?', icon='info'):
        print("You did the thing")
    else:
        print("You canceled the thing :(")
   

    # ----------------------------------------------------------------------------------------------

    # if messagebox.askretrycancel(title='ask retry cancel', message='Do you want to retry the thing?', icon='warning'):
    #     print("You retried the thing")
    # else:
    #     print("You canceled the thing :(")


    # ----------------------------------------------------------------------------------------------

    # if messagebox.askyesno(title='ask yes or no', message='Do you like cake?', icon='error'):
    #     print("I like cake too :)")
    # else:
    #     print("whay do you not like cake :(")


    # ----------------------------------------------------------------------------------------------

    # answer = messagebox.askquestion(title='ask question', message='Do you like pie?')   # this will returns yes or no
    # if(answer == 'yes'):
    #     print('I like pie too')
    # else:
    #     print("why do you not like pie?")

    # ----------------------------------------------------------------------------------------------

    # answer = messagebox.askyesnocancel(title='yes no cancel', message='Do you like to code?')
    # if(answer==True):
    #     print("you like the code")
    # elif(answer==False):
    #     print("Then why are you see this program")
    # else:
    #     print("You dotch the question ")


window = Tk()

button = Button(window, command=click, text='click me')
button.pack()

window.mainloop()
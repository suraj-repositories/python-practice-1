from tkinter import *

def display():
    if(x.get()==1):     # getting the value of variable which we set in constructor and using as a conditional
        print("You are not a robot")
    else:
        print("You are roude")

window = Tk()

x = IntVar()        # setting the datatype of the variable so we can use this in any function
# x = BooleanVar()
# x = StringVar()

photo = PhotoImage(file='images/play.png')

check_btn = Checkbutton(window, 
                        text="I am not a robot", 
                        variable=x,         # adding the state variable to find the state of check button
                        onvalue=1,          #onvalue=True       #onvalue="YES"
                        offvalue=0,         #offvalue=False     #offvalue="NO"
                        command=display,    # to execute any function use command argument
                        font=('Arial',20),
                        fg='#00FF00',
                        bg='black',
                        activeforeground='#00FF00',     # onclick forground
                        activebackground='black',
                        padx=25,
                        pady=10, 
                        image=photo,
                        compound=LEFT)              # set image in right place relatively to text

check_btn.pack()

window.mainloop()

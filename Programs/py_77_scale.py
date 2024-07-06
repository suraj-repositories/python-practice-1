from tkinter import *

def submit():
    print("The temprature is " + str(scale.get()) + " degrees C")

window = Tk()

googleImg = PhotoImage(file='images/google.png')
googleLabel = Label(image=googleImg)
googleLabel.pack()


scale = Scale(window,
              from_=100, 
              to=0,
              length=500,
              orient=VERTICAL,   # orientation of scale
              font=('Consolas', 20),
              tickinterval=10,   # adds numeric indicator for value
            #   showvalue=0,    # hide the current value
              resolution=5, # increment of slider
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111'
              )

# scale.set(50)
scale.set(((scale['from']-scale['to'])/2)+scale['to'])  # set current value of slider

scale.pack()

facebookImg = PhotoImage(file='images/facebook.png')
facebookLabel = Label(image=facebookImg)
facebookLabel.pack()

button = Button(window,
                 text='submit',
                 command=submit
                 )


button.pack()

window.mainloop()
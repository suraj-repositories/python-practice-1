from tkinter import *

# label : an area widget that holds text and/or an image within a window

window = Tk()   # instantiate an instance of a window

photo = PhotoImage(file='images/play.png')

label = Label(window,
              text="Let's play",
              font=('Arial', 40, 'bold'),
              fg='#00FF00' ,    # forground/text_color
              bg='black',       # background color
              relief=RAISED,    # border style
              bd=10,            # border width
              padx=20,          # padding x 
              pady=20,          # padding y
              image=photo,      # add image
              compound='bottom' # add relative position of image relative with text
              )

# more than one way are available to add lable in window

label.pack()        # by using pack method
# label.place(x=0,y=0)  # using place -- this will set label in specific location

window.mainloop()   # place window on computer screen, listen for events
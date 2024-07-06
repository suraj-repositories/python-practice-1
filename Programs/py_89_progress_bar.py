from tkinter import *
from tkinter.ttk import *       # important import submodule
import time

def start():

    MB = 500        # creating variable which we are going to use
    download = 0
    speed = 5

    while(download < MB):
        time.sleep(0.05)                # time for update
        bar['value']+=(speed/MB)*100        # setting the speed(steps) of the bar
        download += speed   

        percent.set(str(int((download/MB)*100))+"%") # displaying the percentage downloaded
        text.set(str(download)+"/"+str(MB)+" tasks completed")  #show how many tasks complete

        window.update_idletasks()       # to update window in each iteration of while loop

window = Tk()

percent = StringVar()   # deciding the datatype of text variable (creating text variable)
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)    # creating a progressbar
bar.pack(pady=10)       # set some padding on y axis

percentLabel = Label(window, textvariable=percent).pack()   # creating a percent label with text variable
textLabel = Label(window, textvariable=text).pack()

button = Button(window, text="download", command=start).pack()

window.mainloop()
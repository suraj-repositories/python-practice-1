from tkinter import *
import time

WIDTH = 500     # constants for program
HEIGHT = 500
xVelocity = 4
yVelocity = 3

window = Tk()

canvas = Canvas(window,width=WIDTH, height=HEIGHT)  # creating canvas
canvas.pack()

background_photo = PhotoImage(file="images/snake.png")  # creating and setting background image
background = canvas.create_image(0,0,image=background_photo, anchor=NW)

photo_image = PhotoImage(file="images/play.png")    # creating an image to move
my_image = canvas.create_image(0,0,image=photo_image, anchor=NW)

image_width = photo_image.width()       # getting the dimenstions of image
image_height = photo_image.height() 

while True:
    coordinates = canvas.coords(my_image)   # getting the corrds of image to move
    print(coordinates)  # printing the corrds

    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):    # checking the condition the image touch the borders
        xVelocity = -xVelocity  # if yes change the following values
    
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):  # same for y axis
        yVelocity = -yVelocity

    canvas.move(my_image, xVelocity,yVelocity)      # moving the image on canvas
    window.update()     # updateing the window
    time.sleep(0.01)    # refresh rate (speed of animation)


window.mainloop()
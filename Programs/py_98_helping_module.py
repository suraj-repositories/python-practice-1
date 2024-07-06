# we are useing class as a template 

class Ball: # creating a class who help the main animations module

    def __init__(self, canvas, x, y, diamether, xVelocity, yVelocity, color):   # init functions to initialise values which are come from second module
        self.canvas= canvas
        self.image = canvas.create_oval(x,y,diamether,diamether,fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity


    def move(self): # creating a move method same as single animations 
        coordinates = self.canvas.coords(self.image)
        # print(coordinates)

        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVelocity = -self.xVelocity
        
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image, self.xVelocity, self.yVelocity)
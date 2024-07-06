
# super() : Function used to give access to the method of a parent class.
#           Return a temporary object of a parent class when used

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
    

class Squre(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)
    
    def area(self):
        return self.length* self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length* self.width * self.height



squre = Squre(4, 3)
cube = Cube(4, 3, 2)

print(squre.area())
print(cube.volume())

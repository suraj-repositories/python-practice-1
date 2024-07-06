class Car:
    wheels = 4      # class variables

    def __init__(self, make, model, year, color) :
        self.make = make    # instance variables
        self.model = model
        self.year = year
        self.color = color
    
from py_44_classVariables import Car

print("Wheel in car class = " , Car.wheels)       # we can use class variables without creating object 

car1 = Car("Chevy", "Corvette", 2021, "blue")
car2 = Car("Ford", "Mustang", 2022, "red")



# car1.wheels = 6     # we can change value of class variables for specific object
Car.wheels = 3      # Or we whill change there value for all objects


print(car1.model)
print(car1.wheels)

print(car2.model)
print(car2.wheels)

print()


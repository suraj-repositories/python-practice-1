
class Car:

    color = None

class Motercycle:

    color = None

def change_color(vehical, color):       # seperate function to set the color 
    vehical.color = color

car_1 = Car()
car_2 = Car()
bike = Motercycle()

# print(car_1.color)
# print(car_2.color)
# print(bike.color)

change_color(car_1, "red")      # by using function setting the value of color
change_color(car_2, "blue")
change_color(bike, "yellow")

print(car_1.color)
print(car_2.color)
print(bike.color)

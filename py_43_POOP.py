from py_43_CarModule import Car

car1 = Car("Chevy", "Corvette", 2021, "blue")
car2 = Car("Ford", "Mustang", 2022, "red")

print(car1.make, end=" - ")
print(car1.model, end=" - ")
print(car1.year, end=" - ")
print(car1.color)

print(car2.make, end=" - ")
print(car2.model, end=" - ")
print(car2.year, end=" - ")
print(car2.color)
print()

car1.drive()
car1.stop()
print()
car2.drive()
car2.stop()
# Prevent a user from creating an object of class
# + copels/force a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod

class Vehical(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehical):
    
    def go(self):
        print("The car starts moving")

    def stop(self):
        print("the car is stoped")


    

class Motercycle(Vehical):
    
    
    def go(self):
        print("The motercycle starts moving")

    def stop(self):
        print("the motercycle is stoped")

car = Car()
motercycle = Motercycle()


car.go()
car.stop()

motercycle.go()
motercycle.stop()
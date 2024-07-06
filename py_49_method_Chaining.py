
# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and return self


class Car:
    
    def turn_on(self):
        print("You turn on the engine")
        return self

    def drive(self):
        print("You drive the car ")
        return self
    
    def stop(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

# car.turn_on()
# car.drive()

# car.turn_on().drive()
# car.stop().turn_off()

# car.turn_on().drive().stop().turn_off()

# \ is continue line character  | that is more readable
car.turn_on()\
    .drive()\
    .stop()\
    .turn_off()
# logical operators = used on conditional statements

#     and = checks two or more conditional if True
#      or = checks if at least one condition is True
#     not = True if condition is False, and vice versa 

temp = 25

# and -------------------------------------------------
if temp > 0 and temp < 30:
    print("The temprature is good")
else:
    print("The temprature is bad")

# or --------------------------------------------------
if temp <= 0 or temp >= 30:
    print("The temprature is bad")
else:
    print("The temprature is good")

# not -------------------------------------------------
sunny = True

if not sunny:
    print("It is cloudy outside")
else :
    print("It is sunny outside")
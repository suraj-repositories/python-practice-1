# Exception = events detected during execution that interrupt the flow of a program

print("Example program on Exception Handling")


try:
    numerator = int(input("Enter a number ot devide : "))
    denominator = int(input("Enter a number to divide by : "))
    result = numerator / denominator
except ZeroDivisionError as e:      
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError:                  # e is not necessory
    print("Enter only number please")
except Exception as e:
    print("something went wrong :(")
else:                               # it execute when no exception occure
    print(f"Result : {result}")
finally:
    print("Finally will always execute")


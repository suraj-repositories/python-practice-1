# Higher Order Function = a function that either:
#                         1. accept a function as an argument
#                             or
#                         2. return a function
#                         (In python, functions are also treated as objects)

# 1)
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

# 2)
def divisor(x):
    def divident(y):
        return y / x
    return divident

divide = divisor(2)     # assigning memory address of divident funtion which is returned by devisor function to devide 
print(divide(10))
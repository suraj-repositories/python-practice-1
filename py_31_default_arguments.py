# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces number of arguments
#                     1. positional, 2.DEFAULT, 3.keyword, 4.arbitrary


def net_price(list_price, discount=0, tax=0.05):        # we are able to set the default value of parameter
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))           # one argument 
print(net_price(500,0.1))       # two
print(net_price(500,0.1,0))     # three 

# ------------------- Exercise ---------------------

# import time

# def count(end, start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("--- BOOM ---")

# # count(10)
# count(10,5)


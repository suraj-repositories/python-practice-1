# ARBITARY ARGUMENTS -------- important

# *args   = allows you to pass multiple non-key arguments (it accept the argument as a touple)
# **kwargs = allows you to pass multiple keyword-arguments (it accept the argument as a dictionary)
#                 * unpacking operator
#                 1. positional 2. default 3.keyword 4.ARBITARY

# 1) *args
# ---------------- Example -------------------

def add(*args):
    total = 0 
    for arg in args:
        total += arg
    return total

print(add(1))
print(add(1,2,3))       # you can pass any number of arguments
print(add(1,2,3,4,5))

# ---------------- Example -------------------

def display_name(*words):
    for word in words :
        print(word, end=" ")

display_name("Dr.", "shubham", "kumar" , "maurya")
print()


# 2) **kwargs
# ---------------- Example -------------------

def print_addresses(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    # for key in kwargs.keys():
    #     print(key)   
    # for value in kwargs.values():
    #     print(value) 

print_addresses(street = "ratanpur colony",             # they are the keyword arguments see previous practice for better understanding
                city = "Kanpur",
                state = "UP",
                zip = "208020")


# ---------------- Example -------------------
print("---------------------------")
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('streat')}")
    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('state')}")
    print(f"{kwargs.get('zip')}")

shipping_label("Dr.", "Shubham" , "kumar", 
                streat = "Rantanpur colony",
                city = "Kanpur",
                State = "UP",
                zip = "208020")

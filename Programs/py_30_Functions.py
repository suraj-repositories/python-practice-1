# function = A block of reusable code
#             place () after the function name to invoke it

# return = statement used to end a function 
#             and send a result back to the caller

def create_name(first, last):                   # matching set of parameters
    first = first.capitalize()
    last = last.capitalize()    
    return first + " " + last

full_name = create_name("shubham", "kumar")         # arguments

print(full_name)
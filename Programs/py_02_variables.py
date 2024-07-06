# variables : a reusable container for storing a Value
#             a variable behaves as if it were the value it contains

age = 23;

print("You are " + str(age) + " years old.");
print("You are", age , "years old.");
print(f"You are {age} years old.");     # f-strings


# different datatypes in python --------------------------------------------

id = 101;
gpa = 3.3;
name = "shubham";
driving = False;

print(f"{id} , {gpa} , {name} , {driving}");

# tips and tricks -----------------------------------------------------------

  # multiple assignment

# x = 1;
# y = 2;
# z = 3;
x, y, z = 1, 2, 3;      # same as before  
print(f"x = {x} , y = {y} , z = {z}");

a = b = c = 0;
print(f"a = {a} , b = {b} , c = {c}");

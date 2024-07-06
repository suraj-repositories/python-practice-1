# typecasting : The process of converting a value of one data type to another
#                 (string, integer, float, boolean)
#                 Explicit vs Implicit

name = "shubham";
age = 21;
gpa = 3.4;
student = True;

print(type(name));

# Explicit Typecasting 

age = float(age);
print(type(age));

gpa = int(gpa);
print(type(gpa));

student = str(student);
print(type(student) , "student =",student );

age = bool(age);
print(type(age), "age :" , age);


# implicit typecasting

x = 2;
y = 2.0;

print(type(x));

x = x / y;
print("x :" , x , " ", type(x));



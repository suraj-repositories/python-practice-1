# while loop = execute some code while some condition remains true

name = input("Enter Your name : ")

while name == "":
    print("You did not enter your name")
    name = input("Enter Your name : ")

print(f"hello {name}")

# collection = single "variable" used to store multiple values
#     List    =   []  ordered and changeable. Duplicates OK
#     Set     =   {}  unordered and immuteable, but Add/remove OK. No duplicates
#     Tuple   =   ()  ordered and unchageable.Duplicates OK. FASTER


# -------------------------- List -----------------------------------

fruits = ["apple","orange","banana","coconut"]    

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)
# print("pineapple" in fruits)
# print(fruits[0])

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0,"pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("pineapple"))

# for fruit in fruits:
#     print(fruit)


# -------------------------- set -----------------------------------

fruits = {"apple","orange","banana","coconut"}

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()

# -------------------------- tuple -----------------------------------
fruits = ("apple","orange","banana","coconut","coconut")  

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits.index("apple"))
# print(fruits.count("coconut"))

# for fruit in fruits:
#     print(fruit)
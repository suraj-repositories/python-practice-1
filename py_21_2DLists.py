
# list of lists is called 2D
# list of tuples or set or lists is allowed
# set of lists or tuples or sets is allowed
# tuple of lists or sets or tuples is allowed


fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["onions", "carrot", "potatos"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

# groceries = [["apple", "orange", "banana", "coconut"]
#             , ["onions", "carrot", "potatos"]
#             , ["chicken", "fish", "turkey"]]

# print(groceries)
# print(groceries[0])
# print(groceries[1][1])

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

# ---------------------- Exercise ------------------------
# printing the keypad of phone

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
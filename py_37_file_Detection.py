import os

# path = "E:\\Python\\DemoFolder"
# path = "E:\\Python\\DemoText.txt"
# path = "DemoFolder"
path = "DemoText.txt"


if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a folder")
else:
    print("That file doesn't exists")
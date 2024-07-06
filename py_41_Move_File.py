import os

# THIS WILL WORK WITH FOLDERS TOO   EX.     documents/folder

source = "documents/moveTest.txt"
destination = "E:\\Python\\DemoFolder\\moveTest.txt"
# you can rename the file at the time of move
# CHANGE THE desination to src and src to destination to move file back

try:
    if not os.path.exists(source):
        print(source + " not found")
    elif os.path.exists(destination):     # check the file is already exists or not 
        print("There is already a file exists")
    else:
        os.replace(source, destination)     # moveing the file
        print(source + " was moved")

except FileNotFoundError :
    print(source +  " was not found")

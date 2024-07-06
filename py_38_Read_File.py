

try:
    with open('DemoText.txt') as file:
        print("---------------------------------------")
        print(file.read())
        print("---------------------------------------")
        print(f"file closed : {file.closed}")
except FileNotFoundError:
    print("That file not found in given location")

print(f"file closed : {file.closed}")
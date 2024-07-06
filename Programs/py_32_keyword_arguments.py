# keyword arguments = an argument preceded by an identifier
#                     helps with readability 
#                     order of arguments does't matter
#                     1. positional, 2.DEFAULT, 3.keyword, 4.arbitrary


# 1)

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("hello" , last="kumar", title="mr." , first="Shubham")

# 2)
for x in range(1,11):
    print(x, end=" ")                   # end is also a keyword argument

# 3)
print("1", "2", "3", "4", "5", sep="-")     # sep is also a keyword argument

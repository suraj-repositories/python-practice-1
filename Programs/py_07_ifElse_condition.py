# if : Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age : "))

# if-else -------------------------------------------------------------

# if age >= 18:
#     print("eligible for vote")
# else: 
#     print("must be 18+ for vote")

# if-else ladder -----------------------------------------------------

if age >= 18:
    print("eligible for vote")
elif age<=0:
    print("you have not been born yet")
elif age>100:
    print("you are very old to vote")
else: 
    print("must be 18+ for vote")

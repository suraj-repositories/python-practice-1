# format specifiers = {value:flags} format a value on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocates that many spaces 
# :03 = allocates and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align 
# :+ = use to plus sign to indicate positive Value
# := = place sign to leftmost position 
# : = insert a space before positive numbers 
# :, =  comma seperator 


price1 = 3.14159
price2 = -987.65
price3 = 23.56

# print(f"Price 1 is ${price1:.3f}")
# print(f"Price 2 is ${price2:.2f}")
# print(f"Price 3 is ${price3:.2f}")

# print(f"Price 1 is ${price1:10}")
# print(f"Price 2 is ${price2:10}")
# print(f"Price 3 is ${price3:10}")

# print(f"Price 1 is ${price1:010}")
# print(f"Price 2 is ${price2:010}")
# print(f"Price 3 is ${price3:010}")

# print(f"Price 1 is ${price1:<10}")
# print(f"Price 2 is ${price2:<10}")
# print(f"Price 3 is ${price3:<10}")

# print(f"Price 1 is ${price1:>10}")
# print(f"Price 2 is ${price2:>10}")
# print(f"Price 3 is ${price3:>10}")

# print(f"Price 1 is ${price1:^10}")
# print(f"Price 2 is ${price2:^10}")
# print(f"Price 3 is ${price3:^10}")

# print(f"Price 1 is ${price1:+}")
# print(f"Price 2 is ${price2:+}")
# print(f"Price 3 is ${price3:+}")

# print(f"Price 1 is ${price1: }")
# print(f"Price 2 is ${price2: }")
# print(f"Price 3 is ${price3: }")

# print(f"Price 1 is ${price1:,}")
# print(f"Price 2 is ${price2:,}")
# print(f"Price 3 is ${price3:,}")

# print(f"Price 1 is ${price1:+,.3f}")
# print(f"Price 2 is ${price2:+,.2f}")
# print(f"Price 3 is ${price3:+,.2f}")

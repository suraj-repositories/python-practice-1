# indexing = accessing elements of a sequense using [] (indexing operator)
#             [start : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[0:4])
# print(credit_number[:4])        # default starting point is 0
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])        # index from last
# print(credit_number[-6])
# print(credit_number[::2])       # every second character
# print(credit_number[::3])       # every third character


last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")


# ----------------------- reverse a strign --------------------------------------
credit_number = credit_number[::-1]
print(credit_number)
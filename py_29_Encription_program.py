import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters  # creating a char set for encription
chars = list(chars)     # creating a list of characters
key = chars.copy()      # creating a copy as key | it will need when we want to decript the message

random.shuffle(key)     # shuffleing the keys so anybody can't decode it easily

# print(f"chars : {chars}")
# print(f"key : {key}")

# ENCRIPT
plain_text = input("Enter a message to encript : ")     # input message
cipher_text = ""                                        # currently cipher text is an empty string

for letter in plain_text:               # encodeing
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypted message : {cipher_text}")


# DECRIPT
cipher_text = input("Enter a message to decript : ")
plain_text = ""

for letter in cipher_text:              # decodeing
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message : {cipher_text}")
print(f"original message : {plain_text}")
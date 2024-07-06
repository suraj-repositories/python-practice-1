# zip(*iterables) = aggregates elements from two or more iterables (list, tuples, sets , etc.)
#                   creates a zip object with paired elements stored in tuples for each elements

usernames = ["Shubham", "Tushar", "Vaibhav"]
password = ("p@ssword", "abc123", "guest")

# ------------------------------------------------------------------------
# users = zip(usernames, password)

# print(type(users))

# for i in users:
#     print(i)
# ------------------------------------------------------------------------

# users = dict(zip(usernames, password))  # we can simply typecast zip object to any type of iterable object -- dict, list, tuple, set 

# print(type(users))
# for key, value in users.items():
#     print(key + " : " + value)

# ------------------------------------------------------------------------

login_date = ["1/1/2021","1/2/2021","1/3/2021"]

users = zip(usernames, password,login_date)

for i in users :
    print(i)

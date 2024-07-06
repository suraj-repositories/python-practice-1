import time

# print(time.ctime(0))    # convert a time expressed in second since epoch to a readable string 
                        # epoch = when your computer thinks time began (reference point)

# practice
# print(time.ctime(1000000000))

# print(time.time())      # return current seconds since epoch

# print(time.ctime(time.time()))  # for the current time

# time_object = time.localtime()      # localtime object
# time_object = time.gmtime()
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# time_string = "20 April, 2020"
# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)

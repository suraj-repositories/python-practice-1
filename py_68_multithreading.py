
# thread = a flow of execution. Like a separate order of instructions.
#             However each thread takes a turn running to achieve concurrency
#             GIL = (global interpreter lock)
#             allows only one thread to hold the control of the Python interpreter at any one Time

# cpu bound = program /task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing 

# io bound = program/task spends most of it's itme waiting for external events(user input, web scraping)
#             use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drinking coffee")

def study():
    time.sleep(5)
    print("completing homework in the last-moment")

x = threading.Thread(target=eat_breakfast, args=())         # creating thread 
x.start()

y = threading.Thread(target=drink_coffee, args=())          # creating thread
y.start()

z = threading.Thread(target=study, args=())                 # creating thread
z.start()

x.join()    # by using join method the main thread wait for these threads and when they complete there execution then main thread execute
y.join()
z.join()


# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count())     # how many thread are running concurrently
print(threading.enumerate())    # to see the name's of the treads
print(time.perf_counter())      # how much time takes by main thread to complete
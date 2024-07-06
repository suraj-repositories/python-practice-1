# daemon thread = a thread that runs in the background, not important for program to run 
#                 your program will not wait for daemon threads to  complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete 

#                 ex. background tasks, garbage collection, waiting for input, long running processes
            
import threading
import time

def timer():
    print("\n")
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for : ", count , "seconds")

x = threading.Thread(target=timer, daemon=True)

# x.setDaemon(True)

x.start()
print(x.isDaemon())

answer = input("Enter any string to exit : ")
print("---------------")
print(answer)

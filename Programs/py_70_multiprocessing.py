# *************************
# Python multiprocessing
# *************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):   # creating a counter program
    count = 0
    while count < num:
        count +=1

def main():
    
    print(cpu_count())  # for cpu core count

    a = Process(target=counter, args=(10000000, ))      # creating a process
    b = Process(target=counter, args=(10000000, ))
    
    a.start()
    b.start()

    a.join()    # for synchronization
    b.join()

    print("finished in : ", time.perf_counter(), "seconds")


if __name__ == '__main__':      # if using window use this for better result
    main()
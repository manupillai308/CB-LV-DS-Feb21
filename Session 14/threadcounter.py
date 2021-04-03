from threading import Thread
import time
import random

thread_end_time = []

def print_times():
    # thread_counter = 0
    while True:
        if len(thread_end_time) > 0:
            _time = thread_end_time.pop(0)
            if(_time == "exit"):
                break
            print(*_time, sep="->")
            # thread_counter += 1
        # if thread_counter >= 10:
            # break
        

def func(thread_name, start_time):
    start_time = time.time()
    time.sleep(random.randint(3, 8))
    thread_end_time.append((thread_name,"%.2fs" %(time.time()-start_time)))

threads = []
for i in range(10):
    thread = Thread(target=func, args=(f'Thread {i+1}', time.time()))
    threads.append(thread)

time.sleep(2)

for thread in threads:
    thread.start()
    # thread.join()

printer = Thread(target=print_times)

printer.start()

for thread in threads:
    thread.join()

thread_end_time.append("exit")

# print(*thread_end_time, sep="\n")




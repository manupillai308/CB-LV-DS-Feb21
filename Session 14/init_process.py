from multiprocessing import Process
import time
import random


process_end_time = []

processes = []

def func(process_name, start_time):
    print(f"Process {process_name} started")
    start_time = time.time()
    time.sleep(random.randint(3, 8))
    process_end_time.append((process_name,"%.2fs" %(time.time()-start_time)))
    print(f"Process {process_name} ended")


if __name__ == "__main__":
    for i in range(10):
        process = Process(target=func, args=(f'Process {i+1}', time.time()))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    # print(*process_end_time, sep="\n")
    print(len(process_end_time))




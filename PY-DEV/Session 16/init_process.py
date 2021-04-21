from multiprocessing import Process, Queue, Value
# from queue import Queue
import time
import random



def func(process_name, start_time, process_end_time, flag=False):
    print(f"Process {process_name} started")
    start_time = time.time()
    time.sleep(random.randint(3, 8))
    process_end_time.put(process_name + " - %.2fs" %(time.time()-start_time))
    print(f"Process {process_name} ended")
    # if flag != None:
    # if flag:
        # flag.value = 0
        # process_end_time.put("Quit")

if __name__ == "__main__":
    process_end_time = Queue()
    # flag = Value("i", 1)
    processes = []

    for i in range(10):
        args = (f'Process {i+1}', time.time(), process_end_time)
        if i == 9:
            args = args + (True,)
        process = Process(target=func, args=args)
        processes.append(process)

    for process in processes:
        process.start()

    # for process in processes:
    #     process.join()

    # print(*process_end_time, sep="\n")
    # print(len(process_end_time))

    # while flag.value == 1 or not process_end_time.empty():
    # while True:
    while any([p.is_alive() for p in processes]):
        try:
            data = process_end_time.get(block=False)
        except Exception:
            continue
        # if data == "Quit":
            # break
        # else:
            # print(data)
        print(data)



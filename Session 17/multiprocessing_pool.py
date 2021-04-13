from multiprocessing import Pool
import time
import random
import os



def func(i):
    print(f"Child no {i} called")
    time.sleep(random.randint(1, 5))
    print(f"Child no {i} finished")

    return f"{i} finished"


def child_pid(i):
    print(f"pid of child {i} called {os.getpid()}")
    time.sleep(random.randint(1,3))

if __name__ == "__main__":
    pool = Pool(processes=3)
    # result = pool.map(func, (1,2,3,4,5))
    pool.map(child_pid, (1,2,3,4,5))
    # print(result)

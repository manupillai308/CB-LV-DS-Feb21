from threading import Thread, Lock
import time


l = []


def printer():

    while len(l) > 0:
        print(l.pop(0))


def number_generator():
    data = "sdasdakdjlskdjalkdjlakjdlaskjdlkajd"
    l.append(data)


thread1 = Thread(target=number_generator)
thread2 = Thread(target=number_generator)
thread3 = Thread(target=printer)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
print("hey")
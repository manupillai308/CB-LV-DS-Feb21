import threading
import time
import sys

# can_i_print = True

def multiple_print():
    # global can_i_print

    # while can_i_print == False:
        # pass
    # can_i_print = False
    can_i_print.acquire() #blocking call unless blocking = False is passed
    for i in "Manu S Pillai":
        print(i, end="")
        sys.stdout.flush()
        time.sleep(1)
    print()
    can_i_print.release()
    # can_i_print = True
    time.sleep(10)


thread1 = threading.Thread(target=multiple_print)
can_i_print = threading.Lock()

thread1.start()
# thread1.join()
time.sleep(1.5)
multiple_print()
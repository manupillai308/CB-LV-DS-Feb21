import threading
import time


var = "Python"

def print_var():
    while True:
        print(var)
        if var == '':
            return
        time.sleep(1)

thread = threading.Thread(target=print_var)

# print_var()
thread.start()
print("After function calling")
var = input()

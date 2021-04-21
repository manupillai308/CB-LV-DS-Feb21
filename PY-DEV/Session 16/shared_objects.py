from multiprocessing import Process, Value, Array

# class Value:
#     def __init__(self, type, value):
#         self.value = value

def changeVar(var, arr):
    # var.value = 20
    arr[1] = 10
    return


if __name__ == "__main__":
    var = Value("f", 10.2)
    arr = Array("i", 10)
    p = Process(target=changeVar, args=(var,arr))
    # print("Value of var in main:", var.value)
    print("Value of arr in main:", list(arr))
    p.start() # Different process
    p.join()
    # changeVar(var) # Within same process
    # print("Value of var in main after child:", var.value)
    print("Value of arr in main after child:", list(arr))
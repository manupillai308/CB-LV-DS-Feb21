import os

# os.spawnv(os.P_NOWAIT, "C:/Users/Manu/AppData/Local/Programs/Python/Python36/python.exe", ("python", "./child.py"))


print(os.getpid())
os.execl("C:/Users/Manu/AppData/Local/Programs/Python/Python36/python.exe", "python", "./child.py")
print("Hey from Parent")

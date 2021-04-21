import os
import sys

# print("Parent:",os.getpid())

# sys.stdout = open("./Session 15/myfile.txt", "w")
# os.system(f'tasklist /FI "PID eq {os.getpid()}"')
# print("Manu")

res = os.spawnv(os.P_NOWAIT, "C:/Users/Manu/AppData/Local/Programs/Python/Python36/python.exe", ("python", "./child.py"))
print("From Parent")
#necessary works
print(os.waitpid(res, 1000))
# print(res)


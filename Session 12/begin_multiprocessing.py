import os

# os.system('echo manu')

print("Calling subprocess")
val = os.system('python myprogram.py')   #blocking

if val == 0:
    print("Subprocess exited sucessfully")
else:
    print("Subprocess exited with error")
# os.system('python') 


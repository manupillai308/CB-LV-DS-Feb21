import os


pid = os.fork()

if pid == 0:
    print("Hey from Child")
else:
    print("Hey from Parent, say hi to my child with id", pid)

if pid == 0:
    pid = os.fork()
import sys

try:
    a, b = list(map(int, input("Enter 2 numbers:").split(" ")))
except:
    sys.exit(-1)

print("Sum is:", a+b)

sys.exit(0)

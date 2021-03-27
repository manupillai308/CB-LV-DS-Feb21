# a = int(input())
# b = int(input())
import sys

try:
    filename = sys.argv[0]
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except IndexError:
    print("Please provide values for both numbers to be added.")
    exit()

# print(type(sys.argv))
# print()
# print(sys.argv)
# print()


print("Sum is:", a+b)
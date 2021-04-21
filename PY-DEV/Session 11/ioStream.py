import sys

f_out = open("./Session 11/myoutput.txt", "w")
f_in = open("./Session 11/myinput.txt")
f1, f2, f3 = sys.stderr, sys.stdin, sys.stdout

sys.stdout = f_out
sys.stdin = f_in


# print(type(f1), type(f2), type(f3))
# print(f1, f2, f3)
# print(dir(sys))

def custom_print(*args, sep=" ", end="\n"):
    for arg in args:
        sys.stdout.write(arg.__str__() + sep)
    
    sys.stdout.write(end)
    

# print("Hey there!")
# f3.write("Hey there!")

# custom_print(10, 20, 30, "Manu")
# '10 20'

# l = input().split(" ")
# l = list(map(int, l))
# a, b = l

a,b = list(map(int, input().split(" ")))
# print(10, 20, 30, "Manu")

print(a+b)

f_out.close()
f_in.close()
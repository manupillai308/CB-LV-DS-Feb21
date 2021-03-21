def factorial(n):
    fact = 1

    for i in range(1, n+1):
        fact *= i
    
    return fact

class ABCDEFGHIJKL:
    def my_function():
        print("I m from module1")


var = "I m in module1"


# __all__ = ['factorial', 'ABC', 'var']

# print(factorial(10))



from math import factorial

class calculator:
    def add(x, y):
        return x + y
    
    def factorial(x):
        return factorial(x)

    def sin(x, N):
        a1 = 0
        for n in range(0, N+1):
            a = (((-1)**n)*(x**(2*n+1)))/(factorial(2*n+1))
            a1 = a1 + a
            n += 1
        return a1
    
    def divide(x, y):
        return x / y
    
    def multiply(x, y):
        return x * y
    
    def square(x):
        return x ** 2



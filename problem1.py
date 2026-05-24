
"""
In this challenge, your task is to calculate the nth Fibonacci number in the 
Fibonacci series. You have to write a recursive function fibonacci. 
In the function parameter, you will pass the value of type int, and 
the function will return a value of type int. 
It is assumed that only a non-negative value for the parameter n will be used.
"""

def fibonacci(n):
    #Starting the fibonacci sequence from 1
    if n == 1: return 1
    if n == 2: return 1
    if n == 3: return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = int(input("Enter in a positive number"))
print(fibonacci(n))

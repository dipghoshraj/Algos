'''
Recursive starategy for receiving the factorial value
of a given numbers

math equation >> n! = n*(n-1)*(n-2)....3*2*1;
'''

def factorial(n):
    if n > 0:
        return n * factorial(n -1)
    else:
        return 1

factorial_value = int(input("factorial of ::  "))

print(factorial(factorial_value))
# Task 1
a=int(input("Enter a number: "))
def factorial(a):
    fact = 1
    for i in range(1,a+1):
        fact = a*fact
        a=a-1
    return fact
b=factorial(a)
print("The factorial of", a, "is", b)


# Task 2
import math
b=int(input("enter a number:"))
def function (b):
    print("Square root:" ,math.sqrt(b))
    print("Logarithm:" ,math.log(b))
    print("sine ",math.sin(b))

function(b)

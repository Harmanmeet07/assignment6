#pascal's triangle
from math import factorial
n=int(input("Enter the number of rows you want\n"))
for i in range(n):     
    for d in range(n-i+1):
        print(end="  ")
    for d in range(i+1):
        print(factorial(i)//(factorial(d)*factorial(i-d)),end="   ")

    print()

from sympy import *

num = 1000
for i in range(num+1):
    if isprime(i):
        print(i, "&", end = "", sep = "")

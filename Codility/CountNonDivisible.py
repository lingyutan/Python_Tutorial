# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import Counter

def divisors(x):
    res = []
    for i in range(1, int(x ** 0.5)+1):
        if x % i == 0:
            res.append(i)
            if x//i != i:
                res.append(x//i)
    return res

def solution(A):
    N = len(A)
    d = Counter(A)
    res = [N] * (2*N+1)

    for i in d.keys():
        for j in divisors(i):
            res[i] -= d[j]

    return [res[x] for x in A]

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def gcd(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x%y)

def solution(N, M):
    return N // gcd(N, M)

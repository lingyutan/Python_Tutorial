import sys, math
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

for _ in range(inp()):
    n, r, b = inlt()
    x = r // (b+1)
    n1 = r % (b+1)
    n2 = b - n1
    tmp1 = 'R' * (x+1) + 'B'
    tmp2 = 'R' * x + 'B'
    res = tmp1 * n1 + tmp2 * n2
    res += 'R' * x
    print(res)

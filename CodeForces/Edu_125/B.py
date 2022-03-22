import sys
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
    lst = inlt()
    n = lst[0]
    B = lst[1]
    x = lst[2]
    y = lst[3]
    res = 0
    tmp = 0
    for _ in range(n):
        if tmp + x <= B:
            tmp += x
            res += tmp
        else:
            tmp -= y
            res += tmp
    print(res)

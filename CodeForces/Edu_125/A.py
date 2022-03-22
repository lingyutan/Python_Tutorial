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
    tmp = (lst[0]**2+lst[1]**2)**0.5
    if tmp == 0:
        print(0)
    elif tmp == int(tmp):
        print(1)
    else:
        print(2)

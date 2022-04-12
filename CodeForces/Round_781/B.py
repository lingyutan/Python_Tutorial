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
    n = inp()
    nums = inlt()
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    y = max(d.values())
    print(n-y + math.ceil(math.log2(math.ceil(n/y))))

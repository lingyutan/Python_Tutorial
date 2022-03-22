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

n, C = inlt()

squad = []
for i in range(n):
    squad.append(inlt())
squad.sort()

for _ in range(inp()):
    res = C+1
    D, H = inlt()
    for j in range(n):
        res = min( int(((H/squad[j][1]) // (squad[j][2]/D) + 1) * squad[j][0]), res)
    if res <= C:
        print(res)
    else:
        print(-1)

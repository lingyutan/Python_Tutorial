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

def isValid(s: str) -> bool:
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
    return 1 if len(stack) == 0 else 0

for _ in range(inp()):
    input()
    string = ''
    s = input().strip()
    cnt = 0
    stack = []
    for char in s:

        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()

        string += char
        if len(string) >= 2 and (len(stack) == 0 or string == string[::-1]):
            string = ''
            stack = []
            cnt += 1
    print(cnt, len(string))

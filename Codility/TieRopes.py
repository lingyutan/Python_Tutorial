# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    stack = []
    total = 0
    res = 0
    for num in A:
        if total < K:
            stack.append(num)
            total += num
        if total >= K:
            res = max(res, len(stack))
            while total >= K:
                total -= stack[0]
                stack.pop(0)
    return res

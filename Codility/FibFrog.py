# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def fib():
    res = [0, 1]
    while res[-1] < 100000:
        res.append(res[-1]+res[-2])
    return res[2:-1]

def solution(A):
    jump = fib()
    step = [None] * (len(A)+2)
    step[0] = 0
    for i in range(len(step)):
        if step[i] is None:
            continue
        for j in jump:
            if i+j > len(A)+1:
                break
            if i+j == len(A)+1 or A[i+j-1] == 1:
                step[i+j] = min(step[i+j] or 100001, step[i] + 1)

    return step[-1] if step[-1] else -1

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def check(x, A, K):
    cnt, tmp, idx = 0, 0, 0
    while idx < len(A):
        tmp += A[idx]
        if tmp > x:
            cnt += 1
            tmp = 0
            continue
        idx += 1
    cnt += 1
    return K >= cnt


def solution(K, M, A):
    l = max(A)
    r = 1000000001
    while l < r:
        m = l + (r-l)//2
        if check(m, A, K):
            r = m
        else:
            l = m + 1
    return l

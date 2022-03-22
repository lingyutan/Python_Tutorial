def inp():
    return(int(input()))

for _ in range(inp()):
    s = input()
    d = {}
    idx = len(s) - 1
    for c in s[::-1]:
        if d.get(c, None) is None:
            d[c] = idx
        idx -= 1
    print(s[min(d.values()):])

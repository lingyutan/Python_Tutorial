import math
target = 19451945
num = int(math.sqrt(target))

for i in range(num):
    left = i
    right = num
    while left <= right:
        mid = (left + right) // 2
        if i**2 + mid**2 < target:
            left = mid + 1
        elif i**2 + mid**2 > target:
            right = mid -1
        else:
            print(i, mid)
            break

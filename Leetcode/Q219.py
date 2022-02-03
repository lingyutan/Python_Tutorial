nums = [1, 2, 3, 1, 2, 3]
k = 2

d = dict()
for i in range(len(nums)):
    if d.get(nums[i], None) is not None and i - d.get(nums[i], None) <= k:
        print("True")
    else:
        d[nums[i]] = i
print("False")

print(d)

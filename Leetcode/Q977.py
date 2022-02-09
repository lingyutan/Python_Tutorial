class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        p1 = [abs(x) for x in nums].index(min(abs(x) for x in nums))
        res = [nums[p1] ** 2]
        p2 = p1 + 1
        p1 = p1 - 1
        while p1 >= 0 or p2 < len(nums):
            if p1 < 0:
                res.append(nums[p2] ** 2)
                p2 += 1
            elif p2 >= len(nums):
                res.append(nums[p1] ** 2)
                p1 -= 1
            elif abs(nums[p1]) <= abs(nums[p2]):
                res.append(nums[p1] ** 2)
                p1 -= 1
            else:
                res.append(nums[p2] ** 2)
                p2 += 1
        return res
        

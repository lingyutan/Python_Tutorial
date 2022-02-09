class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = len(nums)
        current = 0
        while k:
            if nums[current] == 0:
                nums.pop(current)
                nums.append(0)
            else:
                current += 1
            k -= 1
        

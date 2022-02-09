class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k > len(nums):
            k = k % len(nums)
        while k:
            nums.insert(0, nums[-1])
            nums.pop()
            k -= 1
        

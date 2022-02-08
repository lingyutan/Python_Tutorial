class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if target > nums[-1]:
            return(len(nums))
        while left < right:
            mid = int(left + (right-left)/2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return(mid)
        return(left)
        

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            if d.get(nums[i], None) is not None:
                return True
            else:
                d[nums[i]] = 1
        return False

nums = [1,2,3,1]

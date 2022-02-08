def twoSum(nums: list[int], target: int) -> list[int]:
        d = dict()
        for i in range(len(nums)):
            if d.get(nums[i], None) is not None:
                return [d.get(nums[i]), i]
            d[target - nums[i]] = i





print(twoSum(nums = [2, 7, 11, 15], target = 9))

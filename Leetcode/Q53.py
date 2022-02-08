"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        soln = None
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            if soln is None or tmp > soln:
                soln = tmp
            if tmp < 0:
                tmp = 0
        return(soln)

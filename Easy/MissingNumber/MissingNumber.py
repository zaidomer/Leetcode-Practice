# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = len(nums)
        for i in range(0,len(nums)):
            num += i - nums[i]

        return num
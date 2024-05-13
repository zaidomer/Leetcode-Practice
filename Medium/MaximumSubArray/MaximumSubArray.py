# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0] 
        curSum = 0 
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum = curSum + num
            maxSum = max(maxSum , curSum)
        return maxSum
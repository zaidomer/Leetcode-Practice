# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return False

        dp = [False for _ in range(len(nums)+1)]
        dp[-1] = True

        for i in range(len(nums)-2, -1, -1):
            group2 = nums[i]==nums[i+1] and dp[i+2]
            valid3Group = i<len(nums)-2 and dp[i+3]
            group3Equal = valid3Group and (nums[i]==nums[i+1]==nums[i+2])
            group3Increasing = valid3Group and (nums[i]+2==nums[i+1]+1==nums[i+2])

            dp[i] = group2 or group3Equal or group3Increasing

        return dp[0]
        
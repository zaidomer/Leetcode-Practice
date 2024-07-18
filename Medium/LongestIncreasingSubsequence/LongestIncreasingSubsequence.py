# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        LIS = [1 for _ in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    LIS[i] = max(LIS[i], LIS[j]+1)

        return max(LIS)
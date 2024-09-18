# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #Time: O(n), Space: O(1)
        zero = -1
        l=0
        res = 0

        for r in range(len(nums)):
            if nums[r]==0:
                if zero>=l:
                    l=zero+1
                zero = r
            res = max(res, r-l)

        return res if zero>=0 else len(nums)-1

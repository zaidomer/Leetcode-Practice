# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        result = float("inf")
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                result = min(result, (right-left+1))
                curr-=nums[left]
                left+=1

        if result==float("inf"):
            return 0

        return result

# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 +7
        res = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        
        while left<=right:
            if nums[left]+nums[right]<=target:
                res = (res + pow(2,(right-left),mod))%mod
                left+=1
            else:
                right-=1
        return res
        
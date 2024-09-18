# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #Time: O(n), Space: O(1)
        prod = 1
        l = 0
        res = 0

        for r in range(len(nums)):
            prod*=nums[r]
            while prod>=k and l<=r:
                prod/=nums[l]
                l+=1
            res+=(1+r-l)
        return res

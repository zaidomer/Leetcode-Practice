# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        maxP = 1
        minP = 1

        for num in nums:
            temp = maxP*num
            maxP = max(temp, minP*num, num)
            minP = min(temp, minP*num, num)
            result = max(result, maxP)

        return result

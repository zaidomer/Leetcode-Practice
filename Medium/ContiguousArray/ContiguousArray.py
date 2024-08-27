# https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        currSum = 0
        prefixSum = {0:-1}

        for i in range(len(nums)):
            currSum += 1 if nums[i]==1 else -1
            if currSum in prefixSum:
                res = max(res, i-prefixSum[currSum])
            else:
                prefixSum[currSum] = i

        return res
        
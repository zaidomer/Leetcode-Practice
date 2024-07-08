# https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        currNumZeros=0

        for i in range(0, len(nums)):
            if nums[i]==0:
                currNumZeros+=1
                result+=currNumZeros
            else:
                currNumZeros=0

        return result

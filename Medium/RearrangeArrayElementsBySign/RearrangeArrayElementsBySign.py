# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        posPtr = 0
        negPtr = 1
        
        for i in range(len(nums)):
            if nums[i]>0:
                res[posPtr]=nums[i]
                posPtr+=2
            else:
                res[negPtr]=nums[i]
                negPtr+=2
        return res

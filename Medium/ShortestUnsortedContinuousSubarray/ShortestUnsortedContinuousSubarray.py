# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minVal = float("inf")
        maxVal = float("-inf")
        left = -1
        right = -1

        for i in range(len(nums)):
            if nums[i]>=maxVal:
                maxVal = nums[i]
            else:
                right = i

        for i in range(len(nums)-1,-1,-1):
            if nums[i]<=minVal:
                minVal = nums[i]
            else:
                left=i

        if left==right==-1:
            return 0
        return right-left+1

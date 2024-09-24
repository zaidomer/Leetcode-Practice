# https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        #Time: O(n), Space: O(1)
        minI = 0
        maxI = 0

        for i in range(indexDifference, len(nums)):
            if nums[i-indexDifference]>nums[maxI]:
                maxI = i-indexDifference
            if nums[i-indexDifference]<nums[minI]:
                minI = i-indexDifference

            if nums[i]-nums[minI]>=valueDifference:
                return [minI,i]
            elif nums[maxI]-nums[i]>=valueDifference:
                return [maxI,i]
        
        return [-1,-1]

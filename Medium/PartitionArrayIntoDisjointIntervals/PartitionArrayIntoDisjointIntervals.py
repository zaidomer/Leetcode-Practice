# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        #Time: O(n), Space: O(1)
        left = 1
        maxLeft = nums[0]
        potMaxLeft = nums[0]

        for i in range(1, len(nums)):
            if nums[i]<maxLeft:
                left = i+1
                maxLeft = potMaxLeft
            potMaxLeft = max(potMaxLeft, nums[i])
        
        return left

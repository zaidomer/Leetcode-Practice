# https://leetcode.com/problems/minimum-increment-to-make-array-unique

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        prev=nums[0]
        for i in range(1, len(nums)):
            if nums[i]<=prev:
                count+=prev-nums[i]+1
                prev+=1
            else:
                prev=nums[i]
        
        return count

# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mostRecent = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i]>=mostRecent:
                mostRecent = i
        return mostRecent==0

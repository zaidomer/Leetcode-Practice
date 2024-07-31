# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp = [len(nums) for _ in range(len(nums))]
        # dp[-1]=0

        # for i in range(len(nums)-2, -1, -1):
        #     if nums[i]>0:
        #         s = i+1
        #         e = min(i+nums[i]+1,len(nums))
        #         if e>s:
        #             dp[i] = 1 + min(dp[s:e])

        # return dp[0]







        result = 0
        l=0
        r=0

        while r<len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            l=r+1
            r=farthest
            result+=1
        return result

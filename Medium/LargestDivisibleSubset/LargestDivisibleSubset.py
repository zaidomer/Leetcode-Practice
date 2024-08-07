# https://leetcode.com/problems/largest-divisible-subset/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # dp = {}

        # def dfs(i):
        #     if i==len(nums):
        #         return []
        #     elif i in dp:
        #         return dp[i]

        #     res = [nums[i]]
        #     for j in range(i+1, len(nums)):
        #         if nums[j]%nums[i]==0:
        #             temp = [nums[i]] + dfs(j)
        #             if len(temp)>len(res):
        #                 res = temp
        #     dp[i]=res
        #     return res

        # res = []
        # for i in range(len(nums)):
        #     temp = dfs(i)
        #     if len(temp)>len(res):
        #         res = temp
        # return res










        nums.sort()
        dp = [[nums[i]] for i in range(len(nums))]
        res=[]

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j]%nums[i]==0:
                    temp = [nums[i]]+dp[j]
                    if len(temp)>len(dp[i]):
                        dp[i] = temp
            if len(dp[i])>len(res):
                res = dp[i]
        return res
        
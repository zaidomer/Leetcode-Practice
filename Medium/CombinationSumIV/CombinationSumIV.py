# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ## Valid recursive momoization, Time: O(nm), Space: O(n), where n=target, m=nums
        # dp = defaultdict(int)

        # def dfs(total):
        #     if total==target:
        #         return 1
        #     elif total>target:
        #         return 0
        #     elif total in dp:
        #         return dp[total]

        #     res = 0
        #     for num in nums:
        #         res+=dfs(total+num)
        #     dp[total]=res
        #     return dp[total]
        # return dfs(0)
        






        #DP Approach, Time: O(nm), Space: O(n)
        dp = defaultdict(int)
        dp[0]=1
        for total in range(1, target+1):
            for num in nums:
                dp[total]+=dp[total-num]
        return dp[target]

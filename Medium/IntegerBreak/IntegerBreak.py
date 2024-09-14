# https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        # Initial solution, works fine, but can be simplified
        # ans = 0
        # cache = defaultdict(int)

        # def dfs(remaining):
        #     if remaining==0:
        #         return 1
        #     elif remaining in cache:
        #         return cache[remaining]

        #     res = 0
        #     for i in range(1, remaining+1):
        #         res = max(res, i*dfs(remaining-i))
        #     cache[remaining] = res
        #     return res
        
        # for i in range(1, n):
        #     ans = max(ans, i*dfs(n-i))
        # return ans







        #Same complexity as initial try. Time: O(n^2), Space: O(n)
        # dp = {1:1}
        # def dfs(num):
        #     if num in dp:
        #         return dp[num]
            
        #     dp[num] = 0 if num==n else num
        #     for i in range(1, num):
        #         val = dfs(i)*dfs(num-i)
        #         dp[num] = max(val, dp[num])
        #     return dp[num]

        # return dfs(n)







        #DP Solution, Time: O(n^2), Space: O(n)
        dp = {1:1}
        for num in range(2, n+1):
            dp[num] = 0 if num==n else num
            for i in range(1, num):
                val = dp[i]*dp[num-i]
                dp[num] = max(dp[num], val)
        return dp[n]

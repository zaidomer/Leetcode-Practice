# https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp = {}

        # def dfs(i, remaining):
        #     if remaining==0:
        #         return 1
        #     elif remaining < 0 or i==len(coins):
        #         return 0
        #     elif (i, remaining) in dp:
        #         return dp[(i, remaining)]

        #     dp[(i, remaining)] = dfs(i+1, remaining) + dfs(i, remaining-coins[i])
        #     return dp[(i, remaining)]

        # return dfs(0, amount)





        


        prevDp = [0 for _ in range(amount+1)]
        prevDp[0] = 1

        for i in range(len(coins)-1, -1, -1):
            dp = [0 for _ in range(amount+1)]
            dp[0] = 1
            for j in range(1, amount+1):
                dp[j]=prevDp[j]
                if j-coins[i] >= 0:
                    dp[j] += dp[j-coins[i]]
            prevDp = dp
        return dp[amount]
        
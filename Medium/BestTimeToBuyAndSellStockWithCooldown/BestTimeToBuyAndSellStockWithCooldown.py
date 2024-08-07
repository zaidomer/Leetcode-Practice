# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i>=len(prices):
                return 0
            elif (i, buying) in dp:
                return dp[(i,buying)]

            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, False) - prices[i]
                dp[(i,buying)] = max(cooldown, buy)
            else:
                sell = dfs(i+2, True) + prices[i]
                dp[(i, buying)] = max(cooldown, sell)
            return dp[(i,buying)]

        return dfs(0,True)
        
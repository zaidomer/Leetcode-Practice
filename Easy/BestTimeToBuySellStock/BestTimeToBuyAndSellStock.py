# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        result = 0

        for right in range(1, len(prices)):
            if prices[right]<prices[left]:
                left = right
            else:
                result = max(result, prices[right]-prices[left])

        return result

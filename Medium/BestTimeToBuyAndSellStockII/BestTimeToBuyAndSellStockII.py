# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        result = 0

        for right in range(0, len(prices)):
            if prices[right]>prices[left]:
                result+=prices[right]-prices[left]
            left = right

        return result

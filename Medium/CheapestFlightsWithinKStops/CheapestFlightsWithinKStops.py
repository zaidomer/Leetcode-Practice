# https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") for _ in range(n)]
        prices[src]=0

        for i in range(k+1):
            tempPrices = prices[:]
            for start,end,price in flights:
                if prices[start]==float("inf"):
                    continue
                elif prices[start]+price < tempPrices[end]:
                    tempPrices[end] = prices[start]+price
            prices = tempPrices

        return -1 if prices[dst]==float("inf") else prices[dst]

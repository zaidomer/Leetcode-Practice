# https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        added = 0
        rangeEnd = 0
        i=0

        while rangeEnd<target:
            if i<len(coins) and coins[i]<=rangeEnd+1:
                rangeEnd+=coins[i]
                i+=1
            else:
                added+=1
                rangeEnd+=(rangeEnd+1)
        return added
        
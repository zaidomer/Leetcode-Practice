# https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # result = 0
        # empty = 0
        # full=numBottles

        # while full>0:
        #     result+=full
        #     empty+=full
        #     full=empty//numExchange
        #     empty=empty%numExchange
        
        # return result
        return numBottles + (numBottles-1)//(numExchange-1)
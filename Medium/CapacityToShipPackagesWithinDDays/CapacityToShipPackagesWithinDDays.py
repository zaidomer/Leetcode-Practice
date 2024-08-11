# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def canUseWeight(w):
            daysUsed = 1
            currWeight = 0
            for i in range(len(weights)):
                if (currWeight+weights[i])<=w:
                    currWeight += weights[i]
                else:
                    currWeight = weights[i]
                    daysUsed+=1

                if daysUsed>days:
                    return False
            return True

        while l<=r:
            mid = l+(r-l)//2
            if canUseWeight(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res

# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        #Time: O(nlogn + nlogm) where n is len(price) m is max taste value, Space: O(n) for sorting
        price.sort()
        l=0
        r=price[-1]-price[0]
        res = 0

        def fit(taste):
            count = 1
            prev = 0
            for i in range(len(price)):
                if price[i]-price[prev]>=taste:
                    count+=1
                    prev=i
            return count>=k

        while l<=r:
            mid = l+(r-l)//2
            if fit(mid):
                res = mid
                l = mid+1
            else:
                r = mid-1
        return res

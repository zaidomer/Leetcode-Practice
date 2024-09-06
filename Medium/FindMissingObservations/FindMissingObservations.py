# https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        mSum = sum(rolls)
        total = mean*(m+n)
        nSum = total-mSum

        if nSum>6*n or nSum<n:
            return []
        
        res = []
        for i in range(n):
            die = ceil(nSum/(n-len(res)))
            res.append(die)
            nSum-=die
        return res

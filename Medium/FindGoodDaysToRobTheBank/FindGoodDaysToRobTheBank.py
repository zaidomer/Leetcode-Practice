# https://leetcode.com/problems/find-good-days-to-rob-the-bank/

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        decreasing = [0 for _ in range(len(security))]
        increasing = [0 for _ in range(len(security))]
        res = []

        for i in range(len(security)):
            if i>0 and security[i]<=security[i-1]:
                decreasing[i] = decreasing[i-1]+1

        for i in range(len(security)-1,-1,-1):
            if i<len(security)-1 and security[i]<=security[i+1]:
                increasing[i] = increasing[i+1]+1
            if decreasing[i]>=time and increasing[i]>=time:
                res.append(i)

        return res
        
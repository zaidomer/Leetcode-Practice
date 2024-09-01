# https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0 for _ in range(n+1)]
        total = 0

        for i in range(len(citations)):
            if citations[i]>=n:
                count[n]+=1
            else:
                count[citations[i]]+=1

        for i in range(n, -1, -1):
            total+=count[i]
            if total>=i:
                return i
        return 0

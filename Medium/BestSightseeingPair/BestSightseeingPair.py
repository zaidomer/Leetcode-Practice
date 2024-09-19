class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        #Time: O(n), Space: O(1)
        res = 0
        iVal = 0
        for j in range(1, len(values)):
            i=j-1
            iVal = max(iVal, values[i]+i)
            res = max(res, iVal+values[j]-j)
        return res
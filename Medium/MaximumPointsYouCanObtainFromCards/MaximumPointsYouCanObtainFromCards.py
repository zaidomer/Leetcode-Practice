# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k>=len(cardPoints):
            return sum(cardPoints)

        right = k
        left = len(cardPoints)
        res = sum(cardPoints[0:right])
        curr = res

        for i in range(k):
            right-=1
            left-=1
            curr = curr-cardPoints[right]+cardPoints[left]
            res = max(res, curr)
        return res

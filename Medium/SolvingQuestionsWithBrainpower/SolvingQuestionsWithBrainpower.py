# https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [questions[i][0] for i in range(0, len(questions))]
        currMax = dp[-1]
        for i in range(len(questions)-1,-1,-1):
            nextQIndex = i+questions[i][1]+1
            if nextQIndex<len(questions):
                dp[i]+=dp[nextQIndex]
            
            currMax = max(currMax, dp[i])
            dp[i] = currMax

        return currMax

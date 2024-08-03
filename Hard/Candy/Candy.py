# https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        dp = [1 for _ in range(len(ratings))]
        numCandies=0

        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                dp[i]=dp[i-1]+1


        for i in range(len(ratings)-2, -1, -1):
            if ratings[i]>ratings[i+1]:
                dp[i]= max(dp[i], dp[i+1]+1)
            numCandies+=dp[i]
        numCandies+=dp[-1]

        return numCandies
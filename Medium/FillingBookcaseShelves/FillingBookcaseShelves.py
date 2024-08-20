# https://leetcode.com/problems/filling-bookcase-shelves/

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        ## VALID RECURSIVE APPROACH, SAME TIME AND SPACE COMPLEXITY
        # cache = {}
        # def helper(i):
        #     if i >=len(books):
        #         return 0
        #     elif i in cache:
        #         return cache[i]
            
        #     currWidth = shelfWidth
        #     maxHeight = 0
        #     cache[i] = float("inf")
        #     for j in range(i, len(books)):
        #         width, height = books[j]
        #         if currWidth<width:
        #             break
        #         currWidth-=width
        #         maxHeight = max(maxHeight, height)
        #         cache[i] = min(cache[i], maxHeight+helper(j+1))
        #     return cache[i]

        # return helper(0)










        ## BOTTOM UP DP APPROACH
        dp = [0 for _ in range(len(books)+1)]

        for i in range(len(books)-1,-1,-1):
            currWidth = shelfWidth
            maxHeight = 0
            dp[i] = float("inf")
            for j in range(i, len(books)):
                width, height = books[j]
                if currWidth<width:
                    break
                currWidth-=width
                maxHeight = max(maxHeight, height)
                dp[i] = min(dp[i], maxHeight+dp[j+1])

        return dp[0]
        
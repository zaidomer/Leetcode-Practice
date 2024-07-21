# https://leetcode.com/problems/stone-game/submissions/1328171994/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # return True #LOL no way

        dp = {}

        #return the max Alice can get
        def dfs(left, right):
            if left>right:
                return 0
            elif (left,right) in dp:
                return dp[(left,right)]

            even = False
            if (right-left)%2==1:
                even = True

            stonesTakenRight = piles[right]
            stonesTakenLeft = piles[left]
            if not even:
                stonesTakenRight=0
                stonesTakenLeft=0

            dp[(left,right)] = max(dfs(left+1, right) + stonesTakenLeft, dfs(left, right-1) + stonesTakenRight)
            return dp[(left,right)]

        return dfs(0, len(piles)-1) > (sum(piles))//2
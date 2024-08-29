# https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        upperRight = sum(grid[0])
        lowerLeft = 0
        res = float('inf')
        for i in range(COLS):
            upperRight-=grid[0][i]
            res = min(res, max(upperRight, lowerLeft))
            lowerLeft+=grid[1][i]
        return res

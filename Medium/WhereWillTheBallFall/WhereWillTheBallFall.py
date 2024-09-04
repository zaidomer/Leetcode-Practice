# https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = []
        def travel(col):
            row=0
            while row<ROWS:
                curr = grid[row][col]
                if (curr==-1 and (col==0 or curr*grid[row][col-1]==-1)) or (curr==1 and (col==COLS-1 or curr*grid[row][col+1]==-1)):
                    res.append(-1)
                    return
                elif curr==1:
                    col+=1
                else:
                    col-=1
                row+=1
            res.append(col)

        for i in range(COLS):
            travel(i)
        return res

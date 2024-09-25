# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        #Time: O(nm), Space: O(m)
        res = 0
        prevX = [0 for _ in range(len(grid[0]))]
        prevY = [0 for _ in range(len(grid[0]))]

        for i in range(len(grid)):
            numX = 0
            numY = 0
            for j in range(len(grid[0])):
                if grid[i][j]=='X':
                    numX+=1
                elif grid[i][j]=='Y':
                    numY+=1

                prevX[j]+=numX
                prevY[j]+=numY

                if prevX[j]==prevY[j] and prevX[j]!=0:
                    res+=1

        return res

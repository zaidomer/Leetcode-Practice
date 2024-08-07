# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 2
        # 3 4
        # 6 5 1
        # 4 1 8 1


        # dp = {}
        # def dfs(row, col):
        #     if row>=len(triangle):
        #         return 0
        #     elif (row,col) in dp:
        #         return dp[(row,col)]

        #     dp[(row,col)] = triangle[row][col] + min(dfs(row+1,col), dfs(row+1,col+1))
        #     return dp[(row,col)]
        # return dfs(0,0)









        for i in range(len(triangle)-2, -1, -1):
            for j in range(0,len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
        
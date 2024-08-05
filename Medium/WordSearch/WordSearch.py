# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()

        def dfs(row,col,index):
            if row<0 or col<0 or row>=ROWS or col>=COLS or (row,col) in visit or word[index]!=board[row][col]:
                return False
            elif index==len(word)-1:
                return True

            visit.add((row,col))
            res = dfs(row+1,col,index+1) or dfs(row-1,col,index+1) or dfs(row,col+1,index+1) or dfs(row,col-1,index+1)
            visit.remove((row,col))

            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True

        return False
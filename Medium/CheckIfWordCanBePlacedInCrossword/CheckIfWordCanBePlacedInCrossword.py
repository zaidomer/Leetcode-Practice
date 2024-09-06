# https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row, col, i, horizontal, dir, end):
            if i==len(word):
                if (horizontal and (col==end or board[row][col]=='#')) or (not horizontal and (row==end or board[row][col]=='#')):
                    return True
                else:
                    return False
            elif row>=ROWS or col>=COLS or row<0 or col<0 or (board[row][col]!=' ' and board[row][col]!=word[i]):
                return False
            
            newRow = row if horizontal else row+dir
            newCol = col+dir if horizontal else col
            return dfs(newRow, newCol, i+1, horizontal, dir, end)

        for row in range(ROWS):
            for col in range(COLS):
                if (col==0 or board[row][col-1]=='#') and dfs(row, col, 0, True, 1, COLS):
                    return True
                if (col==COLS-1 or board[row][col+1]=='#') and dfs(row, col, 0, True, -1, -1):
                    return True
                if (row==0 or board[row-1][col]=='#') and dfs(row, col, 0, False, 1, ROWS):
                    return True
                if (row==ROWS-1 or board[row+1][col]=='#') and dfs(row, col, 0, False, -1, -1):
                    return True

        return False
    
    ###NOTE AN ITERATIVE SOLUTION WOULD BE BETTER THAN RECUSRSION. This is O(m*n*max(m,n)) time and space. 
    # Space for iterative could be O(1) (with same time complexity)

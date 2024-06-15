class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap={}
        colMap={}
        boxMap={}

        for i in range(0, 9):
            for j in range(0, 9):
                if not board[i][j].isdigit():
                    continue

                val = board[i][j]
                boxIndex = self.getBox(i, j)
                rowSet = rowMap.get(i, set())
                colSet = colMap.get(j, set())
                boxSet = boxMap.get(boxIndex, set())

                if (val in rowSet) or (val in colSet) or (val in boxSet):
                    return False

                rowSet.add(val)
                colSet.add(val)
                boxSet.add(val)

                rowMap[i]=rowSet
                colMap[j]=colSet
                boxMap[boxIndex]=boxSet

        return True

    def getBox(self, row: int, col: int) -> int:
        # 0,1,2
        # 3,4,5
        # 6,7,8

        if row<3:
            if col<3:
                return 0
            elif col<6:
                return 1
            else:
                return 2
        elif row<6:
            if col<3:
                return 3
            elif col<6:
                return 4
            else:
                return 5
        else:
            if col<3:
                return 6
            elif col<6:
                return 7
            else:
                return 8

# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # result = []
        # colMaxValues = {}

        # def getColMax(col:int) -> int:
        #     if col in colMaxValues:
        #         return colMaxValues[col]
            
        #     maxVal = -1
        #     for row in range(len(matrix)):
        #         maxVal = max(maxVal, matrix[row][col])

        #     colMaxValues[col] = maxVal
        #     return maxVal

        # for row in range(len(matrix)):
        #     rowMin = float('inf')
        #     rowMinValCol = -1
        #     for col in range(len(matrix[0])):
        #         curr = matrix[row][col]
        #         if curr < rowMin:
        #             rowMin = curr
        #             rowMinValCol = col

        #     if rowMin == getColMax(rowMinValCol):
        #         result.append(rowMin)
            
        # return result

        ROWS = len(matrix)
        COLS = len(matrix[0])

        maxOfRowMins = float("-inf")

        for row in range(ROWS):
            rowMin = float("inf")
            rowMinColIndex = -1

            for col in range(COLS):
                if matrix[row][col] < rowMin:
                    rowMin = matrix[row][col]
                    rowMinColIndex = col  

            if rowMin > maxOfRowMins:
                maxOfRowMins = rowMin
                maxOfRowMinsColIndex = rowMinColIndex

        colMax = float("-inf")
        for row in range(ROWS):
            colMax = max(colMax, matrix[row][maxOfRowMinsColIndex])

        if colMax == maxOfRowMins:
            return [colMax]

        return []
            
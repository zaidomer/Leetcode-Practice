# https://leetcode.com/problems/find-all-groups-of-farmland/

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result=[]

        for row in range(0, len(land)):
            for col in range(0, len(land[0])):
                if land[row][col] and (row==0 or (row>0 and land[row-1][col]==0)) and (col==0 or (col>0 and land[row][col-1]==0)):
                    testRow=row
                    testCol=col

                    while testRow<len(land)-1 and land[testRow+1][col]==1:
                        testRow+=1
                        
                    while testCol<len(land[0])-1 and land[testRow][testCol+1]==1:
                        testCol+=1
                    
                    result.append([row,col,testRow,testCol])
        
        return result
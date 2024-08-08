# https://leetcode.com/problems/path-with-minimum-effort/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        heap=[]
        heappush(heap, (0,0,0))
        visit = set()

        while heap:
            effort,row,col = heappop(heap)
            if (row,col) in visit:
                continue
            elif row==ROWS-1 and col==COLS-1:
                return effort
            
            visit.add((row,col))
            for dr,dc in directions:
                r=row+dr
                c=col+dc
                if r>=0 and c>=0 and r<ROWS and c<COLS and (r,c) not in visit:
                    newEffort = max(effort, abs(heights[row][col]-heights[r][c]))
                    heappush(heap, (newEffort,r,c))
        return 0

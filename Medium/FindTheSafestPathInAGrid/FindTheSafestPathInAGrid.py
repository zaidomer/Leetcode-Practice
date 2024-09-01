# https://leetcode.com/problems/find-the-safest-path-in-a-grid/

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        q = deque()

        for i in range(N):
            for j in range(N):
                if grid[i][j]==1:
                    q.append((i,j,0))
                    grid[i][j]=0
                else:
                    grid[i][j]=-1

        while q:
            row,col,dist = q.popleft()
            for dr,dc in directions:
                r = row+dr
                c = col+dc
                if r<0 or c<0 or r>=N or c>=N or grid[r][c]!=-1:
                    continue
                grid[r][c] = dist+1
                q.append((r,c,dist+1))
        
        heap = [(-grid[0][0], 0, 0)]
        heapify(heap)
        visit = set()

        while heap:
            dist, row, col = heappop(heap)
            dist = -dist
            if (row,col) in visit:
                continue
            elif row==N-1 and col==N-1:
                return dist
            visit.add((row,col))
            for dr, dc in directions:
                r = row+dr
                c = col+dc
                if r<0 or c<0 or r>=N or c>=N or (r,c) in visit:
                    continue
                newDist = min(dist, grid[r][c])
                heappush(heap, (-newDist, r, c))

        return 0

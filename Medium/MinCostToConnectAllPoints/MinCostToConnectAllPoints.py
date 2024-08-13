# https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        heappush(heap,(0,points[0][0],points[0][1]))
        visit = set()
        res = 0

        while heap:
            cost,x,y = heappop(heap)
            if (x,y) in visit:
                continue
            visit.add((x,y))
            res+=cost
            if len(visit)==len(points):
                break
            for nX,nY in points:
                if (nX,nY) in visit:
                    continue
                distance = abs(nX-x)+abs(nY-y)
                heappush(heap,(distance,nX,nY))
        return res
        
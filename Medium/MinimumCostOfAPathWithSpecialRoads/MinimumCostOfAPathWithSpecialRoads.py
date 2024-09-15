# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        #Time: O((V+E)logV) = O(n^2logn) in this case, where n is number of locations in specialRoads
        #Space: O(V) = O(n^2) in this case

        visit = set()

        def calcCost(x1, y1, x2, y2):
            return abs(x2-x1)+abs(y2-y1)
        
        heap = [(0, start[0], start[1])]
        heapify(heap)
        while heap:
            cost, x, y = heappop(heap)
            if [x,y]==target:
                return cost
            elif (x,y) in visit:
                continue
            visit.add((x,y))
            for x1,y1,x2,y2,c in specialRoads:
                if (x1,y1)==(x,y):
                    if (x2,y2) in visit:
                        continue
                    newCost = cost+c
                    heappush(heap, (newCost, x2, y2))
                else:
                    if (x1,y1) in visit:
                        continue
                    newCost = cost+calcCost(x,y,x1,y1)
                    heappush(heap, (newCost, x1, y1))
            heappush(heap, (cost+calcCost(x, y, target[0], target[1]), target[0], target[1]))
        return 0

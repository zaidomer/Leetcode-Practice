# https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        numBuildings = 0
        heap = []

        for i in range(0, len(heights)-1):
            diff = heights[i+1]-heights[i]
            if diff<=0:
                numBuildings+=1
            else:
                heappush(heap, diff)
                numBuildings+=1
                if len(heap)>ladders:
                    numBricksUsed = heappop(heap)
                    if numBricksUsed<=bricks:
                        bricks-=numBricksUsed
                    else:
                        return numBuildings-1

        return numBuildings
        
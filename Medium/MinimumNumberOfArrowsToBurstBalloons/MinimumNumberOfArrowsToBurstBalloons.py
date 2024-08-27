# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0:
            return 0

        arrows = 1
        points.sort()
        currRegion = [float("-inf"), float("inf")]
        for i in range(0, len(points)):
            if points[i][0]>=currRegion[0] and points[i][0]<=currRegion[1]:
                currRegion = [points[i][0], min(currRegion[1], points[i][1])]
            else:
                currRegion = points[i]
                arrows+=1

        return arrows

# https://leetcode.com/problems/minimum-area-rectangle/

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        result = float("inf")
        pointSet = set()

        for p in points:
            pointSet.add((p[0], p[1]))

        for p1 in points:
            p1X = p1[0]
            p1Y = p1[1]
            for p2 in points:
                p2X = p2[0]
                p2Y = p2[1]
                if p2X>p1X and p2Y>p1Y and ((p1X, p2Y) in pointSet) and ((p2X, p1Y) in pointSet):
                    currArea = (p2X-p1X)*(p2Y-p1Y)
                    result = min(result, currArea)

        if result==float("inf"):
            return 0

        return result

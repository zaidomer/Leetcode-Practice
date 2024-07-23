# https://leetcode.com/problems/detect-squares/

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])]+=1

    def count(self, point: List[int]) -> int:
        x1 = point[0]
        y1 = point[1]
        result = 0

        for p in self.points:
            x2 = p[0]
            y2 = p[1]
            if (x1!=x2) and (y1!=y2) and (abs(x1-x2)==abs(y1-y2)) and ((x1,y2) in self.points) and ((x2,y1) in self.points):
                result += self.points[(x2,y2)] * self.points[(x2,y1)] * self.points[(x1,y2)]

        return result


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
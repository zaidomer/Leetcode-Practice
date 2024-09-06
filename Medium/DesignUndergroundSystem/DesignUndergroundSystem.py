# https://leetcode.com/problems/design-underground-system/?envType=problem-list-v2&envId=design

class UndergroundSystem:
    #Time: O(1), Space: O(n + m^2) where n is number of people travelled and m is number of stations

    def __init__(self):
        self.checkIns = {} # id -> (start, time)
        self.averages = {} # (start, end) -> (avg, numPts)

    def checkIn(self, id: int, start: str, t: int) -> None:
        self.checkIns[id] = (start, t)

    def checkOut(self, id: int, end: str, t: int) -> None:
        start, tripStartTime = self.checkIns[id]
        self.checkIns.pop(id)
        if (start, end) in self.averages:
            avg, pts = self.averages[(start, end)]
            avg = (avg*pts+(t-tripStartTime))/(pts+1)
            pts+=1
            self.averages[(start, end)] = (avg, pts)
        else:
            self.averages[(start, end)] = (t-tripStartTime, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averages[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
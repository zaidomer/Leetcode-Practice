# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        res = min(passengers[0]-1, buses[-1])
        i = 0

        for busTime in buses:
            people = capacity
            while i<len(passengers) and passengers[i]<=busTime and people>0:
                if i>0 and passengers[i]-1!=passengers[i-1]:
                    res = passengers[i]-1
                i+=1
                people-=1
            if people>0 and passengers[i-1]<busTime:
                res = busTime
        return res

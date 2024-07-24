# https://leetcode.com/problems/meeting-rooms/description/
# https://neetcode.io/problems/meeting-schedule

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda time: time.start)

        for i in range(0, len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False

        return True
# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # result = []

        # if not intervals or newInterval[1] < intervals[0][0]:
        #     result = [newInterval]
        #     result.extend(intervals)
        #     return result

        # added = False
        # for time in intervals:
        #     currS = time[0]
        #     currE = time[1]
        #     newS = newInterval[0]
        #     newE = newInterval[1]


        #     if ((currE >= newS) and (newS >= currS)) or ((newE <= currE) and (newE >= currS)) or ((currS >= newS) and (currE <= newE)):
        #         newInterval[0] = min(newS, currS)
        #         newInterval[1] = max(newE, currE)
        #     else:
        #         if not added and newE<=time[0]:
        #             result.append(newInterval)
        #             added = True
        #         result.append(time)

        # if not added:
        #     result.append(newInterval)
        
        # return result


        result = []
        
        for i in range(0, len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        result.append(newInterval)
        return result
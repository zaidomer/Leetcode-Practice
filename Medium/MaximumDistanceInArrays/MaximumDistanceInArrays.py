# https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        # def maxAndMin(skip):
        #     minVal = None
        #     minI = -1
        #     maxVal = None
        #     maxI = -1

        #     for i in range(len(arrays)):
        #         if i==skip:
        #             continue
        #         if minVal is None or arrays[i][0]<minVal:
        #             minVal = arrays[i][0]
        #             minI = i
        #         if maxVal is None or arrays[i][-1]>maxVal:
        #             maxVal = arrays[i][-1]
        #             maxI = i
        #     return (minI, maxI)
        
        # minI, maxI = maxAndMin(-1)
        # if minI!=maxI:
        #     return arrays[maxI][-1] - arrays[minI][0]

        # secondMinI, secondMaxI = maxAndMin(minI)
        # return max(arrays[maxI][-1]-arrays[secondMinI][0], arrays[secondMaxI][-1]-arrays[minI][0])












        res = 0
        maxVal = arrays[0][-1]
        minVal = arrays[0][0]
        for i in range(1, len(arrays)):
            res = max(res, abs(arrays[i][-1]-minVal), abs(maxVal-arrays[i][0]))
            minVal = min(minVal, arrays[i][0])
            maxVal = max(maxVal, arrays[i][-1])
        return res

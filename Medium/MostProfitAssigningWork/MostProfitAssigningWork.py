# https://leetcode.com/problems/most-profit-assigning-work

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobProfit = {}
        for i in range(0, len(difficulty)):
            jobProfit[difficulty[i]] = max(jobProfit.get(difficulty[i], -1), profit[i]) 
        jobProfit = dict(sorted(jobProfit.items()))

        currMax = -1
        for key in jobProfit:
            currMax = max(jobProfit[key], currMax)
            jobProfit[key] = currMax 

        allKeys = list(jobProfit.keys())

        result = 0
        for i in range(0, len(worker)):
            keyIndex = self.binarySearch(allKeys, worker[i])
            if keyIndex!=-1:
                result+=jobProfit[allKeys[keyIndex]]
        
        return result

    def binarySearch(self, arr:List[int], val:int) -> int:
        left = 0
        right = len(arr)-1
        mid = 0
        prev = -1

        while left<=right:
            mid = (right+left)//2
            if arr[mid]==val:
                return mid
            elif arr[mid]<val:
                prev = mid
                left = mid+1
            else:
                right = mid-1

        if arr[mid]>val:
            return prev

        return mid

        
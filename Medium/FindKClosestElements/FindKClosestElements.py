# https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lBest=0
        rBest=k-1
        left = 0
        dist=0
        for i in range(k):
            dist+=abs(x-arr[i])
        currDist=dist

        for right in range(k, len(arr)):
            if arr[left]>=x:
                break

            currDist += abs(x-arr[right])-abs(x-arr[left])
            left+=1
            if currDist<dist:
                lBest=left
                rBest=right
                dist=currDist

        return arr[lBest:rBest+1]

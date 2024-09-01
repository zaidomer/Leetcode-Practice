# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1

        while l<=r:
            mid = l+(r-l)//2
            print(str(mid)+", "+str(l)+", "+str(r))
            if mid>0 and mid<len(arr)-1 and arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            elif mid==0 or arr[mid-1]<arr[mid]:
                l=mid+1
            else:
                r=mid-1
        return -1

# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0

        l = 0
        r = len(nums)-1

        while l<=r:
            mid = l+(r-l)//2
            if (mid==0 and nums[0]>nums[1]) or (mid==len(nums)-1 and nums[-2]<nums[-1]) or (nums[mid-1]<nums[mid]>nums[mid+1]):
                return mid
            elif mid+1<len(nums) and nums[mid+1]>nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return -1
        
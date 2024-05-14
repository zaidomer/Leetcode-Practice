# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = left + (right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                if nums[mid]>nums[len(nums)-1]>=target:
                    left = mid+1
                else:
                    right = mid-1
            elif nums[mid]<target:
                if nums[mid]<nums[0]<=target:
                    right=mid-1
                else:
                    left = mid+1
        
        return -1

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]

        # def isSmallest(mid:int) -> bool:
        #     if (mid==0 and nums[mid]<nums[mid+1]) or (mid==len(nums)-1 and nums[mid]<nums[mid-1]) or (mid>0 and mid<len(nums)-1 and nums[mid]<nums[mid+1]<nums[mid-1]):
        #         return True
        #     return False

        # left = 0
        # right = len(nums)-1

        # while left<=right:
        #     mid = left+(right-left)//2
        #     if isSmallest(mid):
        #         return nums[mid]
        #     elif nums[mid]>nums[right]:
        #         left = mid+1
        #     else:
        #         right = mid-1


        result = nums[0]
        l=0
        r=len(nums)-1

        while l<=r:
            if nums[l]<nums[r]:
                result = min(result, nums[l])
                break
            
            mid = l+(r-l)//2
            result = min(result, nums[mid])
            if nums[mid]>=nums[l]:
                l=mid+1
            else:
                r=mid-1
        
        return result
        
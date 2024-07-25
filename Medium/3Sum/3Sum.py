# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(0, len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            
            left = i+1
            right = len(nums)-1

            while left<right:
                threeSum = nums[i]+nums[left]+nums[right]
                if threeSum>0:
                    right-=1
                elif threeSum<0:
                    left+=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while nums[left-1]==nums[left] and left<right:
                        left+=1

        return result

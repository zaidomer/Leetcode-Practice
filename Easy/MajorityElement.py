#https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # majority = nums[0]
        # data={}
        
        # for i in range(0, len(nums)):      
        #     if nums[i] in data:
        #         data[nums[i]] = data[nums[i]]+1
        #     else:
        #         data[nums[i]] = 1

        #     if (data[majority] < data[nums[i]]):
        #         majority = nums[i]

        # return majority

        nums.sort()
        return nums[len(nums)//2]
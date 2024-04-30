#https://leetcode.com/problems/majority-element/

class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
        # map = Counter(nums)

        # for key in map:
        #     if map[key] >= len(nums)/2:
        #         return key

        # return -1

    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        majorityCount = 0
        
        for i in range(0,len(nums)):
            if majorityCount == 0:
                majority = nums[i]
            
            if nums[i] == majority:
                majorityCount += 1 
            else:
                majorityCount-=1
        
        return majority


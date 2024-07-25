# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    # def findMaxAverage(self, nums: List[int], k: int) -> float:
    #     currSum = 0
    #     result = None
    #     left = 0

    #     for right in range(0, len(nums)):
    #         if (right-left+1)>k:
    #             currSum-=nums[left]
    #             left+=1
            
    #         currSum+=nums[right]

    #         if (right-left+1)==k:
    #             if not result:
    #                 result = currSum
    #             else:
    #                 result = max(result, currSum)

    #     result/=k
    #     return result

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[0:k])
        result = currSum
        left = 0

        for right in range(k, len(nums)):
            currSum += nums[right]
            currSum -= nums[left]
            left+=1
            result = max(result, currSum)

        result/=k
        return result

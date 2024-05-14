# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # result = []

        # for i in range(0, len(nums)):
        #     heappush(result,nums[i]*nums[i])

        # return [heappop(result) for i in range(len(result))]

        right=len(nums)-1
        left=0
        result = [0 for _ in range(len(nums))]

        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left]) < abs(nums[right]):
                result[i] = nums[right]**2
                right-=1
            else:
                result[i] = nums[left]**2
                left+=1
        
        return result

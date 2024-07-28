# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # before = [1 for _ in range(len(nums))]
        # after = [1 for _ in range(len(nums))]

        # for i in range(1, len(nums)):
        #     before[i] = nums[i-1]*before[i-1]

        # for i in range(len(nums)-2, -1, -1):
        #     after[i] = nums[i+1]*after[i+1]

        # result = []
        # for i in range(len(nums)):
        #     result.append(before[i]*after[i])

        # return result

        before=1
        after=1
        result = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            j=len(nums)-1-i
            
            result[i]*=before
            before*=nums[i]

            result[j]*=after
            after*=nums[j]

        return result

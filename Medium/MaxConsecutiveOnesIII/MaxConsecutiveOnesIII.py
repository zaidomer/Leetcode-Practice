# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # left = 0
        # res = 0
        # numZeroes = 0

        # for right in range(len(nums)):
        #     numZeroes += 1 if nums[right]==0 else 0
        #     while numZeroes>k and left<=right:
        #         numZeroes -= 1 if nums[left]==0 else 0
        #         left+=1
        #     res = max(res, right-left+1)
        # return res







        left = 0
        right = 0

        for right in range(len(nums)):
            if nums[right]==0:
                k-=1

            if k<0:
                if nums[left]==0:
                    k+=1
                left+=1

        return right-left+1
        
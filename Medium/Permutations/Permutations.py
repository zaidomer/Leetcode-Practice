# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # result = []

        # def permuteNums(start:int):
        #     if start==(len(nums)-1):
        #         result.append(nums[:])
        #         return

        #     for i in range(start, len(nums)):
        #         nums[start], nums[i] = nums[i], nums[start]
        #         permuteNums(start+1)
        #         nums[start], nums[i] = nums[i], nums[start]

        # permuteNums(0)
        # return result


        #BOTH OF THESE SOLUTIONS ARE GOOD. Just look slightly different...
        result = []
        if len(nums)==1:
            return [nums[:]]

        for i in range(0, len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(num)
            result.extend(perms)
            nums.append(num)

        return result
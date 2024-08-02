# https://leetcode.com/u/zaid_89/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0:
            return False

        target=total//2
        sumSet = set()

        for i in range(len(nums)-1, -1, -1):
            temp = set()
            for num in sumSet:
                temp.add(nums[i]+num)
            sumSet.update(temp)
            sumSet.add(nums[i])
            
            if target in sumSet:
                return True

        return False
        
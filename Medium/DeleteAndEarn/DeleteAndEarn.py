# https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        #Time: O(nlogn), Space: O(n)
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        secondLastEarn=0
        lastEarn=0

        for i in range(len(nums)):
            currEarn=nums[i]*count[nums[i]]
            temp = lastEarn
            if i>0 and nums[i]==nums[i-1]+1:
                lastEarn = max(currEarn+secondLastEarn, lastEarn)
            else:
                lastEarn += currEarn
            secondLastEarn = temp
        return lastEarn

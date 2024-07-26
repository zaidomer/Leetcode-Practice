# https://leetcode.com/problems/longest-harmonious-subsequence/

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        result = 0
        numDict = Counter(nums)

        for num in nums:
            if num+1 in numDict:
                result = max(result, (numDict[num] + numDict[num+1]))
        
        return result

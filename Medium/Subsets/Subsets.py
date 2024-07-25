# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def backtrack(start:int, curr:List[int]) -> None:
            for i in range(start, len(nums)):
                newCurr = curr[:]
                newCurr.append(nums[i])
                result.append(newCurr)
                backtrack(i+1, newCurr)
                

        backtrack(0, [])
        return result
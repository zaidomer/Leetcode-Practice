# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(0, candidates, [], target, result)
        return result

    def backtrack(self, start:int, candidates: List[int], curr:List[int], target: int, result: List[List[int]]):
        if target==0:
            result.append(curr)
            return
        elif target<0:
            return

        for i in range(start, len(candidates)):
            newCurr=curr[:]
            newCurr.append(candidates[i])
            self.backtrack(i, candidates, newCurr, target-candidates[i], result)
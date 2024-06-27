# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtrack(0, candidates, [], result, target)
        return result

    def backtrack(self, startIndex: int, candidates: List[int], curr: List[int], result: List[List[int]], target: int) -> None:
        if target==0:
            result.append(curr)
            return
        elif target<0:
            return

        for i in range(startIndex, len(candidates)):
            if i>startIndex and candidates[i]==candidates[i-1]:
                continue

            newCurr = curr[:]
            newCurr.append(candidates[i])
            self.backtrack(i+1, candidates, newCurr, result, target-candidates[i])
    
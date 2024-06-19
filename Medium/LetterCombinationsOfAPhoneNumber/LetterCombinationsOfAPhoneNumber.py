# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        self.nums={"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        self.backtrack(digits,"",result)
        return result

    def backtrack(self, digits:str, curr:str, result:List[str]) -> None:
        if len(digits)==0:
            if len(curr)>0:
                result.append(curr)
            return
        
        options = self.nums[digits[0]]
        for j in range(0, len(options)):
            self.backtrack(digits[1:], curr+options[j], result)

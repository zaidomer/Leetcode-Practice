# https://leetcode.com/problems/number-of-senior-citizens/

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        numSeniors = 0
        for person in details:
            if int(person[11:13])>60:
                numSeniors+=1

        return numSeniors

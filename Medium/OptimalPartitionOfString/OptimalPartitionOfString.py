# https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        partitionSet = set()
        result = 1
        for ch in s:
            if ch in partitionSet:
                partitionSet.clear()
                result+=1

            partitionSet.add(ch)
        
        return result

        
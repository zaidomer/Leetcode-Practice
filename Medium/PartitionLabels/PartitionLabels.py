# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        last = {}

        for i in range(len(s)):
            last[s[i]]=i
        
        groupBegin = 0
        groupEnd = 0
        for i in range(len(s)):
            groupEnd = max(groupEnd, last[s[i]])
            if i==groupEnd:
                result.append(groupEnd-groupBegin+1)
                groupBegin = groupEnd+1

        return result
        
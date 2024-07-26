# https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        prevSeq = set()
        left = 0
        result = set()

        for right in range(0, len(s)):
            if (right-left+1)==10:
                curr = s[left:right+1]
                if curr in prevSeq:
                    result.add(curr)
                prevSeq.add(curr)
                left+=1
        
        return result

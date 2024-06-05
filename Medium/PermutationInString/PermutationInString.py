# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        map1=self.genMap(s1,0,len(s1))
        map2=self.genMap(s2, 0, len(s1))
        
        for i in range(0, (len(s2)-len(s1))):
            if map1==map2:
                return True

            map2[ord(s2[i])-ord('a')] = map2[ord(s2[i])-ord('a')]-1
            map2[ord(s2[i+len(s1)])-ord('a')] = map2[ord(s2[i+len(s1)])-ord('a')]+1
        
        return map1==map2

    def genMap(self, s: str, start: int, end: int) -> List[int]:
        arr = [0 for i in range(26)]
        for i in range(start, end):
            arr[ord(s[i])-ord('a')] += 1

        return arr
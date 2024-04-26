class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        
        # map = {}

        # for i in range (0,len(s)):
        #     map[s[i]] = map.get(s[i],0)+1
        
        # for i in range (0,len(t)):
        #     if map.get(t[i]) is None or map.get(t[i])==0:
        #         return False
        #     else:
        #         map[t[i]] = map.get(t[i])-1

        # return True

        map = [0]*26

        for i in range(0,len(s)):
            map[ord(s[i]) - ord('a')] += 1

        for i in range(0,len(t)):
            map[ord(t[i]) - ord('a')]-=1

        for x in map:
            if x!=0:
                return False
        
        return True
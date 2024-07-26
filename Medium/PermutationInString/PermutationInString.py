# https://leetcode.com/problems/permutation-in-string/

class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     if len(s2)<len(s1):
    #         return False

    #     map1=self.genMap(s1,0,len(s1))
    #     map2=self.genMap(s2, 0, len(s1))
        
    #     for i in range(0, (len(s2)-len(s1))):
    #         if map1==map2:
    #             return True

    #         map2[ord(s2[i])-ord('a')] = map2[ord(s2[i])-ord('a')]-1
    #         map2[ord(s2[i+len(s1)])-ord('a')] = map2[ord(s2[i+len(s1)])-ord('a')]+1
        
    #     return map1==map2

    # def genMap(self, s: str, start: int, end: int) -> List[int]:
    #     arr = [0 for i in range(26)]
    #     for i in range(start, end):
    #         arr[ord(s[i])-ord('a')] += 1

    #     return arr




    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     if len(s2)<len(s1):
    #         return False

    #     s1Dict = Counter(s1)
    #     s2Dict = Counter(s2[0:len(s1)])
    #     left = 0
        
    #     for right in range(len(s1), len(s2)):
    #         if s1Dict==s2Dict:
    #             return True
            
    #         s2Dict[s2[left]]-=1
    #         left+=1
    #         s2Dict[s2[right]]+=1

    #     return s1Dict==s2Dict





    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        s1Map = [0 for _ in range(26)]
        s2Map = [0 for _ in range(26)]

        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord('a')] += 1
            s2Map[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(len(s1Map)):
            if s1Map[i]==s2Map[i]:
                matches+=1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches==26:
                return True

            i = ord(s2[right]) - ord('a')
            s2Map[i]+=1
            if s1Map[i]==s2Map[i]:
                matches+=1
            elif s1Map[i]+1==s2Map[i]:
                matches-=1


            i = ord(s2[left]) - ord('a')
            s2Map[i]-=1
            if s1Map[i]==s2Map[i]:
                matches+=1
            elif s1Map[i]-1==s2Map[i]:
                matches-=1

            left+=1

        return matches==26

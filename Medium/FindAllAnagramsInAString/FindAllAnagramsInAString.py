# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # res = []
        # pMap = Counter(p)
        # sMap = Counter(s[0:len(p)])
        # if sMap==pMap:
        #     res.append(0)

        # l=0
        # for r in range(len(p), len(s)):
        #     sMap[s[l]]-=1
        #     sMap[s[r]]+=1
        #     if sMap==pMap:
        #         res.append(l+1)
        #     l+=1
        # return res










        res = []

        def genMap(substring):
            arr = [0 for _ in range(26)]
            for ch in substring:
                arr[ord(ch)-ord('a')]+=1
            return arr

        pMap = genMap(p)
        sMap = genMap(s[0:len(p)])
        l=0
        matches = 0

        for i in range(26):
            if sMap[i]==pMap[i]:
                matches+=1
        if matches==26:
            res.append(0)

        for r in range(len(p), len(s)):
            rightCh = ord(s[r])-ord('a')
            leftCh = ord(s[l])-ord('a')

            sMap[rightCh]+=1
            if sMap[rightCh]==pMap[rightCh]:
                matches+=1
            elif sMap[rightCh]==pMap[rightCh]+1:
                matches-=1

            sMap[leftCh]-=1
            if sMap[leftCh]==pMap[leftCh]:
                matches+=1
            elif sMap[leftCh]==pMap[leftCh]-1:
                matches-=1

            l+=1
            if matches==26:
                res.append(l)
        return res
            
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        #VALID STACK APPROACH
        # stack = deque()
        # res = 0
        
        # for i in range(len(s)):
        #     if stack and stack[-1]=='b' and s[i]=='a':
        #         stack.pop()
        #         res+=1
        #     else:
        #         stack.append(s[i])
        # return res








        #VALID PREFIX APPROACH
        # aCount = 0
        # bCount = 0
        # res = float("inf")

        # for i in range(len(s)):
        #     if s[i]=='a':
        #         aCount += 1
                
        # for i in range(len(s)):
        #     if s[i]=='a':
        #         aCount-=1
        #     res = min(res, bCount+aCount)
        #     bCount += 1 if s[i]=='b' else 0
        
        # return res








        # MOST OPTIMAL
        res = 0
        bCount = 0
        for i in range(len(s)):
            if s[i] == "b":
                bCount += 1
            elif s[i] == "a" and bCount > 0:
                bCount -= 1
                res += 1
        return res

# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        l=0
        r=0

        while r<len(chars):
            count = 1
            while (r+1)<len(chars) and chars[r]==chars[r+1]:
                count+=1
                r+=1
            chars[l]=chars[r]
            l+=1
            if count>1:
                num=str(count)
                for d in num:
                    chars[l]=d
                    l+=1
            r+=1
        
        return l

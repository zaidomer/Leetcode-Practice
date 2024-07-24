# https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        for i in range(min(len(str1),len(str2)), -1, -1):
            curr = str2[0:i+1]

            if len(str1)%(i+1)==0 and len(str2)%(i+1)==0 and (len(str1)//(i+1))*curr==str1 and (len(str2)//(i+1))*curr==str2:
                return curr

        return ""

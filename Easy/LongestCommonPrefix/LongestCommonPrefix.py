# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        # result = ""
        # v = sorted(v)

        # for i in range(0, min(len(v[0]), len(v[len(v)-1]))):
        #     if v[0][i]!=v[len(v)-1][i]:
        #         return result
        #     result+=v[0][i]

        # return result
    







        res = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i==len(word) or strs[0][i]!=word[i]:
                    return res
            res += strs[0][i]
        return res
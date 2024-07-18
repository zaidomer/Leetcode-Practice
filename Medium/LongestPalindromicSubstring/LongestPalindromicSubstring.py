# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     if not s:
    #         return ""

    #     def expand_around_center(s: str, left: int, right: int):
    #         while left >= 0 and right < len(s) and s[left] == s[right]:
    #             left -= 1
    #             right += 1
    #         return right - left - 1


    #     start = 0
    #     end = 0

    #     for i in range(len(s)):
    #         odd = expand_around_center(s, i, i)
    #         even = expand_around_center(s, i, i + 1)
    #         max_len = max(odd, even)
            
    #         if max_len > end - start:
    #             start = i - (max_len - 1) // 2
    #             end = i + max_len // 2
        
    #     return s[start:end+1]

    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(0, len(s)):
            odd = self.expand(s, i-1, i+1)
            even = ""

            if i>0 and s[i]==s[i-1]:
                even = self.expand(s, i-2, i+1)

            curr=""
            if len(odd)>len(even):
                curr=odd
            else:
                curr=even

            if len(curr) > len(result):
                result = curr

        return result

    def expand(self, s:str, left:int, right:int)->str:
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1

        return s[left+1:right]
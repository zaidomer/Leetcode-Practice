#https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        
        map = Counter(s)
        total = 0
        containsOdd = False
        for key in map:
            total += map[key] - map[key]%2
            if map[key]%2==1:
                containsOdd=True

        return total+(0^containsOdd)

# https://leetcode.com/problems/get-equal-substrings-within-budget

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        result = 0
        currCost = 0
        start = 0
        
        for end in range(len(s)):
            currCost += abs(ord(s[end]) - ord(t[end]))
            
            # If the current cost exceeds maxCost, move the start of the window to the right
            while currCost > maxCost:
                currCost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            
            # Update the maximum length of the valid window
            result = max(result, end - start + 1)
        
        return result

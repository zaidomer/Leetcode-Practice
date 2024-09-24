# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        #Time: O(2^n), Space: O(n^2)
        ans = 0
        visited = set()

        def dfs(i):
            nonlocal ans
            if i == len(s): 
                ans = max(ans, len(visited))
                return  
            for j in range(i+1, len(s)+1):    
                if s[i:j] in visited: 
                    continue
                visited.add(s[i:j])
                dfs(j)
                visited.remove(s[i:j])
        
        dfs(0)
        return ans

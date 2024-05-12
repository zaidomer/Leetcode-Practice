# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        map={'(':')', '[':']', '{':'}'}

        for i in range(0, len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(map[s[i]])
            elif len(stack)==0 or stack.pop()!=s[i]:
                return False
        
        return len(stack)==0

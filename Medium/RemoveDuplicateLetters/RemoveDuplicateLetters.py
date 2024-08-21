# https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = deque()
        seen = set()
        lastOcc = {s[i]:i for i in range(len(s))}

        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i]<stack[-1] and i<lastOcc[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(s[i])
                stack.append(s[i])

        return "".join(stack)

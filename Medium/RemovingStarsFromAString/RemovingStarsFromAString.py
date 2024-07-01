# https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()

        for ch in s:
            if ch!='*':
                stack.append(ch)
            elif stack:
                stack.pop()

        return "".join(stack)


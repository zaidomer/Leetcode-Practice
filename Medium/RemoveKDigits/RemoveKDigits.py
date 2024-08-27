# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()

        for i in range(len(num)):
            while stack and stack[-1]>num[i] and k>0:
                stack.pop()
                k-=1
            if stack or num[i]!='0':
                stack.append(num[i])

        for i in range(k):
            if stack:
                stack.pop()
            else:
                break

        return ''.join(stack) if stack else "0"

# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        for ch in s:
            if ch!=']':
                stack.append(ch)
            else:
                curr = ""
                while stack and stack[-1]!='[':
                    curr=stack.pop()+curr
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                stack.append(int(num)*curr)
        return ''.join(stack)

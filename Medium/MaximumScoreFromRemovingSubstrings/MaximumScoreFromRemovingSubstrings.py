# https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        self.s = s

        pair = ""
        maxScore = 0
        minScore = 0

        if x>y:
            pair = "ab"
            maxScore = x
            minScore = y
        else:
            pair = "ba"
            maxScore = y
            minScore = x

        return self.removePair(pair, maxScore) + self.removePair(pair[::-1], minScore)

    def removePair(self, pair, score):
        stack = deque()
        result = 0

        for ch in self.s:
            if ch==pair[1] and stack and stack[-1]==pair[0]:
                stack.pop()
                result+=score
            else:
                stack.append(ch)

        self.s = "".join(stack)
        return result


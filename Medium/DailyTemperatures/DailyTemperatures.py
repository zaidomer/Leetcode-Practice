# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = deque()

        for i in range(len(temperatures)):
            while stack and temperatures[i]>stack[-1][0]:
                temp = stack.pop()
                result[temp[1]] = i-temp[1]
            stack.append((temperatures[i], i))
        return result

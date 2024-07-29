# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minVals = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVals or val<self.minVals[-1]:
            self.minVals.append(val)
        else:
            self.minVals.append(self.minVals[-1])

    def pop(self) -> None:
        self.minVals.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
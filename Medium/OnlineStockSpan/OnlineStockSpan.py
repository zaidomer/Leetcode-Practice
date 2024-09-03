# https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):
        self.history = deque()

    def next(self, price: int) -> int:
        span = 1
        while self.history and self.history[-1][0]<=price:
            span += self.history.pop()[1]
        self.history.append((price,span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# https://leetcode.com/problems/stock-price-fluctuation/

class StockPrice:
    
    #Space: O(n)
    def __init__(self):
        self.latestTime = 0
        self.stockValues = {}
        self.maxHeap = []
        self.minHeap = []

    #Time: O(logn)
    def update(self, timestamp: int, price: int) -> None:
        self.stockValues[timestamp] = price
        if timestamp>self.latestTime:
            self.latestTime = timestamp        
        heappush(self.maxHeap, (-price, timestamp))
        heappush(self.minHeap, (price, timestamp))

    #Time: O(1)
    def current(self) -> int:
        return self.stockValues[self.latestTime]

    #Time: O(logn) average, O(nlogn) worst case
    def maximum(self) -> int:
        while -self.stockValues[self.maxHeap[0][1]]!=self.maxHeap[0][0]:
            heappop(self.maxHeap)
        return -self.maxHeap[0][0]

    #Time: O(logn) average, O(nlogn) worst case
    def minimum(self) -> int:
        while self.stockValues[self.minHeap[0][1]]!=self.minHeap[0][0]:
            heappop(self.minHeap)
        return self.minHeap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if not self.dictionary[key] or self.dictionary[key][0][0]>timestamp:
            return ""

        left = 0
        right = len(self.dictionary[key])-1
        res=""
        while left<=right:
            mid = left+(right-left)//2
            currTime = self.dictionary[key][mid][0]
            currWord = self.dictionary[key][mid][1]

            if currTime==timestamp:
                return currWord
            elif currTime<timestamp:
                res = currWord
                left = mid+1
            else:
                right = mid-1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
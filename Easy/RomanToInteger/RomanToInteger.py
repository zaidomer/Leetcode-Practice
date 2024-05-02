class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        total = 0
        prev = -1
        for ch in s:
            if prev*5==map[ch] or prev*10==map[ch]:
                total -= 2*prev
            total+=map[ch]
            prev = map[ch]

        return total
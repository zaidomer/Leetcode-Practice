# https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #Time: O(n+m), Space: O(n+m)
        count = Counter(s)
        orderChars = set(order)

        res = []

        for ch in order:
            for j in range(count.get(ch, 0)):
                res.append(ch)

        for ch in count:
            if ch not in orderChars:
                for j in range(count[ch]):
                    res.append(ch)

        return ''.join(res)

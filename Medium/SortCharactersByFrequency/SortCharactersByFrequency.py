# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        #REGULAR SORT METHOD O(nlogn)
        # count = Counter(s)
        # order = [(-v,k) for k,v in count.items()]
        # order.sort()
        # res = ""

        # for pair in order:
        #     res += (-1*pair[0])*pair[1]
        # return res







        #BUCKET SORT METHOD O(n)
        count = Counter(s)
        buckets = defaultdict(list)
        res = ""

        for ch,val in count.items():
            buckets[val].append(ch)

        for i in range(len(s), -1, -1):
            for ch in buckets[i]:
                res += i*ch
        return res

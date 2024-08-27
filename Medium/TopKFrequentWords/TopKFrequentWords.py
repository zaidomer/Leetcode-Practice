class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # count = Counter(words)
        # freq = defaultdict(list)

        # for word in count:
        #     freq[count[word]].append(word)

        # res = []
        # for i in range(len(words), -1, -1):
        #     freq[i].sort()
        #     for word in freq[i]:
        #         res.append(word)
        #         if len(res)==k:
        #             return res
        # return res







        count = Counter(words)
        heap = [(-freq, word) for word,freq in count.items()]
        heapify(heap)
        
        res = []
        for i in range(k):
            res.append(heappop(heap)[1])
        return res
        
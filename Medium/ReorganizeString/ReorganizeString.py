# https://leetcode.com/problems/reorganize-string/

class Solution:
    def reorganizeString(self, s: str) -> str:
        # count = Counter(s)
        # heap = [(-freq, ch) for ch,freq in count.items()]
        # heapify(heap)
        # res = ""
        
        # while heap:
        #     freq, mostFreqCh = heappop(heap)
        #     if len(res)==0 or res[-1]!=mostFreqCh:
        #         res+=mostFreqCh
        #     elif heap:
        #         secondFreq, secondMostFreqCh = heappop(heap)
        #         res+=secondMostFreqCh+mostFreqCh
        #         if secondFreq+1<0:
        #             heappush(heap, (secondFreq+1, secondMostFreqCh))
        #     else:
        #         return ""

        #     if freq+1<0:
        #         heappush(heap, (freq+1, mostFreqCh))
        # return res











        count = Counter(s)
        heap = [(-freq, ch) for ch,freq in count.items()]
        heapify(heap)
        res = ""
        prev = None

        while heap or prev:
            if prev and not heap:
                return ""

            freq, char = heappop(heap)
            res += char
            
            if prev:
                heappush(heap, prev)
                prev = None
            
            if freq+1<0:
                prev = (freq+1, char)
            
        return res

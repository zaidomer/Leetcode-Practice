# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heap = []

        numStartingPairs = min(k,len(nums1))
        for i in range(numStartingPairs):
            heap.append([nums1[i] + nums2[0], 0])
        heapify(heap)

        for i in range(k):
            pairSum, n2Index = heappop(heap) 
            n1 = pairSum - nums2[n2Index]
            n2 = nums2[n2Index]

            res.append([n1, n2])

            if n2Index + 1 < len(nums2):
                heappush(heap, [n1 + nums2[n2Index + 1], n2Index + 1])

        return res

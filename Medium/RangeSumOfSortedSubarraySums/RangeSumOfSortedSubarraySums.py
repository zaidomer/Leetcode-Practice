# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # heap = []
        # mod = 10**9+7
        
        # for i in range(len(nums)):
        #     curr = 0
        #     for j in range(i, len(nums)):
        #         curr+=nums[j]
        #         heap.append(curr)
        # heapify(heap)

        # res = 0
        # for i in range(right):
        #     val = heappop(heap)
        #     if i+1>=left:
        #         res = (res+val)%mod
        # return res









        mod = 10**9+7
        res = 0
        heap = [(nums[i], i) for i in range(len(nums))]
        heapify(heap)

        for i in range(right):
            num, index = heappop(heap)
            if i>=left-1:
                res = (res+num)%mod
            if index+1<n:
                newPair = (num+nums[index+1],index+1)
                heappush(heap, newPair)
        return res

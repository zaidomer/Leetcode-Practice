# https://leetcode.com/problems/maximize-happiness-of-selected-children

from heapq import _heapify_max, _heappop_max

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        result = 0
        for i in range(0, k):
            if happiness[i] - i < 0: 
                break
            result += happiness[i] - i
        return result

        # This should be faster in theory but wasnt for leetcode test cases
        # _heapify_max(happiness)
        # result = 0
        # for i in range(0,k):
        #     val = _heappop_max(happiness) - i
        #     if val < 0:
        #         break
        #     else:
        #         result += val

        # return result

# https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # freq = defaultdict(int)
        # count = defaultdict(list)

        # for n in nums:
        #     freq[n]+=1

        # for n in nums:
        #     count[freq[n]].append(n)

        # result = []
        # for i in range(1, len(nums)+1):
        #     if i in count:
        #         count[i].sort(reverse=True)
        #         for num in count[i]:
        #             result.append(num)

        # return result

        freq = Counter(nums)
        nums.sort(key = lambda n: (freq[n], -n))
        return nums

# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # result = []
        # best = Counter(nums).most_common(k)
        # for i in range(0, len(best)):
        #     result.append(best[i][0])
        # return result



        # result = []
        # count={}
        # for i in range(0, len(nums)):
        #     count[nums[i]] = count.get(nums[i], 0)+1
        # heap = [(-value, key) for key, value in count.items()]
        # heapq.heapify(heap)
        # for i in range(0,k):
        #     result.append(heapq.heappop(heap)[1])
        # return result




        result = []
        count={}
        freq=[[] for _ in range(len(nums)+1)]
        
        for i in range(0, len(nums)):
            count[nums[i]] = count.get(nums[i], 0)+1
        
        for num,countValue in count.items():
            freq[countValue].append(num)

        for i in range(len(nums),-1,-1):
            temp = freq[i]
            for j in range(0, len(temp)):
                result.append(temp[j])
                if len(result)==k:
                    return result

        return result
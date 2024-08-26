# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        numDict = defaultdict(int)
        pairs = 0
        for num in nums:
            numDict[num]+=1

        for num in numDict:
            numDict[num]-=1
            if num+k in numDict and numDict[num+k]>0:
                pairs+=1
            numDict[num]+=1

        return pairs

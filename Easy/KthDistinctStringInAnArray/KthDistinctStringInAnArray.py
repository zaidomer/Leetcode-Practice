# https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        words = defaultdict(int)
        for i in range(len(arr)):
            words[arr[i]]+=1
        
        for i in range(len(arr)):
            if words[arr[i]]==1:
                k-=1
            if k==0:
                return arr[i]
        return ""
        
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1

        while l<r:
            val = numbers[r]+numbers[l]
            if val>target:
                r-=1
            elif val<target:
                l+=1
            else:
                return [l+1,r+1]

        return []
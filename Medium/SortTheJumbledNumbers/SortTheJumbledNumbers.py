# https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def convert(num:int) -> int:
            if num==0:
                return mapping[num]
            newNum = 0
            i=0
            while num>0:
                newNum+=mapping[num%10]*10**i
                num=num//10
                i+=1
            return newNum

        ##Do this if not using a custom sort in the sort function, then resturn result
        # numDict=defaultdict(list)
        # for i in range(len(nums)):
        #     numDict[convert(nums[i])].append(nums[i])
        # result = []
        # for key in sorted(numDict.keys()):
        #     result.extend(numDict[key])

        nums.sort(key=convert)
        return nums

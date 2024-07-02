# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # result = []
        # nums1.sort()
        # nums2.sort()
        
        # i1=0
        # i2=0

        # while i1<len(nums1) and i2<len(nums2):
        #     if nums1[i1]==nums2[i2]:
        #         result.append(nums1[i1])
        #         i1+=1
        #         i2+=1
        #     elif nums1[i1]<nums2[i2]:
        #         i1+=1
        #     else:
        #         i2+=1

        # return result

        num1Freq = Counter(nums1)
        result=[]
        
        for i in range(0, len(nums2)):
            if num1Freq.get(nums2[i], 0)>0:
                result.append(nums2[i])
                num1Freq[nums2[i]]-=1

        return result

# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # otherIndecies = {0:[1,2], 1:[0,2], 2:[0,1]}
        # for i in range(3):
        #     found = False
        #     for trio in triplets:
        #         o1 = otherIndecies[i][0]
        #         o2 = otherIndecies[i][1]
        #         if trio[i]==target[i] and trio[o1]<=target[o1] and trio[o2]<=target[o2]:
        #             found = True
        #             break
        #     if not found:
        #         return False
        # return True





        good = set()
        for trio in triplets:
            if trio[0]>target[0] or trio[1]>target[1] or trio[2]>target[2]:
                continue

            for j in range(3):
                if trio[j]==target[j]:
                    good.add(j)

        return len(good)==3

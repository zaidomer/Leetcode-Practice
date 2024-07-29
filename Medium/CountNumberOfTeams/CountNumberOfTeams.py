# https://leetcode.com/problems/count-number-of-teams/

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ## MEMOIZATION BACKTRACK AND CACHE SOLUTION
        # result = 0
        # cache={}

        # def genTeam(smaller:bool, size:int, start:int) -> int:
        #     nonlocal result

        #     if size==3:
        #         return 1
        #     elif (smaller, size, start) in cache:
        #         return cache[(smaller, size, start)]

        #     res = 0
        #     for i in range(start+1, len(rating)):
        #         if (smaller and rating[i]<rating[start]) or (not smaller and rating[i]>rating[start]):
        #             res += genTeam(smaller, size+1, i)

        #     cache[(smaller, size, start)] = res
        #     return res
        
        # for i in range(0, len(rating)-2):
        #     result+=genTeam(True,1,i)
        #     result+=genTeam(False,1,i)

        # return result





        ## GREEDY MOST EFFICIENT SOLUTION
        result = 0
        for i in range(1, len(rating)-1):
            numSmaller = 0
            numLarger = 0

            for j in range(i-1, -1, -1):
                if rating[j]<rating[i]:
                    numSmaller+=1
            
            for j in range(i+1, len(rating)):
                if rating[j]>rating[i]:
                    numLarger+=1

            result += numSmaller*numLarger
            result += (i-numSmaller)*(len(rating)-i-1-numLarger)

        return result

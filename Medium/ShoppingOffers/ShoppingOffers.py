# https://leetcode.com/problems/shopping-offers/

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        #Time: O(2^n), Space: O(2^n)
        cache = {}

        def dfs(curr):
            if curr==needs:
                return 0
            elif tuple(curr) in cache:
                return cache[tuple(curr)]
            else:
                for i in range(len(curr)):
                    if curr[i]>needs[i]:
                        return float("inf")

            res = 0
            for i in range(len(curr)):
                res += price[i] * (needs[i]-curr[i]) 

            #specials
            for j in range(len(special)):
                temp = curr[:]
                for k in range(len(special[j])-1):
                    temp[k]+=special[j][k]
                res = min(res, special[j][-1]+dfs(temp))
            
            cache[tuple(curr)]=res
            return res

        currItems = [0 for _ in range(len(needs))]
        return dfs(currItems)

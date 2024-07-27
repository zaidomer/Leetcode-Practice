# https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        l=0
        r=len(people)-1

        people.sort()

        while l<=r:
            if (people[r]+people[l])<=limit:
                l+=1
            r-=1
            result+=1

        return result

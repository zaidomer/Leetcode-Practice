# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        result=0
        currNumFruits=0
        count = defaultdict(int)

        for right in range(0, len(fruits)):
            count[fruits[right]] += 1
            currNumFruits+=1

            while len(count)>2:
                fruitRemoved = fruits[left]
                currNumFruits-=1
                count[fruitRemoved]-=1
                left+=1

                if count[fruitRemoved]==0:
                    count.pop(fruitRemoved)
            
            result = max(result, currNumFruits)

        return result

        
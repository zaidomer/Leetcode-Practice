# https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1:
            return (flowerbed[0]==0)>=n

        numFlowers = 0
        numEmpty = 0

        for i in range(0, len(flowerbed)):
            if flowerbed[i]==0:
                numEmpty+=1
            else:
                numEmpty = 0

            if numEmpty==3 or (numEmpty==2 and (i==1 or i==len(flowerbed)-1)):
                numEmpty=1
                numFlowers+=1

        return numFlowers >= n


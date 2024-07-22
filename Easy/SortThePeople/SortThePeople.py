# https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nameHeightMap = {}
        for i in range(len(names)):
            nameHeightMap[heights[i]] = names[i]

        result = []
        heights.sort(reverse=True)

        for i in range(len(heights)):
            result.append(nameHeightMap[heights[i]])

        return result
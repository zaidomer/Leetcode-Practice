# https://leetcode.com/problems/relative-sort-array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        map = {}
        result = []

        for i in range(0, len(arr1)):
            map[arr1[i]] = map.get(arr1[i], 0)+1

        for j in range(0, len(arr2)):
            for x in range(0, map[arr2[j]]):
                result.append(arr2[j])
            map.pop(arr2[j])

        remaining = []

        for key in map:
            for i in range(0, map[key]):
                remaining.append(key)

        remaining.sort()
        result.extend(remaining)
        return result
# https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        result = 0
        cityFreq = {}
        for i in range(0, len(roads)):
            cityFreq[roads[i][0]] = cityFreq.get(roads[i][0], 0)+1
            cityFreq[roads[i][1]] = cityFreq.get(roads[i][1], 0)+1

        cityFreq = {k: v for k, v in sorted(cityFreq.items(), key=lambda item: item[1], reverse=True)}

        for key,value in cityFreq.items():
            cityFreq[key] = n
            n-=1

        for i in range(0, len(roads)):
            result += cityFreq[roads[i][0]] + cityFreq[roads[i][1]]

        return result

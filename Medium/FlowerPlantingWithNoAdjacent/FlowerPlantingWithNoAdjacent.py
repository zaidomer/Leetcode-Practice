# https://leetcode.com/problems/flower-planting-with-no-adjacent/

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        #Time: O(N+E), Space: O(N+E)
        graph = defaultdict(list)
        for a,b in paths:
            graph[a].append(b)
            graph[b].append(a)
        res = [0 for _ in range(n)]

        for i in range(1, n+1):
            neighbourFlowers = set()
            for nei in graph[i]:
                neighbourFlowers.add(res[nei-1])
            flower = 1
            while flower in neighbourFlowers:
                flower=flower+1
            res[i-1]=flower

        return res

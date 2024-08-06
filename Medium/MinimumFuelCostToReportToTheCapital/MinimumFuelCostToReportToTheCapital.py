# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        res = 0

        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, prev):
            nonlocal res
            passengers=0
            for nei in graph[node]:
                if nei!=prev:
                    neiPassengers = dfs(nei,node)
                    passengers += neiPassengers
                    res += int(ceil(neiPassengers/seats))
            return passengers+1

        dfs(0, -1)
        return res

# https://leetcode.com/problems/detonate-the-maximum-bombs/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        #Time: O(n^2), Space: O(n^2) 
        
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i==j:
                    continue
                if sqrt((bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2) <= bombs[i][2]:
                    graph[i].append(j)

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in graph[node]:
                dfs(nei)

        res = 0
        allVisited = set()
        for i in range(len(bombs)):
            visit = set()
            if i not in allVisited:
                dfs(i)
                res = max(res, len(visit))
            allVisited = allVisited.union(visit)
        return res

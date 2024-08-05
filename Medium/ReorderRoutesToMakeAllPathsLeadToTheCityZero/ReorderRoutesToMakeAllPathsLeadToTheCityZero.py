# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ## VALID DFS APPROACH
        # graph = defaultdict(list)
        # for edge in connections:
        #     graph[edge[0]].append(edge[1])
        #     graph[edge[1]].append(edge[0])

        # result = 0
        # visit = set()
        # edges = {(a,b) for a,b in connections}

        # def dfs(node):
        #     nonlocal result
        #     for nei in graph[node]:
        #         if nei in visit:
        #             continue
        #         if (nei,node) not in edges:
        #             result+=1
        #         visit.add(nei)
        #         dfs(nei)

        # visit.add(0)
        # dfs(0)
        # return result










        ## VALID BFS APPROACH
        graph = defaultdict(list)
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)

        edgeSet = {(a,b) for a,b in connections}

        result = 0
        visit = set()
        q = deque([0])

        while q:
            node = q.popleft()
            visit.add(node)
            for nei in graph[node]:
                if nei in visit:
                    continue
                if (node, nei) in edgeSet:
                    result+=1
                q.append(nei)
        return result

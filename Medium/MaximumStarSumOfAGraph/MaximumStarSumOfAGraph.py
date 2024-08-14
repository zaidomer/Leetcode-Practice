class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # graph = defaultdict(list)
        # for a,b in edges:
        #     graph[a].append((vals[b],b))
        #     graph[b].append((vals[a],a))
        # visit = set()

        # for i in range(len(graph)):
        #     graph[i].sort(reverse=True)

        # def dfs(node):    
        #     if node in visit:
        #         return res
        #     visit.add(node)
        #     currScore = vals[node]
        #     for i in range(min(k, len(graph[node]))):
        #         if graph[node][i][0]<=0:
        #             break
        #         currScore+=graph[node][i][0]

        #     for nei in graph[node]:
        #         currScore = max(currScore, dfs(nei[1]))
        #     return currScore

        # res = float("-inf")
        # for i in range(len(vals)):
        #     if i not in visit:
        #         res = max(res, dfs(i))
        # return res
            

        











        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        res = max(vals)
        for node in range(len(vals)):
            heap = []
            total = vals[node]
            for nei in graph[node]:
                if vals[nei]<=0:
                    continue
                total+=vals[nei]
                heappush(heap, vals[nei])
                if len(heap)>k:
                    total-=heappop(heap)
            res = max(res, total)
        return res
        
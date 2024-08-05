# https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph = defaultdict(list)
        # for edge in times:
        #     graph[edge[0]].append([edge[1],edge[2]])
        
        # q = deque([[k, 0]])
        # visit = {}
        # visit[k]=0
        # while q:
        #     for i in range(len(q)):
        #         node, currCost = q.popleft()
        #         for edge in graph[node]:
        #             if edge[0] not in visit or currCost+edge[1]<=visit[edge[0]]:
        #                 q.append([edge[0], currCost+edge[1]])
        #                 visit[edge[0]] = min(visit.get(edge[0],float("inf")), currCost+edge[1])

        # if len(visit)!=n:
        #     return -1

        # cost = -1
        # for val in visit.values():
        #     cost = max(cost, val)
        # return cost      












        graph = defaultdict(list)
        for edge in times:
            graph[edge[0]].append((edge[1],edge[2]))
        heap = [(0,k)]
        result = 0
        visit = set()

        while heap:
            cost, node = heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            result = cost

            for nei,weight in graph[node]:
                if nei not in visit:
                    heappush(heap, (cost+weight, nei))

        return result if len(visit)==n else -1
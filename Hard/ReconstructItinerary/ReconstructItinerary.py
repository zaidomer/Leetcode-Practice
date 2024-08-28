# https://leetcode.com/problems/reconstruct-itinerary/

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # graph = defaultdict(list)
        # visit = defaultdict(int)
        # for src,dst in tickets:
        #     graph[src].append(dst)
        #     visit[(src,dst)]+=1
        # stack = deque()
        # res = []

        # for airport in graph:
        #     graph[airport].sort()
        
        # def dfs(node):
        #     stack.append(node)
        #     if len(stack)==len(tickets)+1:
        #         return True
            
        #     for nei in graph[node]:
        #         if visit[(node, nei)] > 0:
        #             visit[(node, nei)]-=1
        #             if dfs(nei):
        #                 return True
        #             visit[(node, nei)]+=1
        #     stack.pop()
        #     return False
            
        # dfs("JFK")
        # return list(stack)








        graph = defaultdict(deque) 
        tickets.sort()
        for src, dst in tickets:
            graph[src].append(dst)

        itinerary = []
        def dfs(node):
            while graph[node]:
                nei = graph[node].popleft()
                dfs(nei)
            itinerary.append(node)

        dfs("JFK")
        return itinerary[::-1]
        
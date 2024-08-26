# https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        n = len(rooms)
        
        def dfs(currRoom):
            if currRoom in visit:
                return
            visit.add(currRoom)
            for nei in rooms[currRoom]:
                dfs(nei)
        
        dfs(0)
        return len(visit)==n

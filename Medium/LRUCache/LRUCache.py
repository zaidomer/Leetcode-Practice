# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1

#         self.cache[key] = self.cache.pop(key)
#         return self.cache[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache.pop(key)

#         self.cache[key] = value
#         if len(self.cache) > self.capacity:
#             self.cache.pop(next(iter(self.cache)))













class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        #left = least recently used, right=most recently used
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # insert node at right
    def insert(self, node):
        mostRecent = self.right.prev
        mostRecent.next = node
        node.prev = mostRecent
        node.next = self.right
        self.right.prev = node

    # remove node from list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lruNode = self.left.next
            self.remove(lruNode)
            self.cache.pop(lruNode.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
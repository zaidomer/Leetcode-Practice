# https://leetcode.com/problems/implement-trie-prefix-tree/

class Node:
    def __init__(self, isEnd=False):
        self.isEnd = isEnd
        self.children = [None for _ in range(26)]

class Trie:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            i = ord(c)-ord('a')
            if curr.children[i] is None:
                curr.children[i] = Node()
            curr = curr.children[i]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            i = ord(c)-ord('a')
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            i = ord(c)-ord('a')
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
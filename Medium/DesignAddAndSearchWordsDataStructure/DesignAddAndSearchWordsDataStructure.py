# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        curr = self.head
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=Node()
            curr = curr.children[ch]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def trieSearch(i, curr) -> bool:
            if i==len(word):
                return curr.isEnd
            elif word[i]=='.':
                for ch in curr.children:
                    if trieSearch(i+1, curr.children[ch]):
                        return True
            elif word[i] in curr.children:
                return trieSearch(i+1, curr.children[word[i]])
            return False
                    
        return trieSearch(0, self.head)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
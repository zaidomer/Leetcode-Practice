# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        #Time: O(n+m), Space: O(n), where n=num digits in all arr1 numbers, m=num digits in all arr2 numbers
        trie = Node()
        for num in arr1:
            val = str(num)
            temp = trie
            for ch in val:
                if ch not in temp.children:
                    temp.children[ch]=Node()
                temp = temp.children[ch]
            temp.isEnd = True

        res = 0
        for num in arr2:
            val = str(num)
            temp = trie
            count = 0
            for ch in val:
                if ch in temp.children:
                    temp = temp.children[ch]
                    count+=1
                else:
                    break
            res = max(res, count)
        return res

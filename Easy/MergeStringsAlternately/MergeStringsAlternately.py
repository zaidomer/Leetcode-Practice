# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        for i in range(0, min(len(word1), len(word2))):
            result += word1[i]
            result += word2[i]

        if len(word1)>len(word2):
            result += word1[len(word2):]
        elif len(word2)>len(word1):
            result += word2[len(word1):]

        return result

        
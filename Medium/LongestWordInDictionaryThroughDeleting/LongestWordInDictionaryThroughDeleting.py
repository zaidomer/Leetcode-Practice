# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result = ""
        for word in dictionary:
            if len(word)<len(result) or (len(word)==len(result) and word>result):
                continue
            sPtr = 0
            wrdPtr = 0
            while wrdPtr<len(word) and sPtr<len(s):
                if word[wrdPtr]==s[sPtr]:
                    wrdPtr+=1
                sPtr+=1
            if wrdPtr==len(word):
                result = word
        return result

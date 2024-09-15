# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        masks = []
        for i in range(len(words)):
            num = 0
            for ch in words[i]:
                num|=1<<(ord(ch)-ord('a'))
            masks.append(num)

        for i in range(len(masks)):
            for j in range(i+1, len(masks)):
                if masks[i]&masks[j]==0:
                    res = max(res, len(words[i])*len(words[j]))
        return res

# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        balance = 1
        nodes = preorder.split(',')
        for node in nodes:
            if balance<=0:
                return False
            if node=='#':
                balance-=1
            else:
                balance+=1
        return balance==0

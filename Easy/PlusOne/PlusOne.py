# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        
        for i in range(len(digits)-1, -1, -1):
            add = digits[i] + carry
            digits[i] = add%10
            carry = add//10
            if not carry:
                break

        if carry:
            digits.insert(0, 1)

        return digits
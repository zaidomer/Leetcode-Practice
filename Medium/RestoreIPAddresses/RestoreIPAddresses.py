# https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #Time: O(1) because of constrained size and #combos, Space: O(n) where n is all combos of '.' placements
        if len(s)<4 or len(s)>12:
            return []
        res = []

        def dfs(i, nums):
            if i==len(s):
                return

            if len(nums)==3:
                numStr=s[i:]
                num=int(numStr)
                if (numStr[0]=='0' and len(numStr)==1) or (numStr[0]!='0' and num<=255):
                    nums.append(numStr)
                    res.append('.'.join(nums))
            elif s[i]=='0':
                temp = nums[:]
                temp.append(s[i])
                dfs(i+1, temp)
            else:
                for j in range(i+1, len(s)):
                    numStr=s[i:j]
                    num=int(numStr)
                    if num>255:
                        return
                    else:
                        temp = nums[:]
                        temp.append(numStr)
                        dfs(j, temp)

        dfs(0, [])
        return res

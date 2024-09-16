# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #Time: O(n), Space: O(n) worst case, much smaller on average. Here, n is # of revisions
        v1=0
        v2=0

        while v1<len(version1) or v2<len(version2):
            num1 = ['0']
            while v1<len(version1) and version1[v1]!='.':
                num1.append(version1[v1])
                v1+=1

            num2 = ['0']
            while v2<len(version2) and version2[v2]!='.':
                num2.append(version2[v2])
                v2+=1

            v1+=1
            v2+=1
            
            num1Int = int(''.join(num1))
            num2Int = int(''.join(num2))
            if num1Int>num2Int:
                return 1
            elif num1Int<num2Int:
                return -1
        
        return 0

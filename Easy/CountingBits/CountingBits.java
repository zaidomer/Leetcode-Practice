//https://leetcode.com/problems/counting-bits/

class Solution {
    public int[] countBits(int n) {
        int ans[] = new int[n+1];
        ans[0] = 0;
        int oldIndex = 1;
        int newCountPoint = 1;
        for(int i = 1; i < n+1; i++){     
            if(i==newCountPoint){
                ans[i] = 1;
                oldIndex = 1;
                newCountPoint*=2;
            }else{
                ans[i] = 1+ans[oldIndex];
                oldIndex++;
            }

        }
        return ans;
    }
}

//0       0
//1       1

//10      2
//11      3

//100     4
//101     5
//110     6
//111     7

//1000    8 
//1001    9
//1010    10
//1011    11
//1100    12
//1101    13
//1110    14
//1111    15

//10000   16
//10001   17
//10010   18
//10011   19
//10100   20
//10101   21
//10110   22
//10111   23
//11000   24
//11001   25
//11010   26
//11011   27
//11100   28
//11101   29
//11110   30
//11111   31

// https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution {
public:
    int minBitFlips(int start, int goal) {
        int diff = start^goal;
        int result=0;
        while(diff>0){
            result+=diff&1;
            diff=diff>>1;
        } 
        return result;
    }
};
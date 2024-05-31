// https://leetcode.com/problems/single-number-iii/

class Solution {
public:
    int getBit(int x, int k) {
        return (x >> k) & 1;
    }

    vector<int> singleNumber(vector<int>& nums) {
        int xorXY = 0;
        for (int i = 0; i < nums.size(); i++){
            xorXY ^= nums[i];
        }

        int pos = 0;
        while (!getBit(xorXY, pos)){
            pos++;
        }

        int x = 0;
        for (int i = 0; i < nums.size(); i++){
            if (getBit(nums[i], pos)){
                x ^= nums[i];
            }
        }
        
        int y = xorXY ^ x;
        return {x, y};
    }
};
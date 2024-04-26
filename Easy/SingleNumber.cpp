//https://leetcode.com/problems/single-number/description/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        // std::unordered_set<int> set;

        // for(int i = 0; i < nums.size(); i++){
        //     if(set.find(nums[i]) == set.end()){
        //         set.insert(nums[i]);
        //     }else{
        //         set.erase(nums[i]);
        //     }
        // }

        // return *set.begin();

        int result = 0;

        for(int i = 0; i < nums.size(); i++){
            result = result ^ nums[i];
        }

        return result;
    }
};
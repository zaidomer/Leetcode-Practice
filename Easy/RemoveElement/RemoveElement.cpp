// https://leetcode.com/problems/remove-element/

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        // int left = 0;
        // int right = nums.size()-1;
        
        // while(left<=right){
        //     while(right>left && nums[right]==val){
        //         right--;
        //     }

        //     if(nums[right]==val){
        //         return left;
        //     }

        //     if(left<right && nums[left]==val){
        //         nums[left] = nums[right];
        //         nums[right]=val;
        //     }
        //     left++;
        // }

        // return left;



        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[count] = nums[i];
                count++;
            }
        }
        return count;

    }
};
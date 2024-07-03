// https://leetcode.com/problems/minimize-maximum-of-array/

class Solution {
public:
    int minimizeArrayValue(vector<int>& nums) {
        /*
        first term is the initial limiting factor. Start with first term, add 1 term at a time with loop. The max
        value will be the max average of the sum over all terms in the window. Window size increases 1 at a time. 
        */

        int result = nums[0];
        long sum = nums[0];
        for(int i = 1; i < nums.size(); i++){
            sum+=nums[i];
            /*
            second term just a more efficient way to round up the average ratehr than using ceil. 
            Its same as (int)(ceil((1.0*sum)/(i+1))). Average is rounded up because 1 number in  
            the array will need to take on the extra value, which will effect the max.
            */
            result = max(result, (int)(sum/(i+1) + (sum%(i+1)==0?0:1)));
        }
        return result;
    }
};


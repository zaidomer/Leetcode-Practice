//https://leetcode.com/problems/two-sum/

// class Solution {
//     public int[] twoSum(int[] nums, int target) {
//         int[] result = new int[2];
//         for(int i = 0; i < nums.length; i++){
//             for(int j = i+1; j < nums.length; j++){
//                 if((target-nums[i])==nums[j]){
//                     result[0] = i;
//                     result[1] = j;
//                     return result;
//                 }
//             }
//         }
//         return result;
//     }
// }

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        int n = nums.length;

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (numMap.containsKey(complement)) {
                return new int[] { numMap.get(complement), i };
            }
            numMap.put(nums[i], i);
        }

        return new int[] {};
    }
}
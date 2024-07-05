// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        vector<int> result;
        sort(potions.begin(), potions.end());

        for(int i = 0; i < spells.size(); i++){
            long minPotionStrength = success/spells[i] + (success%spells[i]==0?0:1);
            int indexOfMin = binarySearch(minPotionStrength, potions);
            result.push_back(potions.size() - indexOfMin);
        }
        return result;
    }

    int binarySearch(long target, vector<int>& arr){
        int left = 0;
        int right = arr.size()-1;
        int mid = 0;
        int result = arr.size();

        while(left<=right){
            mid = left+(right-left)/2;
            if(arr[mid]>=target){
                result = mid;
                right = mid-1;
            }else{
                left = mid+1;
            }
        }
        return result;
    }
};


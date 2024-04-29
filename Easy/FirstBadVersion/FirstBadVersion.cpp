//https://leetcode.com/problems/first-bad-version/

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int start = 1;
        int mid = 1;
        int end = n;
        bool current;

        while(start <= end){
            mid = start + (end-start)/2;
            current = isBadVersion(mid);
            if(current && !isBadVersion(mid-1)){
                return mid;
            }else if(current){
                end = mid-1;
            }else{
                start = mid+1;
            }
        }

        return 1;
    }
};
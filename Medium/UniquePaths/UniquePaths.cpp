// https://leetcode.com/problems/unique-paths/description/

class Solution {
public:
    int uniquePaths(int m, int n) {
        int totalMoves = m+n-2;
        long long result = 1;

        int smallerMoves = min(m,n)-1;

        for(int i = 1; i<=smallerMoves; i++){
            result*=(totalMoves+1-i);
            result/=i;
        }
        return result;
    }

    // int uniquePaths(int m, int n) {
    //     int result = 0;
    //     int currM = 0;
    //     int currN = 0;
    //     traverse(currM, currN, m, n, result);
    //     return result;
    // }

    // void traverse(int currM, int currN, int m, int n, int &result){
    //     if(currM < m-1){
    //         traverse(currM+1, currN, m, n, result);
    //     }
    //     if(currN < n-1){
    //         traverse(currM, currN+1, m, n, result);
    //     }

    //     if(currM==m-1 && currN==n-1){
    //         result+=1;
    //     }
    // }
};
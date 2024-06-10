// https://leetcode.com/problems/height-checker/

class Solution {
public:
    int heightChecker(vector<int>& heights) {
        int count = 0;
        // vector<int> sorted = heights;
        // sort(sorted.begin(), sorted.end());
        // for(int i = 0; i < heights.size(); i++){
        //     if(heights[i] != sorted[i]){
        //         count++;
        //     }
        // }
        // return count;

        map<int,int> heightMap;
        for(int i = 1; i <= 100; i++){
            heightMap[i]=0;
        }

        for(int i = 0; i < heights.size(); i++){
            heightMap[heights[i]]+=1;
        }

        auto j = heightMap.begin();
        for(int i = 0; i < heights.size(); i++){
            while(j->second == 0 && j != heightMap.end()){
                j++;
            }

            j->second -= 1;
            if(heights[i] != j->first){
                count++;
            }
        }

        return count;
    }
};
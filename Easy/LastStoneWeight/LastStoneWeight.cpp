// https://leetcode.com/problems/last-stone-weight/

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> q;

        for(int i = 0; i < stones.size(); i++){
            q.push(stones[i]);
        }

        while(q.size()>1){
            int num1 = q.top();
            q.pop();
            int num2 = q.top();
            q.pop();
            int result = num1-num2;

            if(result!=0){
                q.push(result);
            }
        }

        return q.size()*q.top();
    }
};
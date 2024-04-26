class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int result = 0;
        int min = prices[0];
        int potential = 0;
        
        for(int i = 1; i < prices.size(); i++){
            if(prices[i] < min){
                min = prices[i];
            }
            potential = prices[i]-min;
            if(potential>result){
                result = potential;
            }
        }
        return result;
    }
};
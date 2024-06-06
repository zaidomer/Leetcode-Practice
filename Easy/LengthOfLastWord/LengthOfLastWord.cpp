// https://leetcode.com/problems/length-of-last-word/description/

class Solution {
public:
    int lengthOfLastWord(string s) {
        int result = 0;
        for(int i = s.size()-1; i>=0; i--){
            if(s[i] != ' ' || (i==0 && result==0)){
                result+=1;
            }else if(result>0){
                break;
            }
        }
        return result;
    }
};
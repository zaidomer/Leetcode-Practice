// https://leetcode.com/problems/backspace-string-compare/

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        return format(s)==format(t);
    }

    string format(string str){
        string result = "";
        for(int i = 0; i<str.length(); i++){
            if(str[i]!='#'){
                result.push_back(str[i]);
            }else if(result.length()>0){
                result.pop_back();
            }
        }

        return result;
    }
};
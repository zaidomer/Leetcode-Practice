// https://leetcode.com/problems/find-common-characters/

class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<string> result;
        vector<int> resultMap(26,INT_MAX);

        for(int i = 0; i < words.size(); i++){
            vector<int> wordMap(26,0);

            for(int j = 0; j < words[i].size(); j++){
                wordMap[words[i][j] - 'a'] += 1;
            }
            
            for(int j = 0; j < 26; j++){
                resultMap[j] = min(resultMap[j], wordMap[j]);
            }
        }
        
        for(int i = 0; i < 26; i++){
            for(int j = resultMap[i]; j > 0; j--){
                string s(1, (char)(i+(int)('a')));
                result.push_back(s);
            }
        }
            
        return result;
    }
};


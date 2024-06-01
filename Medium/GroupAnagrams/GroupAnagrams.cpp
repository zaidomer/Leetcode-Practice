// https://leetcode.com/problems/group-anagrams/

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> wordMap;
        for(int i = 0; i < strs.size(); i++){
            string tempWord = strs[i];
            std::sort(tempWord.begin(), tempWord.end());
            wordMap[tempWord].push_back(strs[i]);
        }

        for (auto it = wordMap.begin(); it != wordMap.end(); it++){
            result.push_back(it->second);
        }
        return result;
    }

};
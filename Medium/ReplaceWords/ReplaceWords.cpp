// https://leetcode.com/problems/replace-words

class Solution
{
public:
    struct compare_length
    {
        bool operator()(const std::string &l, const std::string &r) const
        {
            return l.size() < r.size();
        }
    };

    string replaceWords(vector<string> &dictionary, string sentence)
    {
        vector<string> words;
        stringstream ss(sentence);
        string s;

        while (getline(ss, s, ' '))
        {
            words.push_back(s);
        }
        std::sort(dictionary.begin(), dictionary.end(), compare_length());

        for (int i = 0; i < words.size(); i++)
        {
            for (int j = 0; j < dictionary.size(); j++)
            {
                if (dictionary[j].size() <= words[i].size() && words[i].substr(0, dictionary[j].size()) == dictionary[j])
                {
                    words[i] = dictionary[j];
                }
            }
        }

        string result = "";

        for (int i = 0; i < words.size(); i++)
        {
            result += words[i];
            if (i != words.size() - 1)
            {
                result += " ";
            }
        }

        return result;
    }
};
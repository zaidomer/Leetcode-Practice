// https://leetcode.com/problems/3sum/description/

class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        std::vector<vector<int>> answer;
        sort(nums.begin(), nums.end());
        if (nums.size() < 3)
        {
            return answer;
        }
        else if (nums[0] > 0)
        {
            return answer;
        }

        std::unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++)
        {
            map[nums[i]] = i;
        }

        for (int i = 0; i < nums.size() - 2; i++)
        {
            if (nums[i] > 0)
            {
                break;
            }

            for (int j = i + 1; j < nums.size() - 1; j++)
            {
                int target = -1 * (nums[i] + nums[j]);
                auto it = map.find(target);
                if (it != map.end() && it->second > j)
                {
                    answer.push_back({nums[i], nums[j], target});
                }
                j = map.find(nums[j])->second;
            }
            i = map.find(nums[i])->second;
        }

        return answer;
    }
};
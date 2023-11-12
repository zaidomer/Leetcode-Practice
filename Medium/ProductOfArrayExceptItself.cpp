// https://leetcode.com/problems/product-of-array-except-self/description/

class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        int n = nums.size();
        std::vector<int> result(n, 1);

        int left = 1;
        int right = 1;

        // Calculate the product of all elements to the left and right of each element
        for (int i = 0; i < n; i++)
        {
            result[i] *= left;
            left *= nums[i];

            result[n - 1 - i] *= right;
            right *= nums[n - 1 - i];
        }

        return result;
    }
};
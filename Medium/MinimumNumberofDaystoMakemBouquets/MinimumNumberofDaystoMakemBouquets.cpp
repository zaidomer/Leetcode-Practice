// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution
{
public:
    int minDays(vector<int> &bloomDay, int m, int k)
    {
        if ((long long)(m)*k > bloomDay.size())
        {
            return -1;
        }

        int left = 0;
        int right = 1e9;
        int mid = -1;

        while (left <= right)
        {
            mid = left + (right - left) / 2;
            if (canMakeGroup(bloomDay, m, k, mid))
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }

        return left;
    }

    bool canMakeGroup(vector<int> arr, int m, int k, int day)
    {
        int total = 0;
        for (int i = 0; i < arr.size(); i++)
        {
            int count = 0;
            while (i < arr.size() && count < k && arr[i] <= day)
            {
                count++;
                i++;
            }

            if (count == k)
            {
                total++;
                i--;
            }

            if (total >= m)
            {
                return true;
            }
        }
        return false;
    }
};

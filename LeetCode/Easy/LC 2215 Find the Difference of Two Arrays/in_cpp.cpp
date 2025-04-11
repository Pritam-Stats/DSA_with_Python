#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<vector<int>> findDifference(vector<int> &nums1, vector<int> &nums2)
{
    set<int> set1(nums1.begin(), nums1.end());
    set<int> set2(nums2.begin(), nums2.end());

    vector<int> onlyInNums1;
    vector<int> onlyInNums2;

    for (int num : set1)
    {
        if (set2.find(num) == set2.end())
        {
            onlyInNums1.push_back(num);
        }
    }

    for (int num : set2)
    {
        if (set1.find(num) == set1.end())
        {
            onlyInNums2.push_back(num);
        }
    }

    return {onlyInNums1, onlyInNums2};
}

void printResult(const vector<vector<int>> &result)
{
    for (const auto &group : result)
    {
        cout << "[";
        for (size_t i = 0; i < group.size(); ++i)
        {
            cout << group[i];
            if (i + 1 < group.size())
                cout << ", ";
        }
        cout << "] ";
    }
    cout << endl;
}

int main()
{
    vector<int> nums1a = {1, 2, 3};
    vector<int> nums2a = {2, 4, 6};

    vector<int> nums1b = {1, 2, 3, 3};
    vector<int> nums2b = {1, 1, 2, 2};

    auto result1 = findDifference(nums1a, nums2a);
    auto result2 = findDifference(nums1b, nums2b);

    printResult(result1); // Expected: [[1, 3], [4, 6]]
    printResult(result2); // Expected: [[3], []]

    return 0;
}

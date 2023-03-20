class Solution {
public:
    /// the main idea is that we wanna skip identical elements before adding them to the subsets
    /// its easy to keep track of this by sorting the whole array at first
    /// Time complexity: O(N * 2^N), since it takes average O(N) to append a new subset to final answer.
    void backtracking(vector<vector<int>>& ans, vector<int> curr_set, int start, vector<int>& nums)
    {
        ans.push_back(curr_set);
        for(int i = start; i < nums.size(); ++i)
        {
            if (i == start || (i != start && nums[i] != nums[i-1]) ) {
                curr_set.push_back(nums[i]);
                backtracking(ans, curr_set, i+1, nums);
                curr_set.pop_back();
            }
        }
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        backtracking(ans, vector<int>(), 0, nums);
        for(auto v : ans)
        {
            for(int i : v) cout << i << " ";
            cout << endl;
        }
        return ans;
    }
};

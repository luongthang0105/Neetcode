class Solution {
public:
    void backtracking(vector<vector<int>>& ans, vector<int> curr_set, int start, vector<int>& nums)
    {
        ans.push_back(curr_set);
        for(int i = start; i < nums.size(); ++i)
        {
            curr_set.push_back(nums[i]);
            backtracking(ans, curr_set, i+1, nums);
            curr_set.pop_back();
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        backtracking(ans, vector<int>(), 0, nums);
        return ans;
    }
};

class Solution {
public:
    ///Time complexity: O(N * N!)
    void backtrack(vector<vector<int>>& ans, vector<bool>& check, vector<int>& curr, vector<int>& nums)
    {
        for(int i = 0; i < nums.size(); ++i)
        {
            if(check[i]) continue;
            check[i] = 1;
            curr.push_back(nums[i]);
            if(curr.size() == nums.size())
            {
                ans.push_back(curr);
                check[i] = 0;
                curr.pop_back();
                return;
            }
            else backtrack(ans, check, curr, nums);
            check[i] = 0;
            curr.pop_back();
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<bool> check(nums.size(), 0);
        vector<int> curr;
        backtrack(ans, check, curr, nums);
        return ans;
    }
};

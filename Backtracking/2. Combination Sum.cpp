class Solution {
public:
    void backtrack(vector<vector<int>>& ans, vector<int>& curr_set, int& start, vector<int>& candidates, int& target, int& curr_sum)
    {
        for(int j = start; j < candidates.size(); ++j)
        {
            int i = candidates[j];
            if(curr_sum + i > target) return;
            curr_set.push_back(i);
            curr_sum += i;
            if(curr_sum == target)
                ans.push_back(curr_set);
            else backtrack(ans, curr_set, j, candidates, target, curr_sum);
            curr_sum -= i;
            curr_set.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> ans;
        vector<int> v;
        int start, curr_sum;
        start = curr_sum = 0;
        backtrack(ans, v, start, candidates, target, curr_sum);
        return ans;
    }
};

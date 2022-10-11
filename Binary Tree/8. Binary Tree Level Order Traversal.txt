/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if(root == NULL) return ans;
        queue< pair<TreeNode*, int>> q;
        q.push({root, 1});
        while(q.size() != 0){
            auto u = q.front();
            q.pop();
            if(u.second > ans.size()) 
            {
                vector<int> temp; temp.push_back(u.first->val);
                ans.push_back(temp);
            }
            else ans[u.second-1].push_back(u.first->val);

            if(u.first->left) q.push({u.first->left, u.second+1});
            if(u.first->right) q.push({u.first->right, u.second+1});
        }
        return ans; 
    }
};
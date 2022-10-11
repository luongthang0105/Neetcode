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
    int ans = 0;
    void deep(TreeNode* node, int depth)
    {
        if(!node) 
        {
            ans = max(ans, depth);
            return;
        }
        deep(node->right, depth+1);
        deep(node->left, depth+1);
    }
    int maxDepth(TreeNode* root) {
        deep(root, 0);
        return ans;      
    }
};
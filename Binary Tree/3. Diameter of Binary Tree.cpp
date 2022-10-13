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
    int dfs(TreeNode* node, int depth){
        if(!node) return depth-1;
        int maxLeft = dfs(node->left, depth+1);
        int maxRight= dfs(node->right,depth+1);
        //cout << node->val << " " << maxLeft << " "  << maxRight << endl;
        ans = max(ans, maxLeft + maxRight - 2*depth);
        return max(maxLeft, maxRight);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        dfs(root, 0);
        return ans;
    }
};
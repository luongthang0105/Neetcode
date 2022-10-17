# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l, r): 
            if l < node.val < r:
                ok = True
                if node.right:
                    ok &= dfs(node.right, node.val, r)
                if node.left:
                    ok &= dfs(node.left, l, node.val)
                return ok
            else: return False
        return dfs(root, float("-inf"), float("inf"))
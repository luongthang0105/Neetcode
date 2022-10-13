# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(node1, node2):
            if (not node1) and (not node2): return True
            if node1 and node2 and node1.val == node2.val:
                return same(node1.left, node2.left) and same(node1.right, node2.right)
            return False
        def dfs(node):
            if not node: return False
            if node.val == subRoot.val:
                if same(node, subRoot):
                    return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
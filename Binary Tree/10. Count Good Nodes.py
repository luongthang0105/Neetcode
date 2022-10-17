# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0

        def count(node, mx):
            if node.val >= mx:
                self.cnt += 1
            if node.right:
                count(node.right, max(mx, node.val))
            if node.left:
                count(node.left, max(mx, node.val))
        count(root, root.val)
        return self.cnt
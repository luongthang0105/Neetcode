# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ok = True
        def dep(node, d):
            if not node: return d-1
            left = dep(node.left, d+1)
            if not self.ok: return -1
            right = dep(node.right, d+1)
            if not self.ok: return -1
            if(abs(left - right) > 1): 
                self.ok = False
                return -1
            return max(left, right) 
        dep(root, 0)
        return self.ok
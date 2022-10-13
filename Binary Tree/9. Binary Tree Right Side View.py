# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        q = collections.deque([root])
        while q:
            L = len(q)
            for i in range(L):
                u = q.popleft()
                if i == L-1: ans.append(u.val)
                if u.left: q.append(u.left)
                if u.right: q.append(u.right)
        return ans
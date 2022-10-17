# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
we minus k by 1 after processing a node's left subtree 
Visually, on Example 2, if we keep visiting the left child of a node,
we will eventually get to the smallest node value
then we we go back to its parent we minus k by 1 since we've taken out the smallest available node

after all, all we need to do is trying to visit the left subtree of a node first then update k

recursive is easy to implement; however iterative approach might save more space.
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        cur = root
        while stack:
            if cur.left:
                cur = cur.left
                stack.append(cur)
            else:
                while stack != []:
                    cur = stack.pop(len(stack)-1)
                    k -= 1
                    if not k: return cur.val 
                    if cur.right: 
                        cur = cur.right
                        stack.append(cur)
                        break
        return 0
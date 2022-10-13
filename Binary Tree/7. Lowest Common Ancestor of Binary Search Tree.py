# notice that this is a Binary Search Tree
#-> find the first node that split p and q into 2 subtree <=> p.val < node.val < q.val (suppose that p.val < q.val)
#special case is that node.val == p.val -> node.val is the answer (this is the case that p is the LCA of p and q)

#I initially misread the problem and use standard LCA algo that should be used to solve this problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#below this code is my solution using LCA algo (without binary lifting)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, P, Q):
            if not node: return None
            if P <= node.val <= Q: return node
            if node.val > Q: return dfs(node.left, P, Q)
            if node.val < P: return dfs(node.right, P, Q)
        if(p.val > q.val): p, q = q, p
        return dfs(root, p.val, q.val)
        
"""
lca solution (without binary lifting)
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.par = defaultdict(list)
        def dfs(pre, node, d):
            if not node: return -1
            #print(pre, d, val)
            self.par[node.val] = [pre, d]
            dfs(node.val, node.right, d+1)
            dfs(node.val, node.left, d+1)
            
        dfs(root.val, root, 0)
        P, Q = p.val, q.val
        lp, lq = self.par[P][1], self.par[Q][1]
        
        if lp > lq: 
            lp, lq = lq, lp
            P, Q = Q, P
        while(lq > lp): 
            lq -= 1
            Q = self.par[Q][0]
        if Q == P: return TreeNode(Q)
        while(self.par[Q][0] != self.par[P][0]):
            Q = self.par[Q][0]
            P = self.par[P][0]

        return TreeNode(self.par[Q][0])
"""
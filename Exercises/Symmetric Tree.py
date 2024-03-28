# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        def isEqual(p,q):
            if p and q:
                return  p.val == q.val and isEqual(p.left,q.right) and isEqual(p.right,q.left)
            return not p and not q
        if root:
            return isEqual(root.left,root.right)
        return True
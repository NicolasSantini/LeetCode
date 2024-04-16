# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def explore(node, val):
            if not node: return 0
            if not node.left and not node.right:
                return val * 10 + node.val
            else:
                return explore(node.left, val * 10 + node.val) + explore(node.right, val * 10 + node.val)
        if not root.left and not root.right:
            return root.val
        return explore(root.left, root.val) + explore(root.right, root.val)


sol = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(sol.sumNumbers(root))

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        l = self.hasPathSum(root.left, targetSum - root.val)
        r = self.hasPathSum(root.right, targetSum - root.val)
        return l or r

sol = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(sol.hasPathSum(root, 3))

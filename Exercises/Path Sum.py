# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        var = False

        def explore(node, partial_sum):
            nonlocal var


            if node:
                partial_sum += node.val
                if node.left:
                    explore(node.left, partial_sum)
                elif node.right:
                    explore(node.right, partial_sum)

                elif partial_sum == targetSum:
                    var = True

        explore(root, 0) if root and targetSum != 0 else None
        return var

sol = Solution()
root = TreeNode(1,TreeNode(2),TreeNode(3))
print(sol.hasPathSum(root, 1))

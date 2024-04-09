# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#raw and O(n) solution
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def explore(node):
            if not node:
                return 0
            return 1 + explore(node.left) + explore(node.right)

        return explore(root)
#O(logn) to implement
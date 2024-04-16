# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def explore(root, level):
            if root is None:
                return
            if level == depth - 1:
                tmpr = root.right
                tmpl = root.left
                root.left = TreeNode(val, tmpl, None)
                root.right = TreeNode(val, None, tmpr)

            explore(root.left, level + 1)
            explore(root.right, level + 1)

        # caso particolare
        if depth == 1:
            root = TreeNode(val, root, None)
        explore(root, 1)
        return root

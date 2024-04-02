# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        lst = 1000 * [0]
        num = 1000 * [0]

        def explore(node, level):
            if not node:
                return
            lst[level] += node.val
            num[level] += 1
            explore(node.left, level + 1)
            explore(node.right, level + 1)

        explore(root, 0)
        final = []
        for i, val in enumerate(lst):  # Unpack the tuple correctly
            final[i] = val / num[i]

        return final

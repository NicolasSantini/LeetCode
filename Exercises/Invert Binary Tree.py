class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        p: TreeNode = root
        l: TreeNode = root.left
        r: TreeNode = root.right
        root.left = r
        root.right = l
        self.invertTree(self, l)
        self.invertTree(self, r)

        return root

#time o(n) space o(n)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # Scambia i sottoalberi sinistro e destro ricorsivamente
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

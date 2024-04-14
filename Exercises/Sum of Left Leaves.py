# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        val = [0]

        def explore(root):
            if root.left:
                if not root.left.left and not root.left.right:
                    val[0] += root.left.val
                explore(root.left)
            if root.right:
                explore(root.right)


        explore(root)
        return val[0]



sol = Solution()
#root = TreeNode(1, TreeNode(2), TreeNode(3))
# Creazione dei nodi dell'albero
node_15 = TreeNode(15)
node_7 = TreeNode(7)
node_20 = TreeNode(20, left=node_15, right=node_7)
node_9 = TreeNode(9)
node_3 = TreeNode(3, left=node_9, right=node_20)

# Restituire il nodo radice dell'albero
root = node_3
print(sol.sumOfLeftLeaves(root))

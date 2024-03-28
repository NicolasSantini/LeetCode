# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root, subRoot) -> bool:

        def isEqual(p, q):
            if p and q:
                return p.val == q.val and isEqual(p.left, q.left) and isEqual(p.right, q.right)
            return p is q

        def dfs(node):
            if not node:
                return False

            if node.val == subRoot.val and isEqual(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)
        # if node and subRoot:
        #     return IsEqual(node,subRoot)
        # else:
        #     return node is subRoot
        #


root = TreeNode(3, TreeNode(4, 1, 2), 5)
subRoot = TreeNode(4, 1, 2)
# Creazione di un'istanza della classe Solution
solution = Solution()

# Chiamata del metodo isSubtree sull'istanza creata
result = solution.isSubtree(root, subRoot)

# Stampa del risultato
print(result)

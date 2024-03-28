# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#O(n) space and time
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height_and_balance(node: TreeNode) -> Tuple[int, bool]:
            if not node:
                return 0, True

            left_height, left_balanced = height_and_balance(node.left)
            right_height, right_balanced = height_and_balance(node.right)

            # Calcola l'altezza del sottoalbero e controlla il bilanciamento
            subtree_height = max(left_height, right_height) + 1
            subtree_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            return subtree_height, subtree_balanced

        _, balanced = height_and_balance(root)
        return balanced

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(log n) per entrambi
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # se il nodo corrente è nullo mi fermo
        if not root:
            return
        #se entrambi i valori sono minori esploro a sinistra e continuo
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # se entrambi i valori sono maggiori esploro a destra e continuo
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        #se sono uno maggiore e uno minore allora ho trovato il nodo padre più basso
        else:
            return root

#provo la versione senza occupare spazio, O(1) spaziale O(log n) temporale
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            if curr.val > p.val and curr.val > q.val:
                curr  = curr.left
                continue
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
                continue
            else:
                return curr
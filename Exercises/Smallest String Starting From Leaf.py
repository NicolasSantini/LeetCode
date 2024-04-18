# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


# worst sol ever but works
# class Solution:
#     def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
#         if root is None:
#             return ''
#         results = []
#         s = ''
#
#         def convert(s):
#             ret = ''
#             for c in s:
#                 ret += chr(int(c) + 97)
#             return ret
#
#         def explore(node: Optional[TreeNode], s):
#             if not node.left and not node.right:
#                 val = s.split(sep=" ")
#                 results.append(val[::-1])
#                 return
#             if node.left:
#                 explore(node.left, s + ' ' + str(node.left.val))
#             if node.right:
#                 explore(node.right, s + ' ' + str(node.right.val))
#
#         explore(root, s + str(root.val))
#         final = results[0]
#         for res in results[1:]:
#
#             for i, c in enumerate(res):
#                 if i == len(final):
#                     break
#                 if int(c) < int(final[i]):
#                     final = res
#                     break
#                 if int(c) > int(final[i]):
#                     break
#                 if len(res) < len(final) and i == len(res) - 1:
#                     final = res
#                     break
#
#
#         return convert(final)


# online sol
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Helper function to perform DFS
        def dfs(node, path, smallest):
            if not node:
                return

            # Append current node's character to the path
            path.append(chr(node.val + ord('a')))

            # If it's a leaf node, reverse the path and compare
            if not node.left and not node.right:
                current_string = ''.join(path[::-1])  # reverse path to get string
                smallest[0] = min(smallest[0], current_string)

            # Recursively traverse left and right subtrees
            dfs(node.left, path, smallest)
            dfs(node.right, path, smallest)

            # Backtrack: remove the current node's character from the path
            path.pop()

        # Initialize smallest string as a large value
        smallest = [chr(ord('z') + 1)]  # Store smallest string found

        # Start DFS from the root with an empty path
        dfs(root, [], smallest)

        return smallest[0]


def build_tree_from_list(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while queue and i < len(lst):
        node = queue.pop(0)

        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)

        i += 1

        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)

        i += 1

    return root


# Sample input
root_input = [2, 0, 1, None, None, 0]
# root_input = [4, 0, 1, 1]
# root_input = [2,1,2,None,0,1,None,None,None,0]

# Build the tree
root_node = build_tree_from_list(root_input)
sol = Solution()
print(sol.smallestFromLeaf(root_node))

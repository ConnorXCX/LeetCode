from typing import Optional
from binary_tree import TreeNode, getLevelOrder


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Time Complexity:  TBD
# Space Complexity: TBD
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Depth-first Search implementation; order does not matter.

        if not root:
            return None

        # Swap the children nodes.
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# # Function to get level order traversal of tree.
# def getLevelOrder(root: Optional[TreeNode]) -> list[int]:
#     if root and root.val == 0 and root.left is None and root.right is None:
#         return []

#     while not root:
#         return []

#     queue = [root]
#     result = []

#     while queue:
#         level_nodes = []
#         temp = []
#         for node in queue:
#             level_nodes.append(node.val)
#             if node.left:
#                 temp.append(node.left)
#             if node.right:
#                 temp.append(node.right)
#         queue = temp
#         result.append(level_nodes)

#     return [item for items in result for item in items]


# # Compute the height of a tree - the number of nodes along the longest path from the root node down to the farthest leaf node.
# def getHeight(node: Optional[TreeNode]) -> int:
#     if node is None:
#         return 0
#     else:
#         # Compute the height of each subtree.
#         leftHeight = height(node.left)
#         rightHeight = height(node.right)

#         # Use the larger one.
#         if leftHeight > rightHeight:
#             return leftHeight + 1
#         else:
#             return rightHeight + 1


if __name__ == '__main__':
    import unittest

    f = Solution().invertTree

    class Test(unittest.TestCase):

        def test_example_1(self):
            # [4, 2, 7, 1, 3, 6, 9]
            self.assertEqual(getLevelOrder(f(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(
                3)), TreeNode(7, TreeNode(6), TreeNode(9))))), [
                4, 7, 2, 9, 6, 3, 1])

        def test_example_2(self):
            # [2, 1, 3]
            self.assertEqual(getLevelOrder(
                f(TreeNode(2, TreeNode(1), TreeNode(3)))), [2, 3, 1])

        def test_example_3(self):
            # []
            self.assertEqual(getLevelOrder(f(TreeNode())), [])

    unittest.main()

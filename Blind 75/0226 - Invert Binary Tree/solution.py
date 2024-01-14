from typing import Optional
from Helpers.binary_tree import TreeNode


# Time Complexity:  TBD
# Space Complexity: TBD
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Depth-first Search implementation; preorder or postorder does not matter.

        if not root:
            return None

        # Swap the children nodes.
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == '__main__':
    import unittest

    f = Solution().invertTree

    class Test(unittest.TestCase):

        # TODO: Need way to create tree given list and traverse tree and output to list.
        def test_example_1(self):
            # [4, 2, 7, 1, 3, 6, 9]
            tree = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(
                6, TreeNode(3), TreeNode(1))), TreeNode(2))

            self.assertEqual(f(tree), [
                4, 7, 2, 9, 6, 3, 1])

        # def test_example_2(self):
            # self.assertEqual(f([2, 1, 3]), [2, 3, 1])

        # def test_example_3(self):
        #     self.assertEqual(f([]), [])

    unittest.main()
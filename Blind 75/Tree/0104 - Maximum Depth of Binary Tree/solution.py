from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().maxDepth

    # Function to get level order traversal of tree.
    def getLevelOrder(root: Optional[TreeNode]) -> list[int]:
        if root and root.val == 0 and root.left is None and root.right is None:
            return []

        while not root:
            return []

        queue = [root]
        result = []

        while queue:
            level_nodes = []
            temp = []
            for node in queue:
                level_nodes.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            result.append(level_nodes)

        return [item for items in result for item in items]

    class Test(unittest.TestCase):

        def test_example_1(self):
            # [3,9,20,null,null,15,7]
            self.assertEqual(f(), 3)

        def test_example_2(self):
            # [1,null,2]
            self.assertEqual(f(), 2)

    unittest.main()

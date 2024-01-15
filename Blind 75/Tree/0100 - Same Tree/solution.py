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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().isSameTree

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
            # p = [1,2,3], q = [1,2,3]
            self.assertEqual(f(), True)

        def test_example_2(self):
            # p = [1,2], q = [1,null,2]
            self.assertEqual(f(), False)

        def test_example_3(self):
            # p = [1,2,1], q = [1,1,2]
            self.assertEqual(f(), False)

    unittest.main()

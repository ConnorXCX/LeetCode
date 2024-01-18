from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return [[]]


if __name__ == '__main__':
    import unittest

    f = Solution().levelOrder

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f(), None)

        def test_example_2(self):
            self.assertEqual(f(), None)

        def test_example_3(self):
            self.assertEqual(f(), None)

    unittest.main()

from typing import Optional
from binary_tree import TreeNode, getLevelOrder


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().maxDepth

    class Test(unittest.TestCase):

        def test_example_1(self):
            # [3,9,20,null,null,15,7]
            self.assertEqual(f(), 3)

        def test_example_2(self):
            # [1,null,2]
            self.assertEqual(f(), 2)

    unittest.main()

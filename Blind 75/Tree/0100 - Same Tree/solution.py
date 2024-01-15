from typing import Optional
from binary_tree import TreeNode, getLevelOrder


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().isSameTree

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

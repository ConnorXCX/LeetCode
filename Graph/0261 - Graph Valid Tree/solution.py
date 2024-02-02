from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().validTree

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f(5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True)

        def test_example_2(self):
            self.assertEqual(
                f(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False)

    unittest.main()

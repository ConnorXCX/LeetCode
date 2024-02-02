from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().countComponents

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f(5, [[0, 1], [1, 2], [3, 4]]), 2)

        def test_example_2(self):
            self.assertEqual(f(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1)

    unittest.main()

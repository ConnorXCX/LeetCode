from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def numIslands(self, grid: List[List[str]]) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().numIslands

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ]), 1)

        def test_example_2(self):
            self.assertEqual(f([
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ]), 3)

    unittest.main()

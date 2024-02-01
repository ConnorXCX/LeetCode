class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def uniquePaths(self, m: int, n: int) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().uniquePaths

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f(3, 7), 28)

        def test_example_2(self):
            # Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
            # 1. Right -> Down -> Down
            # 2. Down -> Down -> Right
            # 3. Down -> Right -> Down
            self.assertEqual(f(3, 2), 3)

    unittest.main()

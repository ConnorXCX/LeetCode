class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def maxProduct(self, nums: list[int]) -> int:
        return 0


if __name__ == '__main__':
    import unittest

    f = Solution().maxProduct

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([2, 3, -2, 4]), 6)

        def test_example_2(self):
            self.assertEqual(f([-2, 0, -1]), 0)

    unittest.main()

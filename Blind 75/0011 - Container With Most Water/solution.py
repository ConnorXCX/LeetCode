class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def maxArea(self, height: list[int]) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().maxArea

    class Test(unittest.TestCase):

        def test_example_1(self):
            # The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
            self.assertEqual(f([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

        def test_example_2(self):
            self.assertEqual(f([1, 1]), 1)

    unittest.main()

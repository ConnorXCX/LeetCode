class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().threeSum

    class Test(unittest.TestCase):

        def test_example_1(self):
            # nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
            # nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
            # nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
            # The distinct triplets are [-1,0,1] and [-1,-1,2].
            # Notice that the order of the output and the order of the triplets does not matter.
            self.assertEqual(f([-1, 0, 1, 2, -1, -4]),
                             [[-1, -1, 2], [-1, 0, 1]])

        def test_example_2(self):
            # The only possible triplet does not sum up to 0.
            self.assertEqual(f([0, 1, 1]), [])

        def test_example_3(self):
            # The only possible triplet sums up to 0.
            self.assertEqual(f([0, 0, 0]), [[0, 0, 0]])

    unittest.main()

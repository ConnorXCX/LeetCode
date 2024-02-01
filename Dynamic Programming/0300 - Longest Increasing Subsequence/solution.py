from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().lengthOfLIS

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
            self.assertEqual(f([10, 9, 2, 5, 3, 7, 101, 18]), 4)

        def test_example_2(self):
            self.assertEqual(f([0, 1, 0, 3, 2, 3]), 4)

        def test_example_3(self):
            self.assertEqual(f([7, 7, 7, 7, 7, 7, 7]), 1)

    unittest.main()

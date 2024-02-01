from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def longestConsecutive(self, nums: List[int]) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().longestConsecutive

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
            self.assertEqual(f([100, 4, 200, 1, 3, 2]), 4)

        def test_example_2(self):
            self.assertEqual(f([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)

    unittest.main()

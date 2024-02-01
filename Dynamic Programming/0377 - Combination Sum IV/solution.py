from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def combinationSum4(self, nums: List[int], target: int) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().combinationSum4

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation:
            # The possible combination ways are:
            # (1, 1, 1, 1)
            # (1, 1, 2)
            # (1, 2, 1)
            # (1, 3)
            # (2, 1, 1)
            # (2, 2)
            # (3, 1)
            # Note that different sequences are counted as different combinations.
            self.assertEqual(f([1, 2, 3], 4), 7)

        def test_example_2(self):
            self.assertEqual(f([9], 3), 0)

    unittest.main()

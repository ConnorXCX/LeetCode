from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().coinChange

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([1, 2, 5], 11), 3)

        def test_example_2(self):
            self.assertEqual(f([2], 3), -1)

        def test_example_3(self):
            self.assertEqual(f([1], 0), 0)

    unittest.main()

from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def rob(self, nums: List[int]) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().rob

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
            # Total amount you can rob = 1 + 3 = 4.
            self.assertEqual(f([1, 2, 3, 1]), 4)

        def test_example_2(self):
            # Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
            # Total amount you can rob = 2 + 9 + 1 = 12.
            self.assertEqual(f([2, 7, 9, 3, 1]), 12)

    unittest.main()

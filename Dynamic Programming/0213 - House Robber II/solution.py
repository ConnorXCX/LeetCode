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
            # Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
            self.assertEqual(f([2, 3, 2]), 3)

        def test_example_2(self):
            # Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
            # Total amount you can rob = 1 + 3 = 4.
            self.assertEqual(f([1, 2, 3, 1]), 4)

        def test_example_3(self):
            self.assertEqual(f([1, 2, 3]), 3)

    unittest.main()

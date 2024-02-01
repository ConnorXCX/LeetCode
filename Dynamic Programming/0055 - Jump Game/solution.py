from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def canJump(self, nums: List[int]) -> bool:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().canJump

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
            self.assertEqual(f([2, 3, 1, 1, 4]), True)

        def test_example_2(self):
            # Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
            self.assertEqual(f([3, 2, 1, 0, 4]), False)

    unittest.main()

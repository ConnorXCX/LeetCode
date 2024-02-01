class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def climbStairs(self, n: int) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().climbStairs

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: There are two ways to climb to the top.
            # 1. 1 step + 1 step
            # 2. 2 steps
            self.assertEqual(f(2), 2)

        def test_example_2(self):
            # Explanation: There are three ways to climb to the top.
            # 1. 1 step + 1 step + 1 step
            # 2. 1 step + 2 steps
            # 3. 2 steps + 1 step
            self.assertEqual(f(3), 3)

    unittest.main()

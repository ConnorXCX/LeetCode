class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def getSum(self, a: int, b: int) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().getSum

    class Test(unittest.TestCase):

        def example_1(self):
            self.assertEqual(f(1, 2), 3)

        def example_2(self):
            self.assertEqual(f(2, 3), 5)

    unittest.main()

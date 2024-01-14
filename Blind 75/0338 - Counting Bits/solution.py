class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def countBits(self, n: int) -> list[int]:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().countBits

    class Test(unittest.TestCase):

        def example_1(self):
            # 0 --> 0
            # 1 --> 1
            # 2 --> 10
            self.assertEqual(f(2), [0, 1, 1])

        def example_2(self):
            # 0 --> 0
            # 1 --> 1
            # 2 --> 10
            # 3 --> 11
            # 4 --> 100
            # 5 --> 101
            self.assertEqual(f(5), [0, 1, 1, 2, 1, 2])

    unittest.main()

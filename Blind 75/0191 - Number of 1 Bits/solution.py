class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def hammingWeight(self, n: int) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().hammingWeight

    class Test(unittest.TestCase):

        def test_example_1(self):
            # The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
            self.assertEqual(f(00000000000000000000000000001011), 3)

        def test_example_2(self):
            # The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
            self.assertEqual(f(00000000000000000000000010000000), 1)

        def test_example_3(self):
            # The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
            self.assertEqual(f(11111111111111111111111111111101), 31)

    unittest.main()

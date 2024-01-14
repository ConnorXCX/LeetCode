class Solution:
    # Time Complexity:  O(1) - input is always a binary string of length 32, translating to a 32 Bit Integer; therefore, iterating through loop constant number of times, not scaling up.
    # Space Complexity: O(1) - input is always a binary string of length 32, translating to a 32 Bit Integer; therefore, iterating through loop constant number of times, not scaling up.
    def hammingWeight(self, n: int) -> int:
        # hammingWeight = 0

        # while n:
        #     hammingWeight += n % 2
        #     # Bitwise right shift by 1.
        #     n = n >> 1

        # return hammingWeight

        # Slightly optimized solution that skips 0's. Reference video linked in README for more detail.
        hammingWeight = 0

        while n:
            n &= (n - 1)
            hammingWeight += 1

        return hammingWeight


if __name__ == '__main__':
    import unittest

    f = Solution().hammingWeight

    class Test(unittest.TestCase):

        def test_example_1(self):
            # The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
            self.assertEqual(f(int('00000000000000000000000000001011', 2)), 3)

        def test_example_2(self):
            # The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
            self.assertEqual(f(int('00000000000000000000000010000000', 2)), 1)

        def test_example_3(self):
            # The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
            self.assertEqual(f(int('11111111111111111111111111111101', 2)), 31)

    unittest.main()

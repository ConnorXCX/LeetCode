class Solution:
    # Time Complexity:  O(1) - input is always a binary string of length 32, translating to a 32 Bit Integer; therefore, iterating through loop constant number of times, not scaling up.
    # Space Complexity: O(1) - input is always a binary string of length 32, translating to a 32 Bit Integer; therefore, iterating through loop constant number of times, not scaling up.
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31 - i))

        return result


if __name__ == '__main__':
    import unittest

    f = Solution().reverseBits

    class Test(unittest.TestCase):

        def test_example_1(self):
            # The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
            self.assertEqual(
                f(int('00000010100101000001111010011100', 2)), 964176192)

        def test_example_2(self):
            # The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
            self.assertEqual(
                f(int('11111111111111111111111111111101', 2)), 3221225471)

    unittest.main()

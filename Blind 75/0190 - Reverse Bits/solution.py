class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def reverseBits(self, n: int) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().reverseBits

    class Test(unittest.TestCase):

        def test_example_1(self):
            # The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
            self.assertEqual(f(00000010100101000001111010011100), 964176192 (00111001011110000010100101000000))

        def test_example_2(self):
            # The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
            self.assertEqual(f(11111111111111111111111111111101), 3221225471 (10111111111111111111111111111111))

    unittest.main()

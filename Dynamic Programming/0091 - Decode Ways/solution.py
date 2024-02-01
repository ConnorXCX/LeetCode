class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def numDecodings(self, s: str) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().numDecodings

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: '12' could be decoded as 'AB' (1 2) or 'L' (12).
            self.assertEqual(f('12'), 2)

        def test_example_2(self):
            # Explanation: '226' could be decoded as 'BZ' (2 26), 'VF' (22 6), or 'BBF' (2 2 6).
            self.assertEqual(f('226'), 3)

        def test_example_3(self):
            # Explanation: '06' cannot be mapped to 'F' because of the leading zero ('6' is different from '06').
            self.assertEqual(f('06'), 0)

    unittest.main()

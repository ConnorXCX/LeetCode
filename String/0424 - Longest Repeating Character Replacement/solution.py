class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def longestPalindrome(self, s: str) -> str:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().longestPalindrome

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: 'aba' is also a valid answer.
            self.assertEqual(f('babad'), 'bab')

        def test_example_2(self):
            self.assertEqual(f('cbbd'), 'bb')

    unittest.main()

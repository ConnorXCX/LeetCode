class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().longestCommonSubsequence

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: The longest common subsequence is 'ace' and its length is 3.
            self.assertEqual(f('abcde', 'ace'), 3)

        def test_example_2(self):
            # Explanation: The longest common subsequence is 'abc' and its length is 3.
            self.assertEqual(f('abc', 'abc'), 3)

        def test_example_3(self):
            # Explanation: There is no such common subsequence, so the result is 0.
            self.assertEqual(f('abc', 'def'), 0)

    unittest.main()

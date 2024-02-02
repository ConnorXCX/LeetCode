class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().lengthOfLongestSubstring

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: The answer is 'abc', with the length of 3.
            self.assertEqual(f('abcabcbb'), 3)

        def test_example_2(self):
            # Explanation: The answer is 'b', with the length of 1.
            self.assertEqual(f('bbbbb'), 1)

        def test_example_3(self):
            # Explanation: The answer is 'wke', with the length of 3.
            # Notice that the answer must be a substring, 'pwke' is a subsequence and not a substring.
            self.assertEqual(f('pwwkew'), 3)

    unittest.main()

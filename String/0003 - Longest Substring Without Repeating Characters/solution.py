class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def characterReplacement(self, s: str, k: int) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().characterReplacement

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: Replace the two 'A's with two 'B's or vice versa.
            self.assertEqual(f('ABAB', 2), 4)

        def test_example_2(self):
            # Explanation: Replace the one 'A' in the middle with 'B' and form 'AABBBBA'.
            # The substring 'BBBB' has the longest repeating letters, which is 4.
            # There may exists other ways to achieve this answer too.
            self.assertEqual(f('AABABBA', 1), 4)

    unittest.main()

class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def minWindow(self, s: str, t: str) -> str:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().minWindow

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
            self.assertEqual(f("ADOBECODEBANC", "ABC"), "ABC")

        def test_example_2(self):
            # Explanation: The entire string s is the minimum window.
            self.assertEqual(f("a", "a"), "a")

        def test_example_3(self):
            # Explanation: Both 'a's from t must be included in the window.
            # Since the largest window of s only has one 'a', return empty string.
            self.assertEqual(f("a", "aa"), "")

    unittest.main()

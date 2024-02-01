class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def countSubstrings(self, s: str) -> int:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().countSubstrings

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: Three palindromic strings: 'a', 'b', 'c'.
            self.assertEqual(f('abc'), 3)

        def test_example_2(self):
            # Explanation: Six palindromic strings: 'a', 'a', 'a', 'aa', 'aa', 'aaa'.
            self.assertEqual(f('aaa'), 6)

    unittest.main()

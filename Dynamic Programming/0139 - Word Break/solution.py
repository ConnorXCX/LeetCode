from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().wordBreak

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: Return true because 'leetcode' can be segmented as 'leet code'.
            self.assertEqual(f('leetcode', ['leet', 'code']), True)

        def test_example_2(self):
            # Explanation: Return true because 'applepenapple' can be segmented as 'apple pen apple'.
            # Note that you are allowed to reuse a dictionary word.
            self.assertEqual(f('applepenapple', ['apple', 'pen']), True)

        def test_example_3(self):
            self.assertEqual(
                f('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']), False)

    unittest.main()

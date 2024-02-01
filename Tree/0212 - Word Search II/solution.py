from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie (Prefix Tree) Implementation to organize words based on their prefixes.
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().findWords

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], [
                             "i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"]), ["eat", "oath"])

        def test_example_2(self):
            self.assertEqual(f([["a", "b"], ["c", "d"]], ["abcb"]), [])

    unittest.main()

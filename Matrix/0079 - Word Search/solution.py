from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().exist

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
            # Output: true
            self.assertEqual(f(), None)

        def test_example_2(self):
            # Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
            # Output: true
            self.assertEqual(f(), None)

        def test_example_3(self):
            # Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
            # Output: false
            self.assertEqual(f(), None)

    unittest.main()

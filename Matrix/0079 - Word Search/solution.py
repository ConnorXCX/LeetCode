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
            self.assertEqual(f([["A", "B", "C", "E"], ["S", "F", "C", "S"], [
                             "A", "D", "E", "E"]], "ABCCED"), True)

        def test_example_2(self):
            self.assertEqual(f([["A", "B", "C", "E"], ["S", "F", "C", "S"], [
                             "A", "D", "E", "E"]], "SEE"), True)

        def test_example_3(self):
            self.assertEqual(f([["A", "B", "C", "E"], ["S", "F", "C", "S"], [
                             "A", "D", "E", "E"]], "ABCB"), False)

    unittest.main()

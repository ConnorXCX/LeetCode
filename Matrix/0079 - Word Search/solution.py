from typing import List


class Solution:
    # Time Complexity:  O(n * m * 3^L) - L being the length of the word with 3 branches in DFS return; 4 branches in code, but can not backtrack to previously visited cell to form word.
    # Space Complexity: TBD
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Recursive DFS Implementation.
        rows, columns = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= rows or c >= columns or word[i] != board[r][c] or (r, c) in path):
                return False

            path.add((r, c))

            result = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1)
                      or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))

            path.remove((r, c))

            return result

        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0):
                    return True

        return False


if __name__ == '__main__':
    import unittest

    f = Solution().exist

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], [
                             'A', 'D', 'E', 'E']], 'ABCCED'), True)

        def test_example_2(self):
            self.assertEqual(f([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], [
                             'A', 'D', 'E', 'E']], 'SEE'), True)

        def test_example_3(self):
            self.assertEqual(f([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], [
                             'A', 'D', 'E', 'E']], 'ABCB'), False)

    unittest.main()

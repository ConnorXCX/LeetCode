from re import L
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def insert(self, word: str) -> None:
        current = self

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        current.endOfWord = True


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie (Prefix Tree) Implementation to organize words based on their prefixes.

        root = TrieNode()

        for word in words:
            root.insert(word)

        rows, columns, result, visited = len(
            board), len(board[0]), set(), set()

        def dfs(row, column, node, word):
            if (row < 0 or column < 0 or row == rows or column == columns or (row, column) in visited or board[row][column] not in node.children):
                return

            visited.add((row, column))

            node = node.children[board[row][column]]
            word += board[row][column]

            if node.endOfWord:
                result.add(word)

            dfs(row - 1, column, node, word)
            dfs(row + 1, column, node, word)
            dfs(row, column - 1, node, word)
            dfs(row, column + 1, node, word)

            visited.remove((row, column))

        for row in range(rows):
            for column in range(columns):
                dfs(row, column, root, '')

        return list(result)


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

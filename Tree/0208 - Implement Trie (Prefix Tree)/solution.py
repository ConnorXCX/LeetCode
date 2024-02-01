class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    # Time Complexity:  TBD
    # Space Complexity: TBD
    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        current.endOfWord = True

    # Time Complexity:  TBD
    # Space Complexity: TBD
    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.endOfWord

    # Time Complexity:  TBD
    # Space Complexity: TBD

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True


if __name__ == '__main__':
    import unittest

    # Input
    # ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    # [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    # Output
    # [null, null, true, false, true, null, true]

    obj = Trie()
    obj.insert("apple")

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(obj.search("apple"), True)

        def test_example_2(self):
            self.assertEqual(obj.search("app"), False)

        def test_example_3(self):
            self.assertEqual(obj.startsWith("app"), True)

        def test_example_4(self):
            obj.insert("app")
            self.assertEqual(obj.search("app"), True)

    unittest.main()

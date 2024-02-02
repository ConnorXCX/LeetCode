from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        """

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """


if __name__ == '__main__':
    import unittest

    # f = Solution().solution

    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.decode(codec.encode(strs))

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Input: dummy_input = ["Hello","World"]
            # Output: ["Hello","World"]
            # Explanation:
            # Machine 1:
            # Codec encoder = new Codec();
            # String msg = encoder.encode(strs);
            # Machine 1 ---msg---> Machine 2

            # Machine 2:
            # Codec decoder = new Codec();
            # String[] strs = decoder.decode(msg);
            self.assertEqual(f(), None)

        def test_example_2(self):
            # Input: dummy_input = [""]
            # Output: [""]
            self.assertEqual(f(), None)

    unittest.main()

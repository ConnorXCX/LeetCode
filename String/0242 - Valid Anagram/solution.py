class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def isAnagram(self, s: str, t: str) -> bool:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().isAnagram

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f('anagram', t='nagaram'), True)

        def test_example_2(self):
            self.assertEqual(f('rat', t='car'), False)

    unittest.main()

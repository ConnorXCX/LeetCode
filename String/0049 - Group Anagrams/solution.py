from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().groupAnagrams

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']), [
                             ['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']])

        def test_example_2(self):
            self.assertEqual(f(['']), [['']])

        def test_example_3(self):
            self.assertEqual(f(['a']), [['a']])

    unittest.main()

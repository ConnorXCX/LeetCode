from typing import List


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def alienOrder(self, words: List[str]) -> str:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().alienOrder

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f(['wrt', 'wrf', 'er', 'ett', 'rftt']), 'wertf')

        def test_example_2(self):
            self.assertEqual(f(['z', 'x']), 'zx')

        def test_example_3(self):
            # Explanation: The order is invalid, so return ''.
            self.assertEqual(f(['z', 'x', 'z']), '')

    unittest.main()

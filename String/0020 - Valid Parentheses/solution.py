class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def isValid(self, s: str) -> bool:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().isValid

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f('()'), True)

        def test_example_2(self):
            self.assertEqual(f('()[]{}'), True)

        def test_example_3(self):
            self.assertEqual(f('(]'), False)

    unittest.main()

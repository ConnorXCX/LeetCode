class Solution:
    # Time Complexity:  O(1) - using constant time logical operators XOR and AND.
    # Space Complexity: O(1) - using constant time logical operators XOR and AND.
    def getSum(self, a: int, b: int) -> int:
        # Need for Python due to how Python represents size in Bits (much larger). Reference video linked in README for more detail.
        bitShortener = 0xffffffff

        while (b & bitShortener):
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        return (a & bitShortener) if b > 0 else a


if __name__ == '__main__':
    import unittest

    f = Solution().getSum

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f(1, 2), 3)

        def test_example_2(self):
            self.assertEqual(f(2, 3), 5)

        def test_example_3(self):
            self.assertEqual(f(9, 11), 20)

    unittest.main()

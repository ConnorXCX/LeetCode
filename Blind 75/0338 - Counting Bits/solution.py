class Solution:
    # Time Complexity:  O(n) - iterating n times.
    # Space Complexity: O(n) - iterating n times.
    def countBits(self, n: int) -> list[int]:
        # ans = [0] * (n + 1)
        # offset = 1

        # for i in range(1, n + 1):
        #     if offset * 2 == i:
        #         offset = i

        #     ans[i] = 1 + ans[i - offset]

        # return ans

        # Slightly optimized solution using Bitwise operators.
        ans = [0]

        for i in range(1, n + 1):
            ans.append(ans[i >> 1] + int(i & 1))

        return ans


if __name__ == '__main__':
    import unittest

    f = Solution().countBits

    class Test(unittest.TestCase):

        def test_example_1(self):
            # 0 --> 0
            # 1 --> 1
            # 2 --> 10
            self.assertEqual(f(2), [0, 1, 1])

        def test_example_2(self):
            # 0 --> 0
            # 1 --> 1
            # 2 --> 10
            # 3 --> 11
            # 4 --> 100
            # 5 --> 101
            self.assertEqual(f(5), [0, 1, 1, 2, 1, 2])

    unittest.main()

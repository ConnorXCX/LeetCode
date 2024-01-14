class Solution:
    # Time Complexity:  O(n) - scanning through given array once with two pointers.
    # Space Complexity: O(1) - no extra space used, using pointers to track instead of other data structures.
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1  # left pointer = buy, right pointer = sell
        maxProfit = 0

        while r < len(prices):
            # Check if profitable.
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1

        return maxProfit


if __name__ == '__main__':
    import unittest

    f = Solution().maxProfit

    class Test(unittest.TestCase):

        def example_1(self):
            # Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
            self.assertEqual(f([7, 1, 5, 3, 6, 4]), 5)

        def example_2(self):
            # In this case, no transactions are done and the max profit = 0.
            self.assertEqual(f([7, 6, 4, 3, 1]), 0)

    unittest.main()

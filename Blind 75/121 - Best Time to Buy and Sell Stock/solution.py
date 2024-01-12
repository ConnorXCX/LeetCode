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


solution = Solution()

# Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # 5

# In this case, no transactions are done and the max profit = 0.
print(solution.maxProfit([7, 6, 4, 3, 1]))  # 0

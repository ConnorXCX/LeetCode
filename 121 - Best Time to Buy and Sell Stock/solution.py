class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return 0


solution = Solution()

# Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # 5

# In this case, no transactions are done and the max profit = 0.
print(solution.maxProfit([7, 6, 4, 3, 1]))  # 0

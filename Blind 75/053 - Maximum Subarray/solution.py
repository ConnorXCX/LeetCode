class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def maxSubArray(self, nums: list[int]) -> int:
        return 0


solution = Solution()

# The subarray [4,-1,2,1] has the largest sum 6.
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6

# The subarray [1] has the largest sum 1.
print(solution.maxSubArray([1]))  # 1

# The subarray [5,4,-1,7,8] has the largest sum 23.
print(solution.maxSubArray([5, 4, -1, 7, 8]))  # 23

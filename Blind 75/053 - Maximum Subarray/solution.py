class Solution:
    # Time Complexity:  O(n) - iterate through array, removing any negative prefix while computing sum.
    # Space Complexity: O(1)
    def maxSubArray(self, nums: list[int]) -> int:
        currentSum = 0
        maxSubArraySum = nums[0]

        for num in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += num
            maxSubArraySum = max(maxSubArraySum, currentSum)

        return maxSubArraySum


solution = Solution()

# The subarray [4,-1,2,1] has the largest sum 6.
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6

# The subarray [1] has the largest sum 1.
print(solution.maxSubArray([1]))  # 1

# The subarray [5,4,-1,7,8] has the largest sum 23.
print(solution.maxSubArray([5, 4, -1, 7, 8]))  # 23

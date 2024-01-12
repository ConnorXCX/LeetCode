class Solution:
    # Time Complexity:  O(n) - using output array to track prefix and postfix array computations.
    # Space Complexity: O(1)
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix, postfix = 1, 1
        answer = [1] * (len(nums))

        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer


solution = Solution()

print(solution.productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]

print(solution.productExceptSelf([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]

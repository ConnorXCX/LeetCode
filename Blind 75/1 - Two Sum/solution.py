class Solution:
    # Time Complexity:  O(n) - iterating through array once and adding to hash map on each iteration (constant time operation).
    # Space Complexity: O(n) - could potentially add every value to hash map.
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        return []


solution = Solution()

# Because nums[0] + nums[1] == 9, we return [0, 1].
print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]

print(solution.twoSum([3, 2, 4], 6))  # [1, 2]

print(solution.twoSum([3, 3], 6))  # [0, 1]

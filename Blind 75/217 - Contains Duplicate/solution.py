class Solution:
    # Time Complexity:  O(nlogn) - one pass to sort and then duplicates are adjacent.
    # Space Complexity: O(1) - no extra space if not counting space of sorting algorithm.
    # Tradeoff of space complexity for time complexity using HashSet:
    # Time Complexity:  O(n) - using HashSet, have to iterate through given array once.
    # Space Complexity: O(n) - HashSet may need maximally the size of the given array.
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)

        return False


solution = Solution()

print(solution.containsDuplicate([1, 2, 3, 1]))  # true

print(solution.containsDuplicate([1, 2, 3, 4]))  # false

print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # true

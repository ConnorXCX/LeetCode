class Solution:
    # Time Complexity:  O(n) - iterating through given array once and then iterating backwards for Bucket Sort array.
    # Space Complexity: O(n) - HashMap to count occurrences of each value of given array.
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Bucket Sort implementation.
        countMap = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)

        for number, count in countMap.items():
            frequency[count].append(number)

        result = []

        for i in range(len(frequency) - 1, 0, -1):
            for number in frequency[i]:
                result.append(number)

        return result[:k]


if __name__ == '__main__':
    import unittest

    f = Solution().topKFrequent

    class Test(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(f([1, 1, 1, 2, 2, 3], 2), [1, 2])

        def test_example_2(self):
            self.assertEqual(f([1], 1), [1])

    unittest.main()

class Solution:
    # Time Complexity:  O(n)
    # Space Complexity: TBD
    def minWindow(self, s: str, t: str) -> str:
        countT, window, = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        have, need, result, resultLength, leftPointer = 0, len(
            countT), [-1, -1], float('infinity'), 0

        for rightPointer in range(len(s)):
            char = s[rightPointer]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                # Update result.
                if (rightPointer - leftPointer + 1) < resultLength:
                    result = [leftPointer, rightPointer]
                    resultLength = (rightPointer - leftPointer + 1)

                # Pop from left of window.
                window[s[leftPointer]] -= 1

                if s[leftPointer] in countT and window[s[leftPointer]] < countT[s[leftPointer]]:
                    have -= 1

                leftPointer += 1

        l, r = result

        return s[l: r + 1] if resultLength != float('infinity') else ''


if __name__ == '__main__':
    import unittest

    f = Solution().minWindow

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: The minimum window substring 'BANC' includes 'A', 'B', and 'C' from string t.
            self.assertEqual(f('ADOBECODEBANC', 'ABC'), 'BANC')

        def test_example_2(self):
            # Explanation: The entire string s is the minimum window.
            self.assertEqual(f('a', 'a'), 'a')

        def test_example_3(self):
            # Explanation: Both 'a's from t must be included in the window.
            # Since the largest window of s only has one 'a', return empty string.
            self.assertEqual(f('a', 'aa'), '')

    unittest.main()

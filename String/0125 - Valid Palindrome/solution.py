class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def isPalindrome(self, s: str) -> bool:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().isPalindrome

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Explanation: "amanaplanacanalpanama" is a palindrome.
            self.assertEqual(f("A man, a plan, a canal: Panama"), True)

        def test_example_2(self):
            # Explanation: "raceacar" is not a palindrome.
            self.assertEqual(f("race a car"), False)

        def test_example_3(self):
            # Explanation: s is an empty string "" after removing non-alphanumeric characters.
            # Since an empty string reads the same forward and backward, it is a palindrome.
            self.assertEqual(f(" "), True)

    unittest.main()

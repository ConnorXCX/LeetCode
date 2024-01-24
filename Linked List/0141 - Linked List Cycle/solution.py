from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity:  TBD
    # Space Complexity: TBD
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass


if __name__ == '__main__':
    import unittest

    f = Solution().hasCycle

    class Test(unittest.TestCase):

        def test_example_1(self):
            # Input: head = [3,2,0,-4], pos = 1
            # Output: true
            # Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
            self.assertEqual(f(), None)

        def test_example_2(self):
            # Input: head = [1,2], pos = 0
            # Output: true
            # Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
            self.assertEqual(f(), None)

        def test_example_3(self):
            # Input: head = [1], pos = -1
            # Output: false
            # Explanation: There is no cycle in the linked list.
            self.assertEqual(f(), None)

    unittest.main()

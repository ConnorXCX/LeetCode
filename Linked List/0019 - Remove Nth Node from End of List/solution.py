from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity:  O(n) - two pointers technique.
    # Space Complexity: O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Empty node at the beginning of the Linked List for reference later.
        stubNode = ListNode(0, head)
        left, right = stubNode, head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next  # type: ignore
            right = right.next

        left.next = left.next.next  # type: ignore

        return stubNode.next


if __name__ == '__main__':
    import unittest

    f = Solution().removeNthFromEnd

    class Test(unittest.TestCase):

        def getSolutionAsList(self, list: Optional[ListNode], n: int) -> List:
            solutionList = []
            solutionListNodes = f(list, n)

            while solutionListNodes:
                solutionList.append(solutionListNodes.val)
                solutionListNodes = solutionListNodes.next

            return solutionList

        def test_example_1(self):
            # Input: head = [1,2,3,4,5], n = 2
            # Output: [1,2,3,5]
            self.assertEqual(self.getSolutionAsList(ListNode(1, ListNode(
                2, ListNode(3, ListNode(4, ListNode(5))))), 2), [1, 2, 3, 5])

        def test_example_2(self):
            # Input: head = [1], n = 1
            # Output: []
            self.assertEqual(self.getSolutionAsList(ListNode(1), 1), [])

        def test_example_3(self):
            # Input: head = [1,2], n = 1
            # Output: [1]
            self.assertEqual(self.getSolutionAsList(
                ListNode(1, ListNode(2)), 1), [1])

    unittest.main()

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity:  O(n) - traversing the Linked List.
    # Space Complexity: O(1)
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Find middle.
        slow, fast = head, head.next  # type: ignore

        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next

        # Reverse second half.
        second = slow.next  # type: ignore
        previous = slow.next = None  # type: ignore

        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp

        # Merge two halves.
        first, second = head, previous

        while second:
            temp1, temp2 = first.next, second.next  # type: ignore
            first.next = second  # type: ignore
            second.next = temp1
            first, second = temp1, temp2

        return head


if __name__ == '__main__':
    import unittest

    f = Solution().reorderList

    class Test(unittest.TestCase):

        def getSolutionAsList(self, list: Optional[ListNode]) -> List:
            solutionList = []
            solutionListNodes = f(list)

            while solutionListNodes:
                solutionList.append(solutionListNodes.val)
                solutionListNodes = solutionListNodes.next

            return solutionList

        def test_example_1(self):
            # Input: head = [1,2,3,4]
            # Output: [1,4,2,3]
            self.assertEqual(
                self.getSolutionAsList(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))), [1, 4, 2, 3])

        def test_example_2(self):
            # Input: head = [1,2,3,4,5]
            # Output: [1,5,2,4,3]
            self.assertEqual(
                self.getSolutionAsList(ListNode(1, ListNode(
                    2, ListNode(3, ListNode(4, ListNode(5)))))), [1, 5, 2, 4, 3])

    unittest.main()

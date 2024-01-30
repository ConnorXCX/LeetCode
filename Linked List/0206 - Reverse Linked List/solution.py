from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Implementation
        # Use two pointers to track current node and previous node.
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        # previous, current = None, head

        # while current:
        #     next = current.next
        #     current.next = previous
        #     previous = current
        #     current = next

        # return previous

        # Recursive Implementation
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        # if not head:
        #     return None

        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head

        # head.next = None

        # return newHead


if __name__ == '__main__':
    import unittest

    f = Solution().reverseList

    class Test(unittest.TestCase):

        def getSolutionAsList(self, list: Optional[ListNode]) -> List:
            solutionList = []
            solutionListNodes = f(list)

            while solutionListNodes:
                solutionList.append(solutionListNodes.val)
                solutionListNodes = solutionListNodes.next

            return solutionList

        def test_example_1(self):
            # Input: head = [1,2,3,4,5]
            # Output: [5,4,3,2,1]
            self.assertEqual(self.getSolutionAsList(ListNode(1, ListNode(
                2, ListNode(3, ListNode(4, ListNode(5)))))), [5, 4, 3, 2, 1])

        def test_example_2(self):
            # Input: head = [1,2]
            # Output: [2,1]
            self.assertEqual(self.getSolutionAsList(ListNode(1, ListNode(
                2))), [2, 1])

        def test_example_3(self):
            # Input: head = []
            # Output: []
            self.assertEqual(self.getSolutionAsList(None), [])

    unittest.main()

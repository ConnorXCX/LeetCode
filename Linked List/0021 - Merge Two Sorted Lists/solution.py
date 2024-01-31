from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity: O(n + m) - n = number of nodes in list1 and  m = number of nodes in list2.
    # Space Complexity: O(1) - just shifting the pointers.
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        initialNode = ListNode()
        currentNode = initialNode

        while list1 and list2:
            if list1.val < list2.val:
                currentNode.next = list1
                list1 = list1.next
            else:
                currentNode.next = list2
                list2 = list2.next

            currentNode = currentNode.next

        if list1:
            currentNode.next = list1
        elif list2:
            currentNode.next = list2

        return initialNode.next


if __name__ == '__main__':
    import unittest

    f = Solution().mergeTwoLists

    class Test(unittest.TestCase):

        def getSolutionAsList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> List:
            solutionList = []
            solutionListNodes = f(list1, list2)

            while solutionListNodes:
                solutionList.append(solutionListNodes.val)
                solutionListNodes = solutionListNodes.next

            return solutionList

        def test_example_1(self):
            # Input: list1 = [1,2,4], list2 = [1,3,4]
            # Output: [1,1,2,3,4,4]
            self.assertEqual(self.getSolutionAsList(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(
                4)))), [1, 1, 2, 3, 4, 4])

        def test_example_2(self):
            # Input: list1 = [], list2 = []
            # Output: []
            self.assertEqual(self.getSolutionAsList(None, None), [])

        def test_example_3(self):
            # Input: list1 = [], list2 = [0]
            # Output: [0]
            self.assertEqual(self.getSolutionAsList(None, ListNode(0)), [0])

    unittest.main()

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity:  O(n) - traversing through entire tree.
    # Space Complexity: O(h) - height of tree; worst case O(n) if not a balanced Binary Tree.
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Solution 1: Recursive DFS
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # Solution 2: Iterative Pre-order DFS
        # stack = [[root, 1]]
        # currentMaxDepth = 0

        # while stack:
        #     node, depth = stack.pop()

        #     if node:
        #         currentMaxDepth = max(currentMaxDepth, depth)
        #         # Add children of current node to stack, including their depth.
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])

        # return currentMaxDepth

        # Solution 3: Iterative BFS
        # if not root:
        #     return 0

        # levels = 0
        # q = deque([root])
        # while q:
        #     # Traverse level and replace parents with children, or replace current level with next level.
        #     for i in range(len(q)):
        #         node = q.popleft()

        #         if node.left:
        #             q.append(node.left)

        #         if node.right:
        #             q.append(node.right)

        #     levels += 1

        # return levels


if __name__ == '__main__':
    import unittest

    f = Solution().maxDepth

    # Function to get level order traversal of tree.
    def getLevelOrder(root: Optional[TreeNode]) -> list[int]:
        if root and root.val == 0 and root.left is None and root.right is None:
            return []

        while not root:
            return []

        queue = [root]
        result = []

        while queue:
            level_nodes = []
            temp = []
            for node in queue:
                level_nodes.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            result.append(level_nodes)

        return [item for items in result for item in items]

    class Test(unittest.TestCase):

        def test_example_1(self):
            # [3,9,20,null,null,15,7]
            self.assertEqual(
                f(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))), 3)

        def test_example_2(self):
            # [1,null,2]
            self.assertEqual(f(TreeNode(1, None, TreeNode(2))), 2)

    unittest.main()

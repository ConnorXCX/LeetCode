from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity:  O(n) - DFS implementation.
    # Space Complexity: O(h) - height of tree.
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = [root.val]

        # Return max path sum without split.
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Compute max path sum WITH split.
            result[0] = max(result[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)

        return result[0]


if __name__ == '__main__':
    import unittest

    f = Solution().maxPathSum

    # Function to get level order traversal of tree.
    def getLevelOrder(root: Optional[TreeNode]) -> List[int]:
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
            self.assertEqual(f(TreeNode(1, TreeNode(2), TreeNode(3))), 6)

        def test_example_2(self):
            self.assertEqual(
                f(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))), 42)

    unittest.main()

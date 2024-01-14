from typing import Optional

# Recursive Python program for level
# order traversal of Binary Tree
# Source: https://www.geeksforgeeks.org/level-order-tree-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


# Compute the height of a tree - the number of nodes along the longest path from the root node down to the farthest leaf node.
def height(node: Optional[TreeNode]) -> int:
    if node is None:
        return 0
    else:
        # Compute the height of each subtree.
        leftHeight = height(node.left)
        rightHeight = height(node.right)

        # Use the larger one.
        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(getLevelOrder(root))

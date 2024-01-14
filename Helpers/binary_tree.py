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
def getLevelOrder(root: Optional[TreeNode]):
    levels = []
    h = height(root)

    for i in range(1, h+1):
        levels.append(getCurrentLevel(root, i))

    return levels


# Get nodes at a current level
def getCurrentLevel(root: Optional[TreeNode], level: int):
    if root is None:
        return
    if level == 1:
        # levels.append(root.val)
        return root.val
    elif level > 1:
        leftLevel = getCurrentLevel(root.left, level - 1)
        if leftLevel is not None:
            # levels.append(leftLevel)
            return leftLevel
        rightLevel = getCurrentLevel(root.right, level - 1)
        if rightLevel is not None:
            # levels.append(rightLevel)
            return rightLevel


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

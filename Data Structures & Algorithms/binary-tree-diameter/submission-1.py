# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def getHeight(root):

            nonlocal diameter

            if not root:
                return 0

            leftHeight = getHeight(root.left)
            rightHeight = getHeight(root.right)

            diameter = max(diameter, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        getHeight(root)

        return diameter
        
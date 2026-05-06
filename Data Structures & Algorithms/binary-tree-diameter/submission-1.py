# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0, 0
            
            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)

            height = 1 + max(left_height, right_height)

            diameter = left_height + right_height

            best_diameter = max(
                diameter,
                left_diameter,
                right_diameter
            )

            return height, best_diameter
        
        height, diameter = dfs(root)
        return diameter


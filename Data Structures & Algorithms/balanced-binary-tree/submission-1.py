# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node):
            if not node:
                return True, 0
            
            left_balance, left_height = dfs(node.left)
            right_balance, right_height = dfs(node.right)
            balanced = False
            if abs(left_height - right_height) <= 1:
                balanced = True

            return (balanced and left_balance and right_balance), max(left_height, right_height) + 1
        
        balanced, height = dfs(root)

        return balanced

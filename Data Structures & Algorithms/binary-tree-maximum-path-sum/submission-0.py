# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, best):
            if not node:
                return 0, best
            
            left_gain, best = dfs(node.left, best)
            right_gain, best = dfs(node.right, best)

            left_gain = max(left_gain, 0)
            right_gain = max(right_gain, 0)

            current_path = node.val + left_gain + right_gain

            best = max(current_path, best)

            upward = node.val + max(left_gain, right_gain)

            return upward, best

        _, best = dfs(root, float("-inf"))

        return best

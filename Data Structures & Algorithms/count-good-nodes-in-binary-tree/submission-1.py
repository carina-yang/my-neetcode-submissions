# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        good = 0

        while stack:
            node, max_so_far = stack.pop()

            if node.val >= max_so_far:
                good += 1
            
            new_max = max(max_so_far, node.val)

            if node.left:
                stack.append((node.left, new_max))
            if node.right:
                stack.append((node.right, new_max))
        
        return good
            
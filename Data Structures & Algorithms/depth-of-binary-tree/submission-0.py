# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = { root: 1 }
        stack = []
        curr = root
        max_depth = 0

        while curr or stack:
            if curr:
                print(curr)
                stack.append(curr)
                if curr.left:
                    depth[curr.left] = depth.get(curr, 0) + 1
                curr = curr.left
            else:
                curr = stack.pop()
                max_depth = max(depth[curr], max_depth)
                if curr.right:
                    depth[curr.right] = depth.get(curr, 0) + 1
                curr = curr.right
        
        return max_depth
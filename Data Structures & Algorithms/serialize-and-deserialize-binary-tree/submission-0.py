# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        def dfs(node):
            if not node:
                return "N"
            
            return str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)
        
        return dfs(root)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")

        def dfs(i):
            if vals[i] == "N":
                i += 1
                return None, i
            
            node = TreeNode(int(vals[i]))
            i += 1

            left_node, i = dfs(i)
            right_node, i = dfs(i)

            node.left = left_node
            node.right = right_node

            return node, i
        
        root, _ = dfs(0)

        return root



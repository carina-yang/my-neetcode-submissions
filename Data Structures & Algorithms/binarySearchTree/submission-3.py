class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def _recInsert(self, node: TreeNode, key: int, val: int) -> TreeNode:
        if not node:
            return TreeNode(key, val)
        
        if key < node.key:
            node.left = self._recInsert(node.left, key, val)
        elif key > node.key:
            node.right = self._recInsert(node.right, key, val)
        else:
            node.val = val
        return node

    def insert(self, key: int, val: int) -> None:
        self.root = self._recInsert(self.root, key, val)

    def _recGet(self, node: TreeNode, key) -> int:
        if not node:
            return -1
        
        if key < node.key:
            return self._recGet(node.left, key)
        elif key > node.key:
            return self._recGet(node.right, key)
        else:
            return node.val

    def get(self, key: int) -> int: 
        return self._recGet(self.root, key)
    
    def _getMinNode(self, node: TreeNode) -> TreeNode:
        curr = node
        while curr and curr.left:
            curr = curr.left
        return curr

    def getMin(self) -> int:
        minNode = self._getMinNode(self.root)
        if minNode:
            return minNode.val
        return -1
    
    def _getMaxNode(self, node: TreeNode) -> TreeNode:
        curr = node
        while curr and curr.right:
            curr = curr.right
        return curr

    def getMax(self) -> int:
        maxNode = self._getMaxNode(self.root)
        if maxNode:
            return maxNode.val
        return -1
    
    def _recRemove(self, node: TreeNode, key: int) -> None:
        if not node:
            return None
        
        if key < node.key:
            node.left = self._recRemove(node.left, key)
        elif key > node.key:
            node.right = self._recRemove(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                minNode = self._getMinNode(node.right)
                node.key = minNode.key
                node.val = minNode.val
                node.right = self._recRemove(node.right, minNode.key)
        return node

    def remove(self, key: int) -> None:
        self.root = self._recRemove(self.root, key)
    
    def _recGetInorderKeys(self, node: TreeNode) -> List[int]:
        if not node:
            return []
        
        return self._recGetInorderKeys(node.left) + [node.key] + self._recGetInorderKeys(node.right)

    def getInorderKeys(self) -> List[int]:
        return self._recGetInorderKeys(self.root)



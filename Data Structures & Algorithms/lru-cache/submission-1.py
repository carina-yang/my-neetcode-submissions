class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Node] = {}
        
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insert_front(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def _move_to_front(self, node: Node) -> None:
        self._remove(node)
        self._insert_front(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._insert_front(node)

            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
        

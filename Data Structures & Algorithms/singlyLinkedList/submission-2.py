class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.nex = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if self.length == 0 or index >= self.length:
            return -1
        cur = self.head
        while index > 0:
            cur = cur.nex
            index -= 1
        return cur.val

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.nex = self.head
        self.head = node
        if self.length == 0:
            self.tail = node
        self.length += 1

    def insertTail(self, val: int) -> None:
        print("hi")
        node = ListNode(val)
        if self.tail:
            self.tail.nex = node
        self.tail = node
        if self.length == 0:
            self.head = node
        self.length += 1

    def remove(self, index: int) -> bool:
        if self.length == 0 or index >= self.length:
            return False
        if index == 0:
            self.head = self.head.nex
            self.length -= 1
            return True
        cur = self.head
        while index > 1:
            cur = cur.nex
            index -= 1
        cur.nex = cur.nex.nex
        if index == self.length - 1:
            self.tail = cur
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        res = []
        cur = self.head
        while cur:
            res.append(cur.val)
            cur = cur.nex
        return res

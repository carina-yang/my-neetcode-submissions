class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        curr = self.head.next
        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        if index == 0:
            self.addAtHead(val)
            return

        node = ListNode(val)
        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        node.next = prev.next
        prev.next = node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.length:
          
            prev = self.head
            for _ in range(index):
                prev = prev.next

            prev.next = prev.next.next
            self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
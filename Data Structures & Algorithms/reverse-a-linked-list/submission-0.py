# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_head = ListNode(head.val)
        cur = head.next
        while cur:
            node = ListNode(cur.val)
            node.next = new_head
            new_head = node
            cur = cur.next
        return new_head
        
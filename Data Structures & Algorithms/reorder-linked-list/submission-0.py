# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        middle = slow

        prev = None
        cur = middle.next
        middle.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        p2 = prev
        p1 = head

        while p1.next and p2:
            next_node1 = p1.next
            next_node2 = p2.next
            p1.next = p2
            p1.next.next = next_node1
            p1 = next_node1
            p2 = next_node2
        
        
        

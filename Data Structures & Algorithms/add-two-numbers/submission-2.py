# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(-1)
        cur = l3
        carry_over = 0
        while l1 or l2:
            l1_val, l2_val = 0, 0

            if l1:
                l1_val = l1.val
                l1 = l1.next

            if l2:
                l2_val = l2.val
                l2 = l2.next
                
            val = l1_val + l2_val + carry_over
            remainder = val % 10
            carry_over = val // 10

            node = ListNode(remainder)
            cur.next = node
            cur = cur.next
        
        if carry_over == 1:
            node = ListNode(carry_over)
            cur.next = node
        
        return l3.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = None
        cur1 = list1
        cur2 = list2
        cur = None      
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                if not head:
                    head = cur1
                    cur = head
                else:
                    cur.next = cur1
                    cur = cur.next
                cur1 = cur1.next
            else:
                if not head:
                    head = cur2
                    cur = head
                else:
                    cur.next = cur2
                    cur = cur.next
                cur2 = cur2.next
        cur.next = (cur2 if cur2 else cur1)
        
        return head

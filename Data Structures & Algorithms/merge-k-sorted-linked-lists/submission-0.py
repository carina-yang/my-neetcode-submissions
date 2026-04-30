# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur_res = dummy
        min_index = 0
        k = len(lists)
        if k == 0: 
            return dummy.next
        while True:
            for i in range(k):
                if not lists[min_index] and lists[i]:
                    min_index = i

                if lists[i]:
                    if lists[i].val <= lists[min_index].val:
                        min_index = i
            
            if not lists[min_index]:
                cur_res.next = None
                break

            cur_res.next = lists[min_index]
            lists[min_index] = lists[min_index].next
            cur_res = cur_res.next
        
        return dummy.next

            
                    

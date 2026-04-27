# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = {None: None}
        cur1 = head
        while cur1:
            node = Node(cur1.val)
            stack[cur1] = node
            cur1 = cur1.next
        
        cur1 = head
        while cur1:
            random = cur1.random
            stack[cur1].random = stack[random]
            stack[cur1].next = stack[cur1.next]
            cur1 = cur1.next

        return stack[head]

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        nodes = {}
        while curr is not None:
            nodes[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        newcurr = None
        while curr is not None:
            newcurr = nodes.get(curr)
            newcurr.next = nodes.get(curr.next)
            newcurr.random = nodes.get(curr.random)

            curr = curr.next
            newcurr = newcurr.next

        return nodes.get(head)
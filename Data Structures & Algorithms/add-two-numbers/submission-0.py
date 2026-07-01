# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0,None)
        curr = dummy
        while l1 is not None or l2 is not None or carry != 0:
            l1val = 0
            l2val = 0
            val = 0

            if l1 is not None:
                l1val = l1.val
                l1 = l1.next
            if l2 is not None:
                l2val = l2.val
                l2 = l2.next

            val = l2val +l1val + carry

            if val > 9:
                carry = 1
                val = val % 10
            else:
                carry = 0

            curr.next = ListNode(val, None)
            curr = curr.next
            
        return dummy.next

            
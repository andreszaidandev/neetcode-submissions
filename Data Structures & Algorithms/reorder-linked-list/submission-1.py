# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        l1 = head
        l2 = self.reverseList(slow.next)
        slow.next = None

        while l2 is not None:
            temp = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp
            
            l1 = temp
            l2 = temp2


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            newhead = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return newhead



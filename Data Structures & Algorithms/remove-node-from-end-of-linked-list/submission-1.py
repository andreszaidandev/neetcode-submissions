# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #variables
        fast = head
        slow = head
        prev = None
        #move fast to be exactly n spaces ahead of slow
        for i in range(n):
            fast = fast.next
        #if fast is none we are at the end of the list so we need to remove the head.
        if fast is None:
            return slow.next
        #we need to move both slow and fast until fast reaches the end of the list
        else:   
            while fast is not None:
                prev = slow
                slow = slow.next
                fast = fast.next
            #we set prev.next to skip slow.
            prev.next = slow.next
            return head
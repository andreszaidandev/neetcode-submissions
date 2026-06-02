class LinkedList:
    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None
            
    def __init__(self):
        self.head = self.ListNode(-1)
        self.tail = self.head
        
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = self.ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        self.tail.next = self.ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        for i in range(index):
            if curr.next:
                curr = curr.next
            else:
                return False
        
        if curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    remainder = 0
    root = n = ListNode()
    while l1 or l2 or remainder:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        l1 = l1.next if l1 else ListNode()
        l2 = l2.next if l2 else ListNode()
        remainder, val = divmod(v1 + v2 + remainder, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next
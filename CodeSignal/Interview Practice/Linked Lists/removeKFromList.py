# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    while l and l.value == k:
        l = l.next
    curr = l
    while curr:
        if curr.next and curr.next.value == k:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return l
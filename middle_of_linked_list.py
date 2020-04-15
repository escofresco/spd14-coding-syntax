# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def middleNode(self, head: ListNode) -> ListNode:
    ## Use two pointers to get to middle
    slow = fast = head
    while (fast is not None and
           fast.next is not None):
        slow = slow.next
        fast = fast.next.next

    is_even = fast is None
    return (slow, slow.next) if is_even else (slow,)

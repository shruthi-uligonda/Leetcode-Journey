# Reorder List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nextnode = curr.next
            curr.next = prev 
            prev = curr
            curr = nextnode
        first = head
        second = prev
        while second:
            temp = first.next
            first.next = second
            first = second
            second = temp

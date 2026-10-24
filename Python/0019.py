# Remove Nth Node from End of the List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        if count == n:
            return head.next
        temp = head
        value = count - n
        for i in range(value - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head

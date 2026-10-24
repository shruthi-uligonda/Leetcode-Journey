# Odd Even Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        temp1 = head
        temp2 = head.next 
        even_head = temp2 
        while temp2 and temp2.next:
            temp1.next = temp2.next
            temp1 = temp1.next

            temp2.next = temp1.next
            temp2 = temp2.next

        temp1.next = even_head
        return head

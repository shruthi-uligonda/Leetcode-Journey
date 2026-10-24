# Delete the Middle Node of the Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        temp = head
        middle = count // 2
        for i in range (middle - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head
        

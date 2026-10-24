# Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1 = head
        while temp1 and temp1.next:
            if temp1.val == temp1.next.val:
                temp1.next = temp1.next.next
            else:
                temp1 = temp1.next
        return head

# Double a Number Represented as a Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1 = head
        value = 0
        while temp1:
            value = value * 10 + temp1.val
            temp1 = temp1.next
        value *= 2
        digits = str(value)
        temp1 = head
        prev = None
        for digit in digits:
            if temp1:
                temp1.val = int(digit)
                prev = temp1
                temp1 = temp1.next
            else:
                prev.next = ListNode(int(digit))
        return head
        

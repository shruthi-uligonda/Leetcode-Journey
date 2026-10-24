# Delete Nodes from Linked Link Present In Array

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = set(nums)
        while head and head.val in nums:
            head = head.next
        temp = head
        while temp and temp.next:
            if temp.next.val in nums:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head
        
